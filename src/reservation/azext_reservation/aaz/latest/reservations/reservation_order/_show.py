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
    "reservations reservation-order show",
)
class Show(AAZCommand):
    """Get the details of the `ReservationOrder`.

    :example: Get the details of a reservation order
        az reservations reservation-order show --reservation-order-id 50000000-aaaa-bbbb-cccc-200000000005
    """

    _aaz_info = {
        "version": "2022-11-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.capacity/reservationorders/{}", "2022-11-01"],
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
        _args_schema.reservation_order_id = AAZStrArg(
            options=["--reservation-order-id"],
            help="Order Id of the reservation",
            required=True,
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="May be used to expand the planInformation.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ReservationOrderGet(ctx=self.ctx)()
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

    class ReservationOrderGet(AAZHttpOperation):
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
                "/providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}",
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
                    "reservationOrderId", self.ctx.args.reservation_order_id,
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
                    "api-version", "2022-11-01",
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
            _schema_on_200.etag = AAZIntType()
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
            _ShowHelper._build_schema_system_data_read(_schema_on_200.system_data)
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.benefit_start_time = AAZStrType(
                serialized_name="benefitStartTime",
            )
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.created_date_time = AAZStrType(
                serialized_name="createdDateTime",
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.expiry_date = AAZStrType(
                serialized_name="expiryDate",
            )
            properties.expiry_date_time = AAZStrType(
                serialized_name="expiryDateTime",
            )
            properties.original_quantity = AAZIntType(
                serialized_name="originalQuantity",
            )
            properties.plan_information = AAZObjectType(
                serialized_name="planInformation",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.request_date_time = AAZStrType(
                serialized_name="requestDateTime",
            )
            properties.reservations = AAZListType()
            properties.review_date_time = AAZStrType(
                serialized_name="reviewDateTime",
            )
            properties.term = AAZStrType()

            plan_information = cls._schema_on_200.properties.plan_information
            plan_information.next_payment_due_date = AAZStrType(
                serialized_name="nextPaymentDueDate",
            )
            plan_information.pricing_currency_total = AAZObjectType(
                serialized_name="pricingCurrencyTotal",
            )
            _ShowHelper._build_schema_price_read(plan_information.pricing_currency_total)
            plan_information.start_date = AAZStrType(
                serialized_name="startDate",
            )
            plan_information.transactions = AAZListType()

            transactions = cls._schema_on_200.properties.plan_information.transactions
            transactions.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.plan_information.transactions.Element
            _element.billing_account = AAZStrType(
                serialized_name="billingAccount",
            )
            _element.billing_currency_total = AAZObjectType(
                serialized_name="billingCurrencyTotal",
            )
            _ShowHelper._build_schema_price_read(_element.billing_currency_total)
            _element.due_date = AAZStrType(
                serialized_name="dueDate",
            )
            _element.extended_status_info = AAZObjectType(
                serialized_name="extendedStatusInfo",
            )
            _ShowHelper._build_schema_extended_status_info_read(_element.extended_status_info)
            _element.payment_date = AAZStrType(
                serialized_name="paymentDate",
            )
            _element.pricing_currency_total = AAZObjectType(
                serialized_name="pricingCurrencyTotal",
            )
            _ShowHelper._build_schema_price_read(_element.pricing_currency_total)
            _element.status = AAZStrType()

            reservations = cls._schema_on_200.properties.reservations
            reservations.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.reservations.Element
            _element.etag = AAZIntType()
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.kind = AAZStrType()
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType()
            _element.sku = AAZObjectType()
            _ShowHelper._build_schema_sku_name_read(_element.sku)
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _ShowHelper._build_schema_system_data_read(_element.system_data)
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties.reservations.Element.properties
            properties.applied_scope_properties = AAZObjectType(
                serialized_name="appliedScopeProperties",
            )
            _ShowHelper._build_schema_applied_scope_properties_read(properties.applied_scope_properties)
            properties.applied_scope_type = AAZStrType(
                serialized_name="appliedScopeType",
            )
            properties.applied_scopes = AAZListType(
                serialized_name="appliedScopes",
            )
            _ShowHelper._build_schema_applied_scopes_read(properties.applied_scopes)
            properties.archived = AAZBoolType()
            properties.benefit_start_time = AAZStrType(
                serialized_name="benefitStartTime",
            )
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
            )
            properties.capabilities = AAZStrType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.display_provisioning_state = AAZStrType(
                serialized_name="displayProvisioningState",
                flags={"read_only": True},
            )
            properties.effective_date_time = AAZStrType(
                serialized_name="effectiveDateTime",
            )
            properties.expiry_date = AAZStrType(
                serialized_name="expiryDate",
            )
            properties.expiry_date_time = AAZStrType(
                serialized_name="expiryDateTime",
            )
            properties.extended_status_info = AAZObjectType(
                serialized_name="extendedStatusInfo",
            )
            _ShowHelper._build_schema_extended_status_info_read(properties.extended_status_info)
            properties.instance_flexibility = AAZStrType(
                serialized_name="instanceFlexibility",
            )
            properties.last_updated_date_time = AAZStrType(
                serialized_name="lastUpdatedDateTime",
                flags={"read_only": True},
            )
            properties.merge_properties = AAZObjectType(
                serialized_name="mergeProperties",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.provisioning_sub_state = AAZStrType(
                serialized_name="provisioningSubState",
                flags={"read_only": True},
            )
            properties.purchase_date = AAZStrType(
                serialized_name="purchaseDate",
            )
            properties.purchase_date_time = AAZStrType(
                serialized_name="purchaseDateTime",
            )
            properties.quantity = AAZIntType()
            properties.renew = AAZBoolType()
            properties.renew_destination = AAZStrType(
                serialized_name="renewDestination",
            )
            properties.renew_properties = AAZObjectType(
                serialized_name="renewProperties",
            )
            properties.renew_source = AAZStrType(
                serialized_name="renewSource",
            )
            properties.reserved_resource_type = AAZStrType(
                serialized_name="reservedResourceType",
            )
            properties.review_date_time = AAZStrType(
                serialized_name="reviewDateTime",
            )
            properties.sku_description = AAZStrType(
                serialized_name="skuDescription",
            )
            properties.split_properties = AAZObjectType(
                serialized_name="splitProperties",
            )
            properties.swap_properties = AAZObjectType(
                serialized_name="swapProperties",
            )
            properties.term = AAZStrType()
            properties.user_friendly_applied_scope_type = AAZStrType(
                serialized_name="userFriendlyAppliedScopeType",
                flags={"read_only": True},
            )
            properties.user_friendly_renew_state = AAZStrType(
                serialized_name="userFriendlyRenewState",
                flags={"read_only": True},
            )
            properties.utilization = AAZObjectType(
                flags={"read_only": True},
            )

            merge_properties = cls._schema_on_200.properties.reservations.Element.properties.merge_properties
            merge_properties.merge_destination = AAZStrType(
                serialized_name="mergeDestination",
            )
            merge_properties.merge_sources = AAZListType(
                serialized_name="mergeSources",
            )

            merge_sources = cls._schema_on_200.properties.reservations.Element.properties.merge_properties.merge_sources
            merge_sources.Element = AAZStrType()

            renew_properties = cls._schema_on_200.properties.reservations.Element.properties.renew_properties
            renew_properties.billing_currency_total = AAZObjectType(
                serialized_name="billingCurrencyTotal",
            )
            renew_properties.pricing_currency_total = AAZObjectType(
                serialized_name="pricingCurrencyTotal",
            )
            renew_properties.purchase_properties = AAZObjectType(
                serialized_name="purchaseProperties",
            )

            billing_currency_total = cls._schema_on_200.properties.reservations.Element.properties.renew_properties.billing_currency_total
            billing_currency_total.amount = AAZFloatType()
            billing_currency_total.currency_code = AAZStrType(
                serialized_name="currencyCode",
            )

            pricing_currency_total = cls._schema_on_200.properties.reservations.Element.properties.renew_properties.pricing_currency_total
            pricing_currency_total.amount = AAZFloatType()
            pricing_currency_total.currency_code = AAZStrType(
                serialized_name="currencyCode",
            )

            purchase_properties = cls._schema_on_200.properties.reservations.Element.properties.renew_properties.purchase_properties
            purchase_properties.location = AAZStrType()
            purchase_properties.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            purchase_properties.sku = AAZObjectType()
            _ShowHelper._build_schema_sku_name_read(purchase_properties.sku)

            properties = cls._schema_on_200.properties.reservations.Element.properties.renew_properties.purchase_properties.properties
            properties.applied_scope_properties = AAZObjectType(
                serialized_name="appliedScopeProperties",
            )
            _ShowHelper._build_schema_applied_scope_properties_read(properties.applied_scope_properties)
            properties.applied_scope_type = AAZStrType(
                serialized_name="appliedScopeType",
            )
            properties.applied_scopes = AAZListType(
                serialized_name="appliedScopes",
            )
            _ShowHelper._build_schema_applied_scopes_read(properties.applied_scopes)
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.quantity = AAZIntType()
            properties.renew = AAZBoolType()
            properties.reserved_resource_properties = AAZObjectType(
                serialized_name="reservedResourceProperties",
            )
            properties.reserved_resource_type = AAZStrType(
                serialized_name="reservedResourceType",
            )
            properties.review_date_time = AAZStrType(
                serialized_name="reviewDateTime",
            )
            properties.term = AAZStrType()

            reserved_resource_properties = cls._schema_on_200.properties.reservations.Element.properties.renew_properties.purchase_properties.properties.reserved_resource_properties
            reserved_resource_properties.instance_flexibility = AAZStrType(
                serialized_name="instanceFlexibility",
            )

            split_properties = cls._schema_on_200.properties.reservations.Element.properties.split_properties
            split_properties.split_destinations = AAZListType(
                serialized_name="splitDestinations",
            )
            split_properties.split_source = AAZStrType(
                serialized_name="splitSource",
            )

            split_destinations = cls._schema_on_200.properties.reservations.Element.properties.split_properties.split_destinations
            split_destinations.Element = AAZStrType()

            swap_properties = cls._schema_on_200.properties.reservations.Element.properties.swap_properties
            swap_properties.swap_destination = AAZStrType(
                serialized_name="swapDestination",
            )
            swap_properties.swap_source = AAZStrType(
                serialized_name="swapSource",
            )

            utilization = cls._schema_on_200.properties.reservations.Element.properties.utilization
            utilization.aggregates = AAZListType()
            utilization.trend = AAZStrType(
                flags={"read_only": True},
            )

            aggregates = cls._schema_on_200.properties.reservations.Element.properties.utilization.aggregates
            aggregates.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.reservations.Element.properties.utilization.aggregates.Element
            _element.grain = AAZFloatType(
                flags={"read_only": True},
            )
            _element.grain_unit = AAZStrType(
                serialized_name="grainUnit",
                flags={"read_only": True},
            )
            _element.value = AAZFloatType(
                flags={"read_only": True},
            )
            _element.value_unit = AAZStrType(
                serialized_name="valueUnit",
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_applied_scope_properties_read = None

    @classmethod
    def _build_schema_applied_scope_properties_read(cls, _schema):
        if cls._schema_applied_scope_properties_read is not None:
            _schema.display_name = cls._schema_applied_scope_properties_read.display_name
            _schema.management_group_id = cls._schema_applied_scope_properties_read.management_group_id
            _schema.resource_group_id = cls._schema_applied_scope_properties_read.resource_group_id
            _schema.subscription_id = cls._schema_applied_scope_properties_read.subscription_id
            _schema.tenant_id = cls._schema_applied_scope_properties_read.tenant_id
            return

        cls._schema_applied_scope_properties_read = _schema_applied_scope_properties_read = AAZObjectType()

        applied_scope_properties_read = _schema_applied_scope_properties_read
        applied_scope_properties_read.display_name = AAZStrType(
            serialized_name="displayName",
        )
        applied_scope_properties_read.management_group_id = AAZStrType(
            serialized_name="managementGroupId",
        )
        applied_scope_properties_read.resource_group_id = AAZStrType(
            serialized_name="resourceGroupId",
        )
        applied_scope_properties_read.subscription_id = AAZStrType(
            serialized_name="subscriptionId",
        )
        applied_scope_properties_read.tenant_id = AAZStrType(
            serialized_name="tenantId",
        )

        _schema.display_name = cls._schema_applied_scope_properties_read.display_name
        _schema.management_group_id = cls._schema_applied_scope_properties_read.management_group_id
        _schema.resource_group_id = cls._schema_applied_scope_properties_read.resource_group_id
        _schema.subscription_id = cls._schema_applied_scope_properties_read.subscription_id
        _schema.tenant_id = cls._schema_applied_scope_properties_read.tenant_id

    _schema_applied_scopes_read = None

    @classmethod
    def _build_schema_applied_scopes_read(cls, _schema):
        if cls._schema_applied_scopes_read is not None:
            _schema.Element = cls._schema_applied_scopes_read.Element
            return

        cls._schema_applied_scopes_read = _schema_applied_scopes_read = AAZListType()

        applied_scopes_read = _schema_applied_scopes_read
        applied_scopes_read.Element = AAZStrType()

        _schema.Element = cls._schema_applied_scopes_read.Element

    _schema_extended_status_info_read = None

    @classmethod
    def _build_schema_extended_status_info_read(cls, _schema):
        if cls._schema_extended_status_info_read is not None:
            _schema.message = cls._schema_extended_status_info_read.message
            _schema.status_code = cls._schema_extended_status_info_read.status_code
            return

        cls._schema_extended_status_info_read = _schema_extended_status_info_read = AAZObjectType()

        extended_status_info_read = _schema_extended_status_info_read
        extended_status_info_read.message = AAZStrType()
        extended_status_info_read.status_code = AAZStrType(
            serialized_name="statusCode",
        )

        _schema.message = cls._schema_extended_status_info_read.message
        _schema.status_code = cls._schema_extended_status_info_read.status_code

    _schema_price_read = None

    @classmethod
    def _build_schema_price_read(cls, _schema):
        if cls._schema_price_read is not None:
            _schema.amount = cls._schema_price_read.amount
            _schema.currency_code = cls._schema_price_read.currency_code
            return

        cls._schema_price_read = _schema_price_read = AAZObjectType()

        price_read = _schema_price_read
        price_read.amount = AAZFloatType()
        price_read.currency_code = AAZStrType(
            serialized_name="currencyCode",
        )

        _schema.amount = cls._schema_price_read.amount
        _schema.currency_code = cls._schema_price_read.currency_code

    _schema_sku_name_read = None

    @classmethod
    def _build_schema_sku_name_read(cls, _schema):
        if cls._schema_sku_name_read is not None:
            _schema.name = cls._schema_sku_name_read.name
            return

        cls._schema_sku_name_read = _schema_sku_name_read = AAZObjectType()

        sku_name_read = _schema_sku_name_read
        sku_name_read.name = AAZStrType()

        _schema.name = cls._schema_sku_name_read.name

    _schema_system_data_read = None

    @classmethod
    def _build_schema_system_data_read(cls, _schema):
        if cls._schema_system_data_read is not None:
            _schema.created_at = cls._schema_system_data_read.created_at
            _schema.created_by = cls._schema_system_data_read.created_by
            _schema.created_by_type = cls._schema_system_data_read.created_by_type
            _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
            _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
            _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type
            return

        cls._schema_system_data_read = _schema_system_data_read = AAZObjectType(
            flags={"read_only": True}
        )

        system_data_read = _schema_system_data_read
        system_data_read.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data_read.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data_read.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data_read.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data_read.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data_read.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.created_at = cls._schema_system_data_read.created_at
        _schema.created_by = cls._schema_system_data_read.created_by
        _schema.created_by_type = cls._schema_system_data_read.created_by_type
        _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
        _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
        _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type


__all__ = ["Show"]
