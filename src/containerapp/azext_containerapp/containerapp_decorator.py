# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long, consider-using-f-string, no-else-return, duplicate-string-formatting-argument, expression-not-assigned, too-many-locals, logging-fstring-interpolation, broad-except, pointless-statement, bare-except
from typing import Dict, Any

from azure.cli.core.commands import AzCliCommand

import time

from azure.cli.core.azclierror import (
    RequiredArgumentMissingError,
    ValidationError)
from azure.cli.core.commands.client_factory import get_subscription_id

from knack.log import get_logger

from msrestazure.tools import parse_resource_id, is_valid_resource_id
from msrest.exceptions import DeserializationError

from ._client_factory import handle_raw_exception
from ._clients import ManagedEnvironmentClient, ContainerAppClient

from ._models import (
    Ingress as IngressModel,
    Configuration as ConfigurationModel,
    Template as TemplateModel,
    RegistryCredentials as RegistryCredentialsModel,
    ContainerApp as ContainerAppModel,
    Dapr as DaprModel,
    ContainerResources as ContainerResourcesModel,
    Scale as ScaleModel,
    Service as ServiceModel,
    Container as ContainerModel,
    ManagedServiceIdentity as ManagedServiceIdentityModel,
    ScaleRule as ScaleRuleModel,
    Volume as VolumeModel,
    VolumeMount as VolumeMountModel)

from ._utils import (_ensure_location_allowed,
                     parse_secret_flags, store_as_secret_and_return_secret_ref, parse_env_var_flags,
                     _convert_object_from_snake_to_camel_case,
                     _object_to_dict, _remove_additional_attributes,
                     _remove_readonly_attributes,
                     _infer_acr_credentials,
                     _ensure_identity_resource_id,
                     validate_container_app_name, register_provider_if_needed,
                     set_managed_identity,
                     create_acrpull_role_assignment, is_registry_msi_system,
                     safe_set, parse_metadata_flags, parse_auth_flags,
                     get_default_workload_profile_name_from_env,
                     ensure_workload_profile_supported, _generate_secret_volume_name,
                     parse_service_bindings, check_unique_bindings, AppType,
                     create_deserializer, process_loaded_yaml, load_yaml_file, get_linker_client)
from ._validators import validate_create, validate_revision_suffix

from ._constants import (CONTAINER_APPS_RP,
                         HELLO_WORLD_IMAGE)

logger = get_logger(__name__)


class BaseContainerAppDecorator:
    def __init__(
        self, cmd: AzCliCommand, client: ContainerAppClient, raw_parameters: Dict, models: str
    ):
        self.raw_param = raw_parameters
        self.cmd = cmd
        self.client = client
        self.models = models

    def register_provider(self):
        raise NotImplementedError()

    def validate_arguments(self):
        raise NotImplementedError()

    def construct_containerapp(self):
        raise NotImplementedError()

    def create_containerapp(self, containerapp_def):
        raise NotImplementedError()

    def construct_containerapp_for_post_process(self, containerapp_def, r):
        raise NotImplementedError()

    def post_process_containerapp(self, containerapp_def, r):
        raise NotImplementedError()

    def get_param(self, key) -> Any:
        return self.raw_param.get(key)

    def set_param(self, key, value):
        self.raw_param[key] = value


class ContainerAppCreateDecorator(BaseContainerAppDecorator):
    def __init__(
        self, cmd: AzCliCommand, client: Any, raw_parameters: Dict, models: str
    ):
        super().__init__(cmd, client, raw_parameters, models)

    def register_provider(self):
        register_provider_if_needed(self.cmd, CONTAINER_APPS_RP)

    def validate_arguments(self):
        validate_container_app_name(self.get_name(), AppType.ContainerApp.name)
        validate_create(self.get_registry_identity(), self.get_registry_pass(), self.get_registry_user(), self.get_registry_server(), self.get_no_wait())
        validate_revision_suffix(self.get_revision_suffix())

    def construct_containerapp(self):
        if self.get_registry_identity() and not is_registry_msi_system(self.get_registry_identity()):
            logger.info("Creating an acrpull role assignment for the registry identity")
            create_acrpull_role_assignment(self.cmd, self.get_registry_server(), self.get_registry_identity(), skip_error=True)

        if self.get_yaml():
            return self.set_up_create_containerapp_yaml(name=self.get_name(), file_name=self.get_yaml())

        if not self.get_image():
            self.set_image(HELLO_WORLD_IMAGE)

        if self.get_managed_env() is None:
            raise RequiredArgumentMissingError('Usage error: --environment is required if not using --yaml')

        # Validate managed environment
        parsed_managed_env = parse_resource_id(self.get_managed_env())
        managed_env_name = parsed_managed_env['name']
        managed_env_rg = parsed_managed_env['resource_group']
        managed_env_info = None

        try:
            managed_env_info = ManagedEnvironmentClient.show(cmd=self.cmd, resource_group_name=managed_env_rg,
                                                             name=managed_env_name)
        except:
            pass

        if not managed_env_info:
            raise ValidationError(
                "The environment '{}' does not exist. Specify a valid environment".format(self.get_managed_env()))

        location = managed_env_info["location"]
        _ensure_location_allowed(self.cmd, location, CONTAINER_APPS_RP, "containerApps")

        if not self.get_workload_profile_name() and "workloadProfiles" in managed_env_info:
            workload_profile_name = get_default_workload_profile_name_from_env(self.cmd, managed_env_info, managed_env_rg)
            self.set_workload_profile_name(workload_profile_name)

        external_ingress = None
        if self.get_ingress() is not None:
            if self.get_ingress().lower() == "internal":
                external_ingress = False
            elif self.get_ingress().lower() == "external":
                external_ingress = True

        ingress_def = None
        if self.get_target_port() is not None and self.get_ingress() is not None:
            ingress_def = IngressModel
            ingress_def["external"] = external_ingress
            ingress_def["targetPort"] = self.get_target_port()
            ingress_def["transport"] = self.get_transport()
            ingress_def["exposedPort"] = self.get_exposed_port() if self.get_transport() == "tcp" else None

        secrets_def = None
        if self.get_secrets() is not None:
            secrets_def = parse_secret_flags(self.get_secrets())

        registries_def = None
        if self.get_registry_server() is not None and not is_registry_msi_system(self.get_registry_identity()):
            registries_def = RegistryCredentialsModel
            registries_def["server"] = self.get_registry_server()

            # Infer credentials if not supplied and its azurecr
            if (self.get_registry_user() is None or self.get_registry_pass() is None) and self.get_registry_identity() is None:
                registry_user, registry_pass = _infer_acr_credentials(self.cmd, self.get_registry_server(), self.get_disable_warnings())
                self.set_registry_user(registry_user)
                self.set_registry_pass(registry_pass)

            if not self.get_registry_identity():
                registries_def["username"] = self.get_registry_user()

                if secrets_def is None:
                    secrets_def = []
                registries_def["passwordSecretRef"] = store_as_secret_and_return_secret_ref(secrets_def, self.get_registry_user(),
                                                                                            self.get_registry_server(),
                                                                                            self.get_registry_pass(),
                                                                                            disable_warnings=self.get_disable_warnings())
            else:
                registries_def["identity"] = self.get_registry_identity()

        dapr_def = None
        if self.get_dapr_enabled():
            dapr_def = DaprModel
            dapr_def["enabled"] = True
            dapr_def["appId"] = self.get_dapr_app_id()
            dapr_def["appPort"] = self.get_dapr_app_port()
            dapr_def["appProtocol"] = self.get_dapr_app_protocol()
            dapr_def["httpReadBufferSize"] = self.get_dapr_http_read_buffer_size()
            dapr_def["httpMaxRequestSize"] = self.get_dapr_http_max_request_size()
            dapr_def["logLevel"] = self.get_dapr_log_level()
            dapr_def["enableApiLogging"] = self.get_dapr_enable_api_logging()

        service_def = None
        if self.get_service_type():
            service_def = ServiceModel
            service_def["type"] = self.get_service_type()

        config_def = ConfigurationModel
        config_def["secrets"] = secrets_def
        config_def["activeRevisionsMode"] = self.get_revisions_mode()
        config_def["ingress"] = ingress_def
        config_def["registries"] = [registries_def] if registries_def is not None else None
        config_def["dapr"] = dapr_def
        config_def["service"] = service_def if service_def is not None else None

        # Identity actions
        identity_def = ManagedServiceIdentityModel
        identity_def["type"] = "None"

        assign_system_identity = self.get_system_assigned()
        if self.get_user_assigned():
            assign_user_identities = [x.lower() for x in self.get_user_assigned()]
        else:
            assign_user_identities = []

        if assign_system_identity and assign_user_identities:
            identity_def["type"] = "SystemAssigned, UserAssigned"
        elif assign_system_identity:
            identity_def["type"] = "SystemAssigned"
        elif assign_user_identities:
            identity_def["type"] = "UserAssigned"

        if assign_user_identities:
            identity_def["userAssignedIdentities"] = {}
            subscription_id = get_subscription_id(self.cmd.cli_ctx)

            for r in assign_user_identities:
                r = _ensure_identity_resource_id(subscription_id, self.get_resource_group_name(), r)
                identity_def["userAssignedIdentities"][r] = {}  # pylint: disable=unsupported-assignment-operation

        scale_def = self.set_up_scale_rule()

        resources_def = None
        if self.get_cpu() is not None or self.get_memory() is not None:
            resources_def = ContainerResourcesModel
            resources_def["cpu"] = self.get_cpu()
            resources_def["memory"] = self.get_memory()

        container_def = ContainerModel
        container_def["name"] = self.get_container_name() if self.get_container_name() else self.get_name()
        container_def["image"] = self.get_image() if not is_registry_msi_system(self.get_registry_identity()) else HELLO_WORLD_IMAGE
        if self.get_env_vars() is not None:
            container_def["env"] = parse_env_var_flags(self.get_env_vars())
        if self.get_startup_command() is not None:
            container_def["command"] = self.get_startup_command()
        if self.get_args() is not None:
            container_def["args"] = self.get_args()
        if resources_def is not None:
            container_def["resources"] = resources_def

        template_def = TemplateModel

        service_bindings_def_list = None
        service_connectors_def_list = None

        if self.get_service_bindings() is not None:
            service_connectors_def_list, service_bindings_def_list = parse_service_bindings(self.cmd, self.get_service_bindings(),
                                                                                            self.get_resource_group_name(), self.get_name())
            self.set_service_connectors_def_list(service_connectors_def_list)
            unique_bindings = check_unique_bindings(self.cmd, service_connectors_def_list, service_bindings_def_list,
                                                    self.get_resource_group_name(), self.get_name())
            if not unique_bindings:
                raise ValidationError("Binding names across managed and dev services should be unique.")

        template_def["containers"] = [container_def]
        template_def["scale"] = scale_def
        template_def["serviceBinds"] = service_bindings_def_list

        if self.get_secret_volume_mount() is not None:
            volume_def = VolumeModel
            volume_mount_def = VolumeMountModel
            # generate a volume name
            volume_def["name"] = _generate_secret_volume_name()
            volume_def["storageType"] = "Secret"

            # mount the volume to the container
            volume_mount_def["volumeName"] = volume_def["name"]
            volume_mount_def["mountPath"] = self.get_secret_volume_mount()
            container_def["volumeMounts"] = [volume_mount_def]
            template_def["volumes"] = [volume_def]

        if self.get_revision_suffix() is not None and not is_registry_msi_system(self.get_registry_identity()):
            template_def["revisionSuffix"] = self.get_revision_suffix()

        containerapp_def = ContainerAppModel
        containerapp_def["location"] = location
        containerapp_def["identity"] = identity_def
        containerapp_def["properties"]["environmentId"] = self.get_managed_env()
        containerapp_def["properties"]["configuration"] = config_def
        containerapp_def["properties"]["template"] = template_def
        containerapp_def["tags"] = self.get_tags()

        if self.get_workload_profile_name():
            containerapp_def["properties"]["workloadProfileName"] = self.get_workload_profile_name()
            ensure_workload_profile_supported(self.cmd, managed_env_name, managed_env_rg, self.get_workload_profile_name(),
                                              managed_env_info)

        if self.get_registry_identity():
            if is_registry_msi_system(self.get_registry_identity()):
                set_managed_identity(self.cmd, self.get_resource_group_name(), containerapp_def, system_assigned=True)
            else:
                set_managed_identity(self.cmd, self.get_resource_group_name(), containerapp_def, user_assigned=[self.get_registry_identity()])
        return containerapp_def

    def create_containerapp(self, containerapp_def):
        try:
            r = self.client.create_or_update(
                cmd=self.cmd, resource_group_name=self.get_resource_group_name(), name=self.get_name(), container_app_envelope=containerapp_def,
                no_wait=self.get_no_wait())

            return r
        except Exception as e:
            handle_raw_exception(e)

    def construct_containerapp_for_post_process(self, containerapp_def, r):
        if is_registry_msi_system(self.get_registry_identity()):
            while r["properties"]["provisioningState"] == "InProgress":
                r = self.client.show(self.cmd, self.get_resource_group_name(), self.get_name())
                time.sleep(10)
            logger.info("Creating an acrpull role assignment for the system identity")
            system_sp = r["identity"]["principalId"]
            create_acrpull_role_assignment(self.cmd, self.get_registry_server(), registry_identity=None, service_principal=system_sp)
            safe_set(containerapp_def, "properties", "template", "containers", "image", value=self.get_image())
            safe_set(containerapp_def, "properties", "template", "revisionSuffix", value=self.get_revision_suffix())

            registries_def = RegistryCredentialsModel
            registries_def["server"] = self.get_registry_server()
            registries_def["identity"] = self.get_registry_identity()
            safe_set(containerapp_def, "properties", "configuration", "registries", value=[registries_def])
            return containerapp_def

    def post_process_containerapp(self, containerapp_def, r):
        if is_registry_msi_system(self.get_registry_identity()):
            r = self.create_containerapp(containerapp_def)

        if "properties" in r and "provisioningState" in r["properties"] and r["properties"]["provisioningState"].lower() == "waiting" and not self.get_no_wait():
            not self.get_disable_warnings() and logger.warning('Containerapp creation in progress. Please monitor the creation using `az containerapp show -n {} -g {}`'.format(self.get_name, self.get_resource_group_name()))

        if "configuration" in r["properties"] and "ingress" in r["properties"]["configuration"] and r["properties"]["configuration"]["ingress"] and "fqdn" in r["properties"]["configuration"]["ingress"]:
            not self.get_disable_warnings() and logger.warning("\nContainer app created. Access your app at https://{}/\n".format(r["properties"]["configuration"]["ingress"]["fqdn"]))
        else:
            target_port = self.get_target_port() or "<port>"
            not self.get_disable_warnings() and logger.warning("\nContainer app created. To access it over HTTPS, enable ingress: "
                                                    "az containerapp ingress enable -n %s -g %s --type external --target-port %s"
                                                    " --transport auto\n", self.get_name(), self.get_resource_group_name(), target_port)

        if self.get_service_connectors_def_list() is not None:
            linker_client = get_linker_client(self.cmd)

            for item in self.get_service_connectors_def_list():
                while r is not None and r["properties"]["provisioningState"].lower() == "inprogress":
                    r = self.client.show(self.cmd, self.get_resource_group_name(), self.get_name())
                    time.sleep(1)
                linker_client.linker.begin_create_or_update(resource_uri=r["id"],
                                                            parameters=item["parameters"],
                                                            linker_name=item["linker_name"]).result()
        return r

    def set_up_create_containerapp_yaml(self, name, file_name):
        if self.get_image() or self.get_managed_env() or self.get_min_replicas() or self.get_max_replicas() or self.get_target_port() or self.get_ingress() or \
                self.get_revisions_mode() or self.get_secrets() or self.get_env_vars() or self.get_cpu() or self.get_memory() or self.get_registry_server() or \
                self.get_registry_user() or self.get_registry_pass() or self.get_dapr_enabled() or self.get_dapr_app_port() or self.get_dapr_app_id() or \
                self.get_startup_command() or self.get_args() or self.get_tags():
            not self.get_disable_warnings() and logger.warning(
                'Additional flags were passed along with --yaml. These flags will be ignored, and the configuration defined in the yaml will be used instead')

        yaml_containerapp = process_loaded_yaml(load_yaml_file(file_name))
        if type(yaml_containerapp) != dict:  # pylint: disable=unidiomatic-typecheck
            raise ValidationError(
                'Invalid YAML provided. Please see https://aka.ms/azure-container-apps-yaml for a valid containerapps YAML spec.')

        if not yaml_containerapp.get('name'):
            yaml_containerapp['name'] = name
        elif yaml_containerapp.get('name').lower() != name.lower():
            logger.warning(
                'The app name provided in the --yaml file "{}" does not match the one provided in the --name flag "{}". The one provided in the --yaml file will be used.'.format(
                    yaml_containerapp.get('name'), name))
        name = yaml_containerapp.get('name')

        if not yaml_containerapp.get('type'):
            yaml_containerapp['type'] = 'Microsoft.App/containerApps'
        elif yaml_containerapp.get('type').lower() != "microsoft.app/containerapps":
            raise ValidationError('Containerapp type must be \"Microsoft.App/ContainerApps\"')

        # Deserialize the yaml into a ContainerApp object. Need this since we're not using SDK
        containerapp_def = None
        try:
            deserializer = create_deserializer(self.models)

            containerapp_def = deserializer('ContainerApp', yaml_containerapp)
        except DeserializationError as ex:
            raise ValidationError(
                'Invalid YAML provided. Please see https://aka.ms/azure-container-apps-yaml for a valid containerapps YAML spec.') from ex

        # Remove tags before converting from snake case to camel case, then re-add tags. We don't want to change the case of the tags. Need this since we're not using SDK
        tags = None
        if yaml_containerapp.get('tags'):
            tags = yaml_containerapp.get('tags')
            del yaml_containerapp['tags']

        containerapp_def = _convert_object_from_snake_to_camel_case(_object_to_dict(containerapp_def))
        containerapp_def['tags'] = tags

        # After deserializing, some properties may need to be moved under the "properties" attribute. Need this since we're not using SDK
        containerapp_def = process_loaded_yaml(containerapp_def)

        # Remove "additionalProperties" and read-only attributes that are introduced in the deserialization. Need this since we're not using SDK
        _remove_additional_attributes(containerapp_def)
        _remove_readonly_attributes(containerapp_def)

        # Remove extra workloadProfileName introduced in deserialization
        if "workloadProfileName" in containerapp_def:
            del containerapp_def["workloadProfileName"]

        # Validate managed environment
        if not containerapp_def["properties"].get('environmentId'):
            raise RequiredArgumentMissingError(
                'environmentId is required. This can be retrieved using the `az containerapp env show -g MyResourceGroup -n MyContainerappEnvironment --query id` command. Please see https://aka.ms/azure-container-apps-yaml for a valid containerapps YAML spec.')

        env_id = containerapp_def["properties"]['environmentId']
        env_name = None
        env_rg = None
        env_info = None

        if is_valid_resource_id(env_id):
            parsed_managed_env = parse_resource_id(env_id)
            env_name = parsed_managed_env['name']
            env_rg = parsed_managed_env['resource_group']
        else:
            raise ValidationError('Invalid environmentId specified. Environment not found')

        try:
            env_info = ManagedEnvironmentClient.show(cmd=self.cmd, resource_group_name=env_rg, name=env_name)
        except:
            pass

        if not env_info:
            raise ValidationError("The environment '{}' in resource group '{}' was not found".format(env_name, env_rg))

        # Validate location
        if not containerapp_def.get('location'):
            containerapp_def['location'] = env_info['location']

        return containerapp_def

    def get_name(self):
        return self.get_param("name")

    def get_resource_group_name(self):
        return self.get_param("resource_group_name")

    def get_yaml(self):
        return self.get_param("yaml")

    def get_image(self):
        return self.get_param("image")

    def set_image(self, image):
        self.set_param("image", image)

    def get_container_name(self):
        return self.get_param("container_name")

    def get_managed_env(self):
        return self.get_param("managed_env")

    def get_min_replicas(self):
        return self.get_param("min_replicas")

    def get_max_replicas(self):
        return self.get_param("max_replicas")

    def get_scale_rule_name(self):
        return self.get_param("scale_rule_name")

    def set_up_scale_rule(self):
        scale_def = None
        if self.get_min_replicas() is not None or self.get_max_replicas() is not None:
            scale_def = ScaleModel
            scale_def["minReplicas"] = self.get_min_replicas()
            scale_def["maxReplicas"] = self.get_max_replicas()

        scale_rule_type = self.get_scale_rule_type()
        scale_rule_name = self.get_scale_rule_name()
        scale_rule_auth = self.get_scale_rule_auth()
        scale_rule_metadata = self.get_scale_rule_metadata()
        scale_rule_http_concurrency = self.get_scale_rule_http_concurrency()
        if self.get_scale_rule_name():
            if not scale_rule_type:
                scale_rule_type = "http"
            scale_rule_type = scale_rule_type.lower()
            scale_rule_def = ScaleRuleModel
            curr_metadata = {}
            if self.get_scale_rule_http_concurrency():
                if scale_rule_type in ('http', 'tcp'):
                    curr_metadata["concurrentRequests"] = str(scale_rule_http_concurrency)
            metadata_def = parse_metadata_flags(scale_rule_metadata, curr_metadata)
            auth_def = parse_auth_flags(scale_rule_auth)
            if scale_rule_type == "http":
                scale_rule_def["name"] = scale_rule_name
                scale_rule_def["custom"] = None
                scale_rule_def["http"] = {}
                scale_rule_def["http"]["metadata"] = metadata_def
                scale_rule_def["http"]["auth"] = auth_def
            else:
                scale_rule_def["name"] = scale_rule_name
                scale_rule_def["http"] = None
                scale_rule_def["custom"] = {}
                scale_rule_def["custom"]["type"] = scale_rule_type
                scale_rule_def["custom"]["metadata"] = metadata_def
                scale_rule_def["custom"]["auth"] = auth_def
            if not scale_def:
                scale_def = ScaleModel
            scale_def["rules"] = [scale_rule_def]
            return scale_def

    def get_scale_rule_type(self):
        return self.get_param("scale_rule_type")

    def set_scale_rule_type(self, scale_rule_type):
        self.set_param("scale_rule_type", scale_rule_type)

    def get_scale_rule_http_concurrency(self):
        return self.get_param("scale_rule_http_concurrency")

    def get_scale_rule_metadata(self):
        return self.get_param("scale_rule_metadata")

    def get_scale_rule_auth(self):
        return self.get_param("scale_rule_auth")

    def get_target_port(self):
        return self.get_param("target_port")

    def get_exposed_port(self):
        return self.get_param("exposed_port")

    def get_transport(self):
        return self.get_param("transport")

    def get_ingress(self):
        return self.get_param("ingress")

    def get_revisions_mode(self):
        return self.get_param("revisions_mode")

    def get_secrets(self):
        return self.get_param("secrets")

    def get_env_vars(self):
        return self.get_param("env_vars")

    def get_cpu(self):
        return self.get_param("cpu")

    def get_memory(self):
        return self.get_param("memory")

    def get_registry_server(self):
        return self.get_param("registry_server")

    def get_registry_user(self):
        return self.get_param("registry_user")

    def set_registry_user(self, registry_user):
        self.set_param("registry_user", registry_user)

    def get_registry_pass(self):
        return self.get_param("registry_pass")

    def set_registry_pass(self, registry_pass):
        self.set_param("registry_pass", registry_pass)

    def get_dapr_enabled(self):
        return self.get_param("dapr_enabled")

    def get_dapr_app_port(self):
        return self.get_param("dapr_app_port")

    def get_dapr_app_id(self):
        return self.get_param("dapr_app_id")

    def get_dapr_app_protocol(self):
        return self.get_param("dapr_app_protocol")

    def get_dapr_http_read_buffer_size(self):
        return self.get_param("dapr_http_read_buffer_size")

    def get_dapr_http_max_request_size(self):
        return self.get_param("dapr_http_max_request_size")

    def get_dapr_log_level(self):
        return self.get_param("dapr_log_level")

    def get_dapr_enable_api_logging(self):
        return self.get_param("dapr_enable_api_logging")

    def get_service_type(self):
        return self.get_param("service_type")

    def get_service_bindings(self):
        return self.get_param("service_bindings")

    def get_revision_suffix(self):
        return self.get_param("revision_suffix")

    def get_startup_command(self):
        return self.get_param("startup_command")

    def get_args(self):
        return self.get_param("args")

    def get_tags(self):
        return self.get_param("tags")

    def get_no_wait(self):
        return self.get_param("no_wait")

    def get_system_assigned(self):
        return self.get_param("system_assigned")

    def get_disable_warnings(self):
        return self.get_param("disable_warnings")

    def get_user_assigned(self):
        return self.get_param("user_assigned")

    def get_registry_identity(self):
        return self.get_param("registry_identity")

    def get_workload_profile_name(self):
        return self.get_param("workload_profile_name")

    def set_workload_profile_name(self, workload_profile_name):
        self.set_param("workload_profile_name", workload_profile_name)

    def get_secret_volume_mount(self):
        return self.get_param("secret_volume_mount")

    def get_service_connectors_def_list(self):
        return self.get_param("service_connectors_def_list")

    def set_service_connectors_def_list(self, service_connectors_def_list):
        self.set_param("service_connectors_def_list", service_connectors_def_list)
