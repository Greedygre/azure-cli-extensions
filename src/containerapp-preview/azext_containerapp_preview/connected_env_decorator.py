# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
from typing import Any, Dict

from azure.cli.core.azclierror import ResourceNotFoundError, ValidationError
from azure.cli.core.commands import AzCliCommand
from msrestazure.tools import is_valid_resource_id

from ._client_factory import handle_raw_exception
from ._constants import CONTAINER_APP_EXTENSION_TYPE, CONNECTED_ENVIRONMENT_RESOURCE_TYPE, CONTAINER_APPS_RP
from ._decorator_utils import list_resource_locations
from ._models import ConnectedEnvironment as ConnectedEnvironmentModel, ExtendedLocation as ExtendedLocationModel
from ._utils import (get_cluster_extension, get_custom_location, _get_azext_containerapp_module)


class ConnectedEnvironmentDecorator(_get_azext_containerapp_module("azext_containerapp.base_resource").BaseResource):
    def __init__(
        self, cmd: AzCliCommand, client: Any, raw_parameters: Dict, models: str, resource_type: str
    ):
        super().__init__(cmd, client, raw_parameters, models)
        self.resource_type = resource_type
        self.azext_default_utils = _get_azext_containerapp_module("azext_containerapp._utils")

    def list(self):
        connected_envs = super().list()
        custom_location = self.get_argument_custom_location()
        if custom_location:
            connected_envs = [c for c in connected_envs if c["extendedLocation"]["name"].lower() == custom_location.lower()]

        return connected_envs

    def _validate_environment_location_and_set_default_location(self):
        res_locations = list_resource_locations(self.cmd.cli_ctx, self.resource_type)

        allowed_locs = ", ".join(res_locations)

        if self.get_argument_location():
            try:
                self.azext_default_utils._ensure_location_allowed(self.cmd, self.get_argument_location(), CONTAINER_APPS_RP, CONNECTED_ENVIRONMENT_RESOURCE_TYPE)

            except Exception as e:  # pylint: disable=broad-except
                raise ValidationError("You cannot create a Containerapp connected environment in location {}. List of eligible locations: {}.".format(self.get_argument_location(), allowed_locs)) from e
        else:
            self.set_argument_location(res_locations[0])

    def _validate_custom_location(self, custom_location=None):
        if not is_valid_resource_id(custom_location):
            raise ValidationError('{} is not a valid Azure resource ID.'.format(custom_location))

        r = get_custom_location(cmd=self.cmd, custom_location_id=custom_location)
        if r is None:
            raise ResourceNotFoundError(
                "Cannot find custom location with custom location ID {}".format(custom_location))

        # check extension type
        check_extension_type = False
        for extension_id in r.cluster_extension_ids:
            extension = get_cluster_extension(self.cmd, extension_id)
            if extension.extension_type.lower() == CONTAINER_APP_EXTENSION_TYPE:
                check_extension_type = True
                break
        if not check_extension_type:
            raise ValidationError('There is no Microsoft.App.Environment extension found associated with custom location {}'.format(custom_location))

    def get_argument_custom_location(self):
        return self.get_param("custom_location")

    def get_argument_location(self):
        return self.get_param("location")

    def get_argument_tags(self):
        return self.get_param("tags")

    def get_argument_static_ip(self):
        return self.get_param("static_ip")

    def get_argument_dapr_ai_connection_string(self):
        return self.get_param("dapr_ai_connection_string")

    def set_argument_location(self, location):
        self.set_param("location", location)


class ConnectedEnvironmentPreviewCreateDecorator(ConnectedEnvironmentDecorator):
    def __init__(
            self, cmd: AzCliCommand, client: Any, raw_parameters: Dict, models: str, resource_type: str
    ):
        super().__init__(cmd, client, raw_parameters, models, resource_type)
        self.connected_env_def = ConnectedEnvironmentModel

    def validate_arguments(self):
        self._validate_environment_location_and_set_default_location()
        self._validate_custom_location(self.get_argument_custom_location())

    def construct_connected_environment(self):
        self.connected_env_def["location"] = self.get_argument_location()
        self.connected_env_def["properties"]["daprAIConnectionString"] = self.get_argument_dapr_ai_connection_string()
        self.connected_env_def["properties"]["staticIp"] = self.get_argument_static_ip()
        self.connected_env_def["tags"] = self.get_argument_tags()
        extended_location_def = ExtendedLocationModel
        extended_location_def["name"] = self.get_argument_custom_location()
        extended_location_def["type"] = "CustomLocation"
        self.connected_env_def["extendedLocation"] = extended_location_def

    def create_connected_environment(self):
        try:
            r = self.client.create(
                cmd=self.cmd, resource_group_name=self.get_argument_resource_group_name(), name=self.get_argument_name(),
                connected_environment_envelope=self.connected_env_def, no_wait=self.get_argument_no_wait())

            return r
        except Exception as e:
            handle_raw_exception(e)
