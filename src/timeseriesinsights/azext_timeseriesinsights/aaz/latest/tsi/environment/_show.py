# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "tsi environment show",
)
class Show(AAZCommand):
    """Get the environment with the specified name in the specified subscription and resource group.

    :example: EnvironmentsGet
        az tsi environment show --name "env1" --resource-group "rg1"
    """

    _aaz_info = {
        "version": "2020-05-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.timeseriesinsights/environments/{}", "2020-05-15"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.environment_name = AAZStrArg(
            options=["-n", "--name", "--environment-name"],
            help="The name of the Time Series Insights environment associated with the specified resource group.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="Setting $expand=status will include the status of the internal services of the environment in the Time Series Insights service.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.EnvironmentsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class EnvironmentsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "environmentName", self.ctx.args.environment_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "api-version", "2020-05-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.kind = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.sku = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            sku = cls._schema_on_200.sku
            sku.capacity = AAZIntType(
                flags={"required": True},
            )
            sku.name = AAZStrType(
                flags={"required": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            disc_gen1 = cls._schema_on_200.discriminate_by("kind", "Gen1")
            disc_gen1.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )

            properties = cls._schema_on_200.discriminate_by("kind", "Gen1").properties
            properties.creation_time = AAZStrType(
                serialized_name="creationTime",
                flags={"read_only": True},
            )
            properties.data_access_fqdn = AAZStrType(
                serialized_name="dataAccessFqdn",
                flags={"read_only": True},
            )
            properties.data_access_id = AAZStrType(
                serialized_name="dataAccessId",
                flags={"read_only": True},
            )
            properties.data_retention_time = AAZStrType(
                serialized_name="dataRetentionTime",
                flags={"required": True},
            )
            properties.partition_key_properties = AAZListType(
                serialized_name="partitionKeyProperties",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.status = AAZObjectType(
                flags={"read_only": True},
            )
            _ShowHelper._build_schema_environment_status_read(properties.status)
            properties.storage_limit_exceeded_behavior = AAZStrType(
                serialized_name="storageLimitExceededBehavior",
            )

            partition_key_properties = cls._schema_on_200.discriminate_by("kind", "Gen1").properties.partition_key_properties
            partition_key_properties.Element = AAZObjectType()
            _ShowHelper._build_schema_time_series_id_property_read(partition_key_properties.Element)

            disc_gen2 = cls._schema_on_200.discriminate_by("kind", "Gen2")
            disc_gen2.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )

            properties = cls._schema_on_200.discriminate_by("kind", "Gen2").properties
            properties.creation_time = AAZStrType(
                serialized_name="creationTime",
                flags={"read_only": True},
            )
            properties.data_access_fqdn = AAZStrType(
                serialized_name="dataAccessFqdn",
                flags={"read_only": True},
            )
            properties.data_access_id = AAZStrType(
                serialized_name="dataAccessId",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.status = AAZObjectType(
                flags={"read_only": True},
            )
            _ShowHelper._build_schema_environment_status_read(properties.status)
            properties.storage_configuration = AAZObjectType(
                serialized_name="storageConfiguration",
                flags={"required": True},
            )
            properties.time_series_id_properties = AAZListType(
                serialized_name="timeSeriesIdProperties",
                flags={"required": True},
            )
            properties.warm_store_configuration = AAZObjectType(
                serialized_name="warmStoreConfiguration",
            )

            storage_configuration = cls._schema_on_200.discriminate_by("kind", "Gen2").properties.storage_configuration
            storage_configuration.account_name = AAZStrType(
                serialized_name="accountName",
                flags={"required": True},
            )

            time_series_id_properties = cls._schema_on_200.discriminate_by("kind", "Gen2").properties.time_series_id_properties
            time_series_id_properties.Element = AAZObjectType()
            _ShowHelper._build_schema_time_series_id_property_read(time_series_id_properties.Element)

            warm_store_configuration = cls._schema_on_200.discriminate_by("kind", "Gen2").properties.warm_store_configuration
            warm_store_configuration.data_retention = AAZStrType(
                serialized_name="dataRetention",
                flags={"required": True},
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_environment_status_read = None

    @classmethod
    def _build_schema_environment_status_read(cls, _schema):
        if cls._schema_environment_status_read is not None:
            _schema.ingress = cls._schema_environment_status_read.ingress
            _schema.warm_storage = cls._schema_environment_status_read.warm_storage
            return

        cls._schema_environment_status_read = _schema_environment_status_read = AAZObjectType(
            flags={"read_only": True}
        )

        environment_status_read = _schema_environment_status_read
        environment_status_read.ingress = AAZObjectType(
            flags={"read_only": True},
        )
        environment_status_read.warm_storage = AAZObjectType(
            serialized_name="warmStorage",
            flags={"read_only": True},
        )

        ingress = _schema_environment_status_read.ingress
        ingress.state = AAZStrType()
        ingress.state_details = AAZObjectType(
            serialized_name="stateDetails",
            flags={"read_only": True},
        )

        state_details = _schema_environment_status_read.ingress.state_details
        state_details.code = AAZStrType()
        state_details.message = AAZStrType()

        warm_storage = _schema_environment_status_read.warm_storage
        warm_storage.properties_usage = AAZObjectType(
            serialized_name="propertiesUsage",
            flags={"client_flatten": True, "read_only": True},
        )

        properties_usage = _schema_environment_status_read.warm_storage.properties_usage
        properties_usage.state = AAZStrType()
        properties_usage.state_details = AAZObjectType(
            serialized_name="stateDetails",
            flags={"client_flatten": True, "read_only": True},
        )

        state_details = _schema_environment_status_read.warm_storage.properties_usage.state_details
        state_details.current_count = AAZIntType(
            serialized_name="currentCount",
        )
        state_details.max_count = AAZIntType(
            serialized_name="maxCount",
        )

        _schema.ingress = cls._schema_environment_status_read.ingress
        _schema.warm_storage = cls._schema_environment_status_read.warm_storage

    _schema_time_series_id_property_read = None

    @classmethod
    def _build_schema_time_series_id_property_read(cls, _schema):
        if cls._schema_time_series_id_property_read is not None:
            _schema.name = cls._schema_time_series_id_property_read.name
            _schema.type = cls._schema_time_series_id_property_read.type
            return

        cls._schema_time_series_id_property_read = _schema_time_series_id_property_read = AAZObjectType()

        time_series_id_property_read = _schema_time_series_id_property_read
        time_series_id_property_read.name = AAZStrType()
        time_series_id_property_read.type = AAZStrType()

        _schema.name = cls._schema_time_series_id_property_read.name
        _schema.type = cls._schema_time_series_id_property_read.type


__all__ = ["Show"]
