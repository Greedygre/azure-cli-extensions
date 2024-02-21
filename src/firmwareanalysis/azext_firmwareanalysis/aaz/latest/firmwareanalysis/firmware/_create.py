# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *
import uuid


@register_command(
    "firmwareanalysis firmware create",
)
class Create(AAZCommand):
    """Create a new firmware.

    :example: Create a new firmware.
        az firmwareanalysis firmware create --resource-group {resourceGroupName} --workspace-name {workspaceName} --description {description} --file-name {fileName} --file-size {fileSize} --vendor {vendorName} --model {model} --version {version} --status {status} --status-messages ['hi','message']
    """

    _aaz_info = {
        "version": "2024-01-10",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.iotfirmwaredefense/workspaces/{}/firmwares/{}", "2024-01-10"],
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
        _args_schema.firmware_id = AAZStrArg(
            options=["-n", "--name", "--firmware-id"],
            help="The id of the firmware.",
            default=str(uuid.uuid4()),
            required=False,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["--workspace-name"],
            help="The name of the firmware analysis workspace.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9_.-]*$",
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="User-specified description of the firmware.",
        )
        _args_schema.file_name = AAZStrArg(
            options=["--file-name"],
            arg_group="Properties",
            help="File name for a firmware that user uploaded.",
        )
        _args_schema.file_size = AAZIntArg(
            options=["--file-size"],
            arg_group="Properties",
            help="File size of the uploaded firmware image.",
            nullable=True,
        )
        _args_schema.model = AAZStrArg(
            options=["--model"],
            arg_group="Properties",
            help="Firmware model.",
        )
        _args_schema.status = AAZStrArg(
            options=["--status"],
            arg_group="Properties",
            help="The status of firmware scan.",
            default="Pending",
            enum={"Analyzing": "Analyzing", "Error": "Error", "Extracting": "Extracting", "Pending": "Pending", "Ready": "Ready"},
        )
        _args_schema.status_messages = AAZListArg(
            options=["--status-messages"],
            arg_group="Properties",
            help="A list of errors or other messages generated during firmware analysis",
        )
        _args_schema.vendor = AAZStrArg(
            options=["--vendor"],
            arg_group="Properties",
            help="Firmware vendor.",
        )
        _args_schema.version = AAZStrArg(
            options=["--version"],
            arg_group="Properties",
            help="Firmware version.",
        )

        status_messages = cls._args_schema.status_messages
        status_messages.Element = AAZObjectArg()

        _element = cls._args_schema.status_messages.Element
        _element.error_code = AAZIntArg(
            options=["error-code"],
            help="The error code",
        )
        _element.message = AAZStrArg(
            options=["message"],
            help="The error or status message",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.FirmwaresCreate(ctx=self.ctx)()
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

    class FirmwaresCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTFirmwareDefense/workspaces/{workspaceName}/firmwares/{firmwareId}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "firmwareId", self.ctx.args.firmware_id,
                    required=False,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-01-10",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("fileName", AAZStrType, ".file_name")
                properties.set_prop("fileSize", AAZIntType, ".file_size", typ_kwargs={"nullable": True})
                properties.set_prop("model", AAZStrType, ".model")
                properties.set_prop("status", AAZStrType, ".status")
                properties.set_prop("statusMessages", AAZListType, ".status_messages")
                properties.set_prop("vendor", AAZStrType, ".vendor")
                properties.set_prop("version", AAZStrType, ".version")

            status_messages = _builder.get(".properties.statusMessages")
            if status_messages is not None:
                status_messages.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.statusMessages[]")
            if _elements is not None:
                _elements.set_prop("errorCode", AAZIntType, ".error_code")
                _elements.set_prop("message", AAZStrType, ".message")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.description = AAZStrType()
            properties.file_name = AAZStrType(
                serialized_name="fileName",
            )
            properties.file_size = AAZIntType(
                serialized_name="fileSize",
                nullable=True,
            )
            properties.model = AAZStrType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.status = AAZStrType()
            properties.status_messages = AAZListType(
                serialized_name="statusMessages",
            )
            properties.vendor = AAZStrType()
            properties.version = AAZStrType()

            status_messages = cls._schema_on_200_201.properties.status_messages
            status_messages.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.status_messages.Element
            _element.error_code = AAZIntType(
                serialized_name="errorCode",
            )
            _element.message = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
