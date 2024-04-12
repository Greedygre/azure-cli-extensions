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
    "new-relic monitor monitored-subscription update",
)
class Update(AAZCommand):
    """Update the subscriptions that should be monitored by the NewRelic monitor resource.
    
    :example: Update the subscriptions that should be monitored by the NewRelic monitor resource.
    Please run below commands in the mentioned order
    1) az new-relic monitor monitored-subscription update --resource-group MyResourceGroup --monitor-name MyNewRelicMonitor --configuration-name default --patch-operation AddBegin --subscriptions "[{status:'InProgress',subscription-id:'subscription-id'}]"
    2) az new-relic monitor monitored-subscription update --resource-group MyResourceGroup --monitor-name MyNewRelicMonitor --configuration-name default --patch-operation AddComplete --subscriptions "[{status:'Active',subscription-id:'subscription-id'}]" 
    """

    _aaz_info = {
        "version": "2024-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/newrelic.observability/monitors/{}/monitoredsubscriptions/{}", "2024-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.configuration_name = AAZStrArg(
            options=["--configuration-name"],
            help="The configuration name. Only 'default' value is supported.",
            required=True,
            id_part="child_name_1",
            enum={"default": "default"},
            fmt=AAZStrArgFormat(
                pattern="^.*$",
            ),
        )
        _args_schema.monitor_name = AAZStrArg(
            options=["--monitor-name"],
            help="Name of the Monitoring resource",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^.*$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            options=["--resource-group","--g"],
            help="Name of resource group. You can configure the default group using az configure --defaults group=<name>.",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.monitored_subscription_list = AAZListArg(
            options=["-n", "--subscriptions", "--monitored-subscription-list"],
            arg_group="Properties",
            help="List of subscriptions and the state of the monitoring.",
            nullable=True,
        )
        _args_schema.patch_operation = AAZStrArg(
            options=["--patch-operation"],
            arg_group="Properties",
            help="The operation for the patch on the resource.",
            nullable=True,
            enum={"Active": "Active", "AddBegin": "AddBegin", "AddComplete": "AddComplete", "DeleteBegin": "DeleteBegin", "DeleteComplete": "DeleteComplete"},
        )

        monitored_subscription_list = cls._args_schema.monitored_subscription_list
        monitored_subscription_list.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.monitored_subscription_list.Element
        _element.error = AAZStrArg(
            options=["error"],
            help="The reason of not monitoring the subscription.",
            nullable=True,
        )
        _element.status = AAZStrArg(
            options=["status"],
            help="The state of monitoring.",
            nullable=True,
            enum={"Active": "Active", "Deleting": "Deleting", "Failed": "Failed", "InProgress": "InProgress"},
        )
        _element.subscription_id = AAZStrArg(
            options=["subscription-id"],
            help="The subscriptionId to be monitored.",
            nullable=True,
        )
        _element.tag_rules = AAZObjectArg(
            options=["tag-rules"],
            help="The resource-specific properties for this resource.",
            nullable=True,
        )

        tag_rules = cls._args_schema.monitored_subscription_list.Element.tag_rules
        tag_rules.log_rules = AAZObjectArg(
            options=["log-rules"],
            help="Set of rules for sending logs for the Monitor resource.",
            nullable=True,
        )
        tag_rules.metric_rules = AAZObjectArg(
            options=["metric-rules"],
            help="Set of rules for sending metrics for the Monitor resource.",
            nullable=True,
        )

        log_rules = cls._args_schema.monitored_subscription_list.Element.tag_rules.log_rules
        log_rules.filtering_tags = AAZListArg(
            options=["filtering-tags"],
            help="List of filtering tags to be used for capturing logs. This only takes effect if SendActivityLogs flag is enabled. If empty, all resources will be captured. If only Exclude action is specified, the rules will apply to the list of all available resources. If Include actions are specified, the rules will only include resources with the associated tags.",
            nullable=True,
        )
        log_rules.send_aad_logs = AAZStrArg(
            options=["send-aad-logs"],
            help="Flag specifying if AAD logs should be sent for the Monitor resource.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        log_rules.send_activity_logs = AAZStrArg(
            options=["send-activity-logs"],
            help="Flag specifying if activity logs from Azure resources should be sent for the Monitor resource.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        log_rules.send_subscription_logs = AAZStrArg(
            options=["send-subscription-logs"],
            help="Flag specifying if subscription logs should be sent for the Monitor resource.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )

        filtering_tags = cls._args_schema.monitored_subscription_list.Element.tag_rules.log_rules.filtering_tags
        filtering_tags.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_filtering_tag_update(filtering_tags.Element)

        metric_rules = cls._args_schema.monitored_subscription_list.Element.tag_rules.metric_rules
        metric_rules.filtering_tags = AAZListArg(
            options=["filtering-tags"],
            help="List of filtering tags to be used for capturing metrics.",
            nullable=True,
        )
        metric_rules.send_metrics = AAZStrArg(
            options=["send-metrics"],
            help="Flag specifying if metrics should be sent for the Monitor resource.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        metric_rules.user_email = AAZStrArg(
            options=["user-email"],
            help="User Email",
            nullable=True,
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}$",
            ),
        )

        filtering_tags = cls._args_schema.monitored_subscription_list.Element.tag_rules.metric_rules.filtering_tags
        filtering_tags.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_filtering_tag_update(filtering_tags.Element)
        return cls._args_schema

    _args_filtering_tag_update = None

    @classmethod
    def _build_args_filtering_tag_update(cls, _schema):
        if cls._args_filtering_tag_update is not None:
            _schema.action = cls._args_filtering_tag_update.action
            _schema.name = cls._args_filtering_tag_update.name
            _schema.value = cls._args_filtering_tag_update.value
            return

        cls._args_filtering_tag_update = AAZObjectArg(
            nullable=True,
        )

        filtering_tag_update = cls._args_filtering_tag_update
        filtering_tag_update.action = AAZStrArg(
            options=["action"],
            help="Valid actions for a filtering tag. Exclusion takes priority over inclusion.",
            nullable=True,
            enum={"Exclude": "Exclude", "Include": "Include"},
        )
        filtering_tag_update.name = AAZStrArg(
            options=["name"],
            help="The name (also known as the key) of the tag.",
            nullable=True,
        )
        filtering_tag_update.value = AAZStrArg(
            options=["value"],
            help="The value of the tag.",
            nullable=True,
        )

        _schema.action = cls._args_filtering_tag_update.action
        _schema.name = cls._args_filtering_tag_update.name
        _schema.value = cls._args_filtering_tag_update.value

    def _execute_operations(self):
        self.pre_operations()
        self.MonitoredSubscriptionsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.MonitoredSubscriptionsCreateorUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class MonitoredSubscriptionsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/NewRelic.Observability/monitors/{monitorName}/monitoredSubscriptions/{configurationName}",
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
                    "configurationName", self.ctx.args.configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "monitorName", self.ctx.args.monitor_name,
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
                    "api-version", "2024-01-01",
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
            _UpdateHelper._build_schema_monitored_subscription_properties_read(cls._schema_on_200)

            return cls._schema_on_200

    class MonitoredSubscriptionsCreateorUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/NewRelic.Observability/monitors/{monitorName}/monitoredSubscriptions/{configurationName}",
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
                    "configurationName", self.ctx.args.configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "monitorName", self.ctx.args.monitor_name,
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
                    "api-version", "2024-01-01",
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
                value=self.ctx.vars.instance,
            )

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
            _UpdateHelper._build_schema_monitored_subscription_properties_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("monitoredSubscriptionList", AAZListType, ".monitored_subscription_list")
                properties.set_prop("patchOperation", AAZStrType, ".patch_operation")

            monitored_subscription_list = _builder.get(".properties.monitoredSubscriptionList")
            if monitored_subscription_list is not None:
                monitored_subscription_list.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.monitoredSubscriptionList[]")
            if _elements is not None:
                _elements.set_prop("error", AAZStrType, ".error")
                _elements.set_prop("status", AAZStrType, ".status")
                _elements.set_prop("subscriptionId", AAZStrType, ".subscription_id")
                _elements.set_prop("tagRules", AAZObjectType, ".tag_rules")

            tag_rules = _builder.get(".properties.monitoredSubscriptionList[].tagRules")
            if tag_rules is not None:
                tag_rules.set_prop("logRules", AAZObjectType, ".log_rules")
                tag_rules.set_prop("metricRules", AAZObjectType, ".metric_rules")

            log_rules = _builder.get(".properties.monitoredSubscriptionList[].tagRules.logRules")
            if log_rules is not None:
                log_rules.set_prop("filteringTags", AAZListType, ".filtering_tags")
                log_rules.set_prop("sendAadLogs", AAZStrType, ".send_aad_logs")
                log_rules.set_prop("sendActivityLogs", AAZStrType, ".send_activity_logs")
                log_rules.set_prop("sendSubscriptionLogs", AAZStrType, ".send_subscription_logs")

            filtering_tags = _builder.get(".properties.monitoredSubscriptionList[].tagRules.logRules.filteringTags")
            if filtering_tags is not None:
                _UpdateHelper._build_schema_filtering_tag_update(filtering_tags.set_elements(AAZObjectType, "."))

            metric_rules = _builder.get(".properties.monitoredSubscriptionList[].tagRules.metricRules")
            if metric_rules is not None:
                metric_rules.set_prop("filteringTags", AAZListType, ".filtering_tags")
                metric_rules.set_prop("sendMetrics", AAZStrType, ".send_metrics")
                metric_rules.set_prop("userEmail", AAZStrType, ".user_email")

            filtering_tags = _builder.get(".properties.monitoredSubscriptionList[].tagRules.metricRules.filteringTags")
            if filtering_tags is not None:
                _UpdateHelper._build_schema_filtering_tag_update(filtering_tags.set_elements(AAZObjectType, "."))

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_filtering_tag_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("action", AAZStrType, ".action")
        _builder.set_prop("name", AAZStrType, ".name")
        _builder.set_prop("value", AAZStrType, ".value")

    _schema_filtering_tag_read = None

    @classmethod
    def _build_schema_filtering_tag_read(cls, _schema):
        if cls._schema_filtering_tag_read is not None:
            _schema.action = cls._schema_filtering_tag_read.action
            _schema.name = cls._schema_filtering_tag_read.name
            _schema.value = cls._schema_filtering_tag_read.value
            return

        cls._schema_filtering_tag_read = _schema_filtering_tag_read = AAZObjectType()

        filtering_tag_read = _schema_filtering_tag_read
        filtering_tag_read.action = AAZStrType()
        filtering_tag_read.name = AAZStrType()
        filtering_tag_read.value = AAZStrType()

        _schema.action = cls._schema_filtering_tag_read.action
        _schema.name = cls._schema_filtering_tag_read.name
        _schema.value = cls._schema_filtering_tag_read.value

    _schema_monitored_subscription_properties_read = None

    @classmethod
    def _build_schema_monitored_subscription_properties_read(cls, _schema):
        if cls._schema_monitored_subscription_properties_read is not None:
            _schema.id = cls._schema_monitored_subscription_properties_read.id
            _schema.name = cls._schema_monitored_subscription_properties_read.name
            _schema.properties = cls._schema_monitored_subscription_properties_read.properties
            _schema.type = cls._schema_monitored_subscription_properties_read.type
            return

        cls._schema_monitored_subscription_properties_read = _schema_monitored_subscription_properties_read = AAZObjectType()

        monitored_subscription_properties_read = _schema_monitored_subscription_properties_read
        monitored_subscription_properties_read.id = AAZStrType(
            flags={"read_only": True},
        )
        monitored_subscription_properties_read.name = AAZStrType(
            flags={"read_only": True},
        )
        monitored_subscription_properties_read.properties = AAZObjectType()
        monitored_subscription_properties_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_monitored_subscription_properties_read.properties
        properties.monitored_subscription_list = AAZListType(
            serialized_name="monitoredSubscriptionList",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )

        monitored_subscription_list = _schema_monitored_subscription_properties_read.properties.monitored_subscription_list
        monitored_subscription_list.Element = AAZObjectType()

        _element = _schema_monitored_subscription_properties_read.properties.monitored_subscription_list.Element
        _element.error = AAZStrType()
        _element.status = AAZStrType()
        _element.subscription_id = AAZStrType(
            serialized_name="subscriptionId",
        )
        _element.tag_rules = AAZObjectType(
            serialized_name="tagRules",
        )

        tag_rules = _schema_monitored_subscription_properties_read.properties.monitored_subscription_list.Element.tag_rules
        tag_rules.log_rules = AAZObjectType(
            serialized_name="logRules",
        )
        tag_rules.metric_rules = AAZObjectType(
            serialized_name="metricRules",
        )
        tag_rules.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )

        log_rules = _schema_monitored_subscription_properties_read.properties.monitored_subscription_list.Element.tag_rules.log_rules
        log_rules.filtering_tags = AAZListType(
            serialized_name="filteringTags",
        )
        log_rules.send_aad_logs = AAZStrType(
            serialized_name="sendAadLogs",
        )
        log_rules.send_activity_logs = AAZStrType(
            serialized_name="sendActivityLogs",
        )
        log_rules.send_subscription_logs = AAZStrType(
            serialized_name="sendSubscriptionLogs",
        )

        filtering_tags = _schema_monitored_subscription_properties_read.properties.monitored_subscription_list.Element.tag_rules.log_rules.filtering_tags
        filtering_tags.Element = AAZObjectType()
        cls._build_schema_filtering_tag_read(filtering_tags.Element)

        metric_rules = _schema_monitored_subscription_properties_read.properties.monitored_subscription_list.Element.tag_rules.metric_rules
        metric_rules.filtering_tags = AAZListType(
            serialized_name="filteringTags",
        )
        metric_rules.send_metrics = AAZStrType(
            serialized_name="sendMetrics",
        )
        metric_rules.user_email = AAZStrType(
            serialized_name="userEmail",
        )

        filtering_tags = _schema_monitored_subscription_properties_read.properties.monitored_subscription_list.Element.tag_rules.metric_rules.filtering_tags
        filtering_tags.Element = AAZObjectType()
        cls._build_schema_filtering_tag_read(filtering_tags.Element)

        _schema.id = cls._schema_monitored_subscription_properties_read.id
        _schema.name = cls._schema_monitored_subscription_properties_read.name
        _schema.properties = cls._schema_monitored_subscription_properties_read.properties
        _schema.type = cls._schema_monitored_subscription_properties_read.type


__all__ = ["Update"]