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
    "networkfabric fabric show",
)
class Show(AAZCommand):
    """Show details of the provided Network Fabric resource

    :example: Show the Network Fabric
        az networkfabric fabric show --resource-group "example-rg" --resource-name "example-fabric"
    """

    _aaz_info = {
        "version": "2023-06-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/networkfabrics/{}", "2023-06-15"],
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
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Name of the Network Fabric.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NetworkFabricsGet(ctx=self.ctx)()
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

    class NetworkFabricsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}",
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
                    "networkFabricName", self.ctx.args.resource_name,
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            properties.annotation = AAZStrType()
            properties.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            properties.fabric_asn = AAZIntType(
                serialized_name="fabricASN",
                flags={"required": True},
            )
            properties.fabric_version = AAZStrType(
                serialized_name="fabricVersion",
                flags={"read_only": True},
            )
            properties.ipv4_prefix = AAZStrType(
                serialized_name="ipv4Prefix",
                flags={"required": True},
            )
            properties.ipv6_prefix = AAZStrType(
                serialized_name="ipv6Prefix",
            )
            properties.l2_isolation_domains = AAZListType(
                serialized_name="l2IsolationDomains",
                flags={"read_only": True},
            )
            properties.l3_isolation_domains = AAZListType(
                serialized_name="l3IsolationDomains",
                flags={"read_only": True},
            )
            properties.management_network_configuration = AAZObjectType(
                serialized_name="managementNetworkConfiguration",
                flags={"required": True},
            )
            properties.network_fabric_controller_id = AAZStrType(
                serialized_name="networkFabricControllerId",
                flags={"required": True},
            )
            properties.network_fabric_sku = AAZStrType(
                serialized_name="networkFabricSku",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rack_count = AAZIntType(
                serialized_name="rackCount",
            )
            properties.racks = AAZListType(
                flags={"read_only": True},
            )
            properties.router_ids = AAZListType(
                serialized_name="routerIds",
                flags={"read_only": True},
            )
            properties.server_count_per_rack = AAZIntType(
                serialized_name="serverCountPerRack",
                flags={"required": True},
            )
            properties.terminal_server_configuration = AAZObjectType(
                serialized_name="terminalServerConfiguration",
                flags={"required": True},
            )

            l2_isolation_domains = cls._schema_on_200.properties.l2_isolation_domains
            l2_isolation_domains.Element = AAZStrType()

            l3_isolation_domains = cls._schema_on_200.properties.l3_isolation_domains
            l3_isolation_domains.Element = AAZStrType()

            management_network_configuration = cls._schema_on_200.properties.management_network_configuration
            management_network_configuration.infrastructure_vpn_configuration = AAZObjectType(
                serialized_name="infrastructureVpnConfiguration",
                flags={"required": True},
            )
            _ShowHelper._build_schema_vpn_configuration_properties_read(management_network_configuration.infrastructure_vpn_configuration)
            management_network_configuration.workload_vpn_configuration = AAZObjectType(
                serialized_name="workloadVpnConfiguration",
                flags={"required": True},
            )
            _ShowHelper._build_schema_vpn_configuration_properties_read(management_network_configuration.workload_vpn_configuration)

            racks = cls._schema_on_200.properties.racks
            racks.Element = AAZStrType()

            router_ids = cls._schema_on_200.properties.router_ids
            router_ids.Element = AAZStrType()

            terminal_server_configuration = cls._schema_on_200.properties.terminal_server_configuration
            terminal_server_configuration.network_device_id = AAZStrType(
                serialized_name="networkDeviceId",
                flags={"read_only": True},
            )
            terminal_server_configuration.password = AAZStrType(
                flags={"required": True, "secret": True},
            )
            terminal_server_configuration.primary_ipv4_prefix = AAZStrType(
                serialized_name="primaryIpv4Prefix",
                flags={"required": True},
            )
            terminal_server_configuration.primary_ipv6_prefix = AAZStrType(
                serialized_name="primaryIpv6Prefix",
            )
            terminal_server_configuration.secondary_ipv4_prefix = AAZStrType(
                serialized_name="secondaryIpv4Prefix",
                flags={"required": True},
            )
            terminal_server_configuration.secondary_ipv6_prefix = AAZStrType(
                serialized_name="secondaryIpv6Prefix",
            )
            terminal_server_configuration.serial_number = AAZStrType(
                serialized_name="serialNumber",
            )
            terminal_server_configuration.username = AAZStrType(
                flags={"required": True},
            )

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

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_vpn_configuration_properties_read = None

    @classmethod
    def _build_schema_vpn_configuration_properties_read(cls, _schema):
        if cls._schema_vpn_configuration_properties_read is not None:
            _schema.administrative_state = cls._schema_vpn_configuration_properties_read.administrative_state
            _schema.network_to_network_interconnect_id = cls._schema_vpn_configuration_properties_read.network_to_network_interconnect_id
            _schema.option_a_properties = cls._schema_vpn_configuration_properties_read.option_a_properties
            _schema.option_b_properties = cls._schema_vpn_configuration_properties_read.option_b_properties
            _schema.peering_option = cls._schema_vpn_configuration_properties_read.peering_option
            return

        cls._schema_vpn_configuration_properties_read = _schema_vpn_configuration_properties_read = AAZObjectType()

        vpn_configuration_properties_read = _schema_vpn_configuration_properties_read
        vpn_configuration_properties_read.administrative_state = AAZStrType(
            serialized_name="administrativeState",
            flags={"read_only": True},
        )
        vpn_configuration_properties_read.network_to_network_interconnect_id = AAZStrType(
            serialized_name="networkToNetworkInterconnectId",
        )
        vpn_configuration_properties_read.option_a_properties = AAZObjectType(
            serialized_name="optionAProperties",
        )
        vpn_configuration_properties_read.option_b_properties = AAZObjectType(
            serialized_name="optionBProperties",
        )
        vpn_configuration_properties_read.peering_option = AAZStrType(
            serialized_name="peeringOption",
            flags={"required": True},
        )

        option_a_properties = _schema_vpn_configuration_properties_read.option_a_properties
        option_a_properties.bfd_configuration = AAZObjectType(
            serialized_name="bfdConfiguration",
        )
        option_a_properties.mtu = AAZIntType()
        option_a_properties.peer_asn = AAZIntType(
            serialized_name="peerASN",
            flags={"required": True},
        )
        option_a_properties.primary_ipv4_prefix = AAZStrType(
            serialized_name="primaryIpv4Prefix",
        )
        option_a_properties.primary_ipv6_prefix = AAZStrType(
            serialized_name="primaryIpv6Prefix",
        )
        option_a_properties.secondary_ipv4_prefix = AAZStrType(
            serialized_name="secondaryIpv4Prefix",
        )
        option_a_properties.secondary_ipv6_prefix = AAZStrType(
            serialized_name="secondaryIpv6Prefix",
        )
        option_a_properties.vlan_id = AAZIntType(
            serialized_name="vlanId",
            flags={"required": True},
        )

        bfd_configuration = _schema_vpn_configuration_properties_read.option_a_properties.bfd_configuration
        bfd_configuration.administrative_state = AAZStrType(
            serialized_name="administrativeState",
            flags={"read_only": True},
        )
        bfd_configuration.interval_in_milli_seconds = AAZIntType(
            serialized_name="intervalInMilliSeconds",
        )
        bfd_configuration.multiplier = AAZIntType()

        option_b_properties = _schema_vpn_configuration_properties_read.option_b_properties
        option_b_properties.export_route_targets = AAZListType(
            serialized_name="exportRouteTargets",
        )
        option_b_properties.import_route_targets = AAZListType(
            serialized_name="importRouteTargets",
        )
        option_b_properties.route_targets = AAZObjectType(
            serialized_name="routeTargets",
        )

        export_route_targets = _schema_vpn_configuration_properties_read.option_b_properties.export_route_targets
        export_route_targets.Element = AAZStrType()

        import_route_targets = _schema_vpn_configuration_properties_read.option_b_properties.import_route_targets
        import_route_targets.Element = AAZStrType()

        route_targets = _schema_vpn_configuration_properties_read.option_b_properties.route_targets
        route_targets.export_ipv4_route_targets = AAZListType(
            serialized_name="exportIpv4RouteTargets",
        )
        route_targets.export_ipv6_route_targets = AAZListType(
            serialized_name="exportIpv6RouteTargets",
        )
        route_targets.import_ipv4_route_targets = AAZListType(
            serialized_name="importIpv4RouteTargets",
        )
        route_targets.import_ipv6_route_targets = AAZListType(
            serialized_name="importIpv6RouteTargets",
        )

        export_ipv4_route_targets = _schema_vpn_configuration_properties_read.option_b_properties.route_targets.export_ipv4_route_targets
        export_ipv4_route_targets.Element = AAZStrType()

        export_ipv6_route_targets = _schema_vpn_configuration_properties_read.option_b_properties.route_targets.export_ipv6_route_targets
        export_ipv6_route_targets.Element = AAZStrType()

        import_ipv4_route_targets = _schema_vpn_configuration_properties_read.option_b_properties.route_targets.import_ipv4_route_targets
        import_ipv4_route_targets.Element = AAZStrType()

        import_ipv6_route_targets = _schema_vpn_configuration_properties_read.option_b_properties.route_targets.import_ipv6_route_targets
        import_ipv6_route_targets.Element = AAZStrType()

        _schema.administrative_state = cls._schema_vpn_configuration_properties_read.administrative_state
        _schema.network_to_network_interconnect_id = cls._schema_vpn_configuration_properties_read.network_to_network_interconnect_id
        _schema.option_a_properties = cls._schema_vpn_configuration_properties_read.option_a_properties
        _schema.option_b_properties = cls._schema_vpn_configuration_properties_read.option_b_properties
        _schema.peering_option = cls._schema_vpn_configuration_properties_read.peering_option


__all__ = ["Show"]
