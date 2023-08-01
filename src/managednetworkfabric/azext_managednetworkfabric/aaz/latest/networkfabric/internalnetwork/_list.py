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
    "networkfabric internalnetwork list",
)
class List(AAZCommand):
    """List all Internal Networks in the provided resource group

    :example: List the Internal Networks for Resource Group
        az networkfabric internalnetwork list --resource-group "example-rg" --l3domain "example-l3domain"
    """

    _aaz_info = {
        "version": "2023-06-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/l3isolationdomains/{}/internalnetworks", "2023-06-15"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.l3_isolation_domain_name = AAZStrArg(
            options=["--l3domain", "--l3-isolation-domain-name"],
            help="Name of the L3 Isolation Domain.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.InternalNetworksListByL3IsolationDomain(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class InternalNetworksListByL3IsolationDomain(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks",
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
                    "l3IsolationDomainName", self.ctx.args.l3_isolation_domain_name,
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
                    "api-version", "2023-06-15",
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            properties.annotation = AAZStrType()
            properties.bgp_configuration = AAZObjectType(
                serialized_name="bgpConfiguration",
            )
            properties.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            properties.connected_i_pv4_subnets = AAZListType(
                serialized_name="connectedIPv4Subnets",
            )
            properties.connected_i_pv6_subnets = AAZListType(
                serialized_name="connectedIPv6Subnets",
            )
            properties.egress_acl_id = AAZStrType(
                serialized_name="egressAclId",
            )
            properties.export_route_policy = AAZObjectType(
                serialized_name="exportRoutePolicy",
            )
            properties.export_route_policy_id = AAZStrType(
                serialized_name="exportRoutePolicyId",
            )
            properties.extension = AAZStrType()
            properties.import_route_policy = AAZObjectType(
                serialized_name="importRoutePolicy",
            )
            properties.import_route_policy_id = AAZStrType(
                serialized_name="importRoutePolicyId",
            )
            properties.ingress_acl_id = AAZStrType(
                serialized_name="ingressAclId",
            )
            properties.is_monitoring_enabled = AAZStrType(
                serialized_name="isMonitoringEnabled",
            )
            properties.mtu = AAZIntType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.static_route_configuration = AAZObjectType(
                serialized_name="staticRouteConfiguration",
            )
            properties.vlan_id = AAZIntType(
                serialized_name="vlanId",
                flags={"required": True},
            )

            bgp_configuration = cls._schema_on_200.value.Element.properties.bgp_configuration
            bgp_configuration.allow_as = AAZIntType(
                serialized_name="allowAS",
            )
            bgp_configuration.allow_as_override = AAZStrType(
                serialized_name="allowASOverride",
            )
            bgp_configuration.annotation = AAZStrType()
            bgp_configuration.bfd_configuration = AAZObjectType(
                serialized_name="bfdConfiguration",
            )
            _ListHelper._build_schema_bfd_configuration_read(bgp_configuration.bfd_configuration)
            bgp_configuration.default_route_originate = AAZStrType(
                serialized_name="defaultRouteOriginate",
            )
            bgp_configuration.fabric_asn = AAZIntType(
                serialized_name="fabricASN",
                flags={"read_only": True},
            )
            bgp_configuration.ipv4_listen_range_prefixes = AAZListType(
                serialized_name="ipv4ListenRangePrefixes",
            )
            bgp_configuration.ipv4_neighbor_address = AAZListType(
                serialized_name="ipv4NeighborAddress",
            )
            bgp_configuration.ipv6_listen_range_prefixes = AAZListType(
                serialized_name="ipv6ListenRangePrefixes",
            )
            bgp_configuration.ipv6_neighbor_address = AAZListType(
                serialized_name="ipv6NeighborAddress",
            )
            bgp_configuration.peer_asn = AAZIntType(
                serialized_name="peerASN",
                flags={"required": True},
            )

            ipv4_listen_range_prefixes = cls._schema_on_200.value.Element.properties.bgp_configuration.ipv4_listen_range_prefixes
            ipv4_listen_range_prefixes.Element = AAZStrType()

            ipv4_neighbor_address = cls._schema_on_200.value.Element.properties.bgp_configuration.ipv4_neighbor_address
            ipv4_neighbor_address.Element = AAZObjectType()
            _ListHelper._build_schema_neighbor_address_read(ipv4_neighbor_address.Element)

            ipv6_listen_range_prefixes = cls._schema_on_200.value.Element.properties.bgp_configuration.ipv6_listen_range_prefixes
            ipv6_listen_range_prefixes.Element = AAZStrType()

            ipv6_neighbor_address = cls._schema_on_200.value.Element.properties.bgp_configuration.ipv6_neighbor_address
            ipv6_neighbor_address.Element = AAZObjectType()
            _ListHelper._build_schema_neighbor_address_read(ipv6_neighbor_address.Element)

            connected_i_pv4_subnets = cls._schema_on_200.value.Element.properties.connected_i_pv4_subnets
            connected_i_pv4_subnets.Element = AAZObjectType()
            _ListHelper._build_schema_connected_subnet_read(connected_i_pv4_subnets.Element)

            connected_i_pv6_subnets = cls._schema_on_200.value.Element.properties.connected_i_pv6_subnets
            connected_i_pv6_subnets.Element = AAZObjectType()
            _ListHelper._build_schema_connected_subnet_read(connected_i_pv6_subnets.Element)

            export_route_policy = cls._schema_on_200.value.Element.properties.export_route_policy
            export_route_policy.export_ipv4_route_policy_id = AAZStrType(
                serialized_name="exportIpv4RoutePolicyId",
            )
            export_route_policy.export_ipv6_route_policy_id = AAZStrType(
                serialized_name="exportIpv6RoutePolicyId",
            )

            import_route_policy = cls._schema_on_200.value.Element.properties.import_route_policy
            import_route_policy.import_ipv4_route_policy_id = AAZStrType(
                serialized_name="importIpv4RoutePolicyId",
            )
            import_route_policy.import_ipv6_route_policy_id = AAZStrType(
                serialized_name="importIpv6RoutePolicyId",
            )

            static_route_configuration = cls._schema_on_200.value.Element.properties.static_route_configuration
            static_route_configuration.bfd_configuration = AAZObjectType(
                serialized_name="bfdConfiguration",
            )
            _ListHelper._build_schema_bfd_configuration_read(static_route_configuration.bfd_configuration)
            static_route_configuration.extension = AAZStrType()
            static_route_configuration.ipv4_routes = AAZListType(
                serialized_name="ipv4Routes",
            )
            static_route_configuration.ipv6_routes = AAZListType(
                serialized_name="ipv6Routes",
            )

            ipv4_routes = cls._schema_on_200.value.Element.properties.static_route_configuration.ipv4_routes
            ipv4_routes.Element = AAZObjectType()
            _ListHelper._build_schema_static_route_properties_read(ipv4_routes.Element)

            ipv6_routes = cls._schema_on_200.value.Element.properties.static_route_configuration.ipv6_routes
            ipv6_routes.Element = AAZObjectType()
            _ListHelper._build_schema_static_route_properties_read(ipv6_routes.Element)

            system_data = cls._schema_on_200.value.Element.system_data
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


class _ListHelper:
    """Helper class for List"""

    _schema_bfd_configuration_read = None

    @classmethod
    def _build_schema_bfd_configuration_read(cls, _schema):
        if cls._schema_bfd_configuration_read is not None:
            _schema.administrative_state = cls._schema_bfd_configuration_read.administrative_state
            _schema.interval_in_milli_seconds = cls._schema_bfd_configuration_read.interval_in_milli_seconds
            _schema.multiplier = cls._schema_bfd_configuration_read.multiplier
            return

        cls._schema_bfd_configuration_read = _schema_bfd_configuration_read = AAZObjectType()

        bfd_configuration_read = _schema_bfd_configuration_read
        bfd_configuration_read.administrative_state = AAZStrType(
            serialized_name="administrativeState",
            flags={"read_only": True},
        )
        bfd_configuration_read.interval_in_milli_seconds = AAZIntType(
            serialized_name="intervalInMilliSeconds",
        )
        bfd_configuration_read.multiplier = AAZIntType()

        _schema.administrative_state = cls._schema_bfd_configuration_read.administrative_state
        _schema.interval_in_milli_seconds = cls._schema_bfd_configuration_read.interval_in_milli_seconds
        _schema.multiplier = cls._schema_bfd_configuration_read.multiplier

    _schema_connected_subnet_read = None

    @classmethod
    def _build_schema_connected_subnet_read(cls, _schema):
        if cls._schema_connected_subnet_read is not None:
            _schema.annotation = cls._schema_connected_subnet_read.annotation
            _schema.prefix = cls._schema_connected_subnet_read.prefix
            return

        cls._schema_connected_subnet_read = _schema_connected_subnet_read = AAZObjectType()

        connected_subnet_read = _schema_connected_subnet_read
        connected_subnet_read.annotation = AAZStrType()
        connected_subnet_read.prefix = AAZStrType(
            flags={"required": True},
        )

        _schema.annotation = cls._schema_connected_subnet_read.annotation
        _schema.prefix = cls._schema_connected_subnet_read.prefix

    _schema_neighbor_address_read = None

    @classmethod
    def _build_schema_neighbor_address_read(cls, _schema):
        if cls._schema_neighbor_address_read is not None:
            _schema.address = cls._schema_neighbor_address_read.address
            _schema.configuration_state = cls._schema_neighbor_address_read.configuration_state
            return

        cls._schema_neighbor_address_read = _schema_neighbor_address_read = AAZObjectType()

        neighbor_address_read = _schema_neighbor_address_read
        neighbor_address_read.address = AAZStrType()
        neighbor_address_read.configuration_state = AAZStrType(
            serialized_name="configurationState",
            flags={"read_only": True},
        )

        _schema.address = cls._schema_neighbor_address_read.address
        _schema.configuration_state = cls._schema_neighbor_address_read.configuration_state

    _schema_static_route_properties_read = None

    @classmethod
    def _build_schema_static_route_properties_read(cls, _schema):
        if cls._schema_static_route_properties_read is not None:
            _schema.next_hop = cls._schema_static_route_properties_read.next_hop
            _schema.prefix = cls._schema_static_route_properties_read.prefix
            return

        cls._schema_static_route_properties_read = _schema_static_route_properties_read = AAZObjectType()

        static_route_properties_read = _schema_static_route_properties_read
        static_route_properties_read.next_hop = AAZListType(
            serialized_name="nextHop",
            flags={"required": True},
        )
        static_route_properties_read.prefix = AAZStrType(
            flags={"required": True},
        )

        next_hop = _schema_static_route_properties_read.next_hop
        next_hop.Element = AAZStrType()

        _schema.next_hop = cls._schema_static_route_properties_read.next_hop
        _schema.prefix = cls._schema_static_route_properties_read.prefix


__all__ = ["List"]
