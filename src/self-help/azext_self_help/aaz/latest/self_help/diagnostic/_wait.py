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
    "self-help diagnostic wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/{scope}/providers/microsoft.help/diagnostics/{}", "2023-09-01-preview"],
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
        _args_schema.diagnostic_name = AAZStrArg(
            options=["--diagnostic-name"],
            help="Unique resource name for insight resources",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z0-9-+@()_]+$",
                max_length=100,
                min_length=1,
            ),
        )
        _args_schema.scope = AAZStrArg(
            options=["--scope"],
            help="This is an extension resource provider and only resource level extension is supported at the moment.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DiagnosticsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class DiagnosticsGet(AAZHttpOperation):
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
                "/{scope}/providers/Microsoft.Help/diagnostics/{diagnosticsResourceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "diagnosticsResourceName", self.ctx.args.diagnostic_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "scope", self.ctx.args.scope,
                    skip_quote=True,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-09-01-preview",
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
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.accepted_at = AAZStrType(
                serialized_name="acceptedAt",
                flags={"read_only": True},
            )
            properties.diagnostics = AAZListType(
                flags={"read_only": True},
            )
            properties.global_parameters = AAZDictType(
                serialized_name="globalParameters",
            )
            properties.insights = AAZListType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            diagnostics = cls._schema_on_200.properties.diagnostics
            diagnostics.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.diagnostics.Element
            _element.error = AAZObjectType()
            _WaitHelper._build_schema_error_read(_element.error)
            _element.insights = AAZListType()
            _element.solution_id = AAZStrType(
                serialized_name="solutionId",
            )
            _element.status = AAZStrType()

            insights = cls._schema_on_200.properties.diagnostics.Element.insights
            insights.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.diagnostics.Element.insights.Element
            _element.id = AAZStrType()
            _element.importance_level = AAZStrType(
                serialized_name="importanceLevel",
            )
            _element.results = AAZStrType()
            _element.title = AAZStrType()

            global_parameters = cls._schema_on_200.properties.global_parameters
            global_parameters.Element = AAZStrType()

            insights = cls._schema_on_200.properties.insights
            insights.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.insights.Element
            _element.additional_parameters = AAZDictType(
                serialized_name="additionalParameters",
            )
            _element.solution_id = AAZStrType(
                serialized_name="solutionId",
            )

            additional_parameters = cls._schema_on_200.properties.insights.Element.additional_parameters
            additional_parameters.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
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

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_error_read = None

    @classmethod
    def _build_schema_error_read(cls, _schema):
        if cls._schema_error_read is not None:
            _schema.code = cls._schema_error_read.code
            _schema.details = cls._schema_error_read.details
            _schema.message = cls._schema_error_read.message
            _schema.type = cls._schema_error_read.type
            return

        cls._schema_error_read = _schema_error_read = AAZObjectType()

        error_read = _schema_error_read
        error_read.code = AAZStrType(
            flags={"read_only": True},
        )
        error_read.details = AAZListType()
        error_read.message = AAZStrType(
            flags={"read_only": True},
        )
        error_read.type = AAZStrType(
            flags={"read_only": True},
        )

        details = _schema_error_read.details
        details.Element = AAZObjectType()
        cls._build_schema_error_read(details.Element)

        _schema.code = cls._schema_error_read.code
        _schema.details = cls._schema_error_read.details
        _schema.message = cls._schema_error_read.message
        _schema.type = cls._schema_error_read.type


__all__ = ["Wait"]
