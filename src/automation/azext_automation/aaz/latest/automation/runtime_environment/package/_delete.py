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
    "automation runtime-environment package delete",
    confirmation="Are you sure you want to perform this operation?",
)
class Delete(AAZCommand):
    """Delete the package by name.

    :example: Delete the package
        az automation runtime-environment package delete -g rg --automation-account-name myAutomationAccount --runtime-environment-name rt --name rt-package
    """

    _aaz_info = {
        "version": "2023-05-15-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.automation/automationaccounts/{}/runtimeenvironments/{}/packages/{}", "2023-05-15-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return None

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.automation_account_name = AAZStrArg(
            options=["--account", "--automation-account-name"],
            help="The name of the automation account.",
            required=True,
            id_part="name",
        )
        _args_schema.package_name = AAZStrArg(
            options=["-n", "--name", "--package-name"],
            help="The Package name.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.runtime_environment_name = AAZStrArg(
            options=["--environment", "--runtime-environment-name"],
            help="The name of the Runtime Environment.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z][a-zA-Z-_0-9]*$",
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PackageDelete(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class PackageDelete(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)
            if session.http_response.status_code in [204]:
                return self.on_204(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runtimeEnvironments/{runtimeEnvironmentName}/packages/{packageName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "DELETE"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "automationAccountName", self.ctx.args.automation_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "packageName", self.ctx.args.package_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "runtimeEnvironmentName", self.ctx.args.runtime_environment_name,
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
                    "api-version", "2023-05-15-preview",
                    required=True,
                ),
            }
            return parameters

        def on_200(self, session):
            pass

        def on_204(self, session):
            pass


class _DeleteHelper:
    """Helper class for Delete"""


__all__ = ["Delete"]
