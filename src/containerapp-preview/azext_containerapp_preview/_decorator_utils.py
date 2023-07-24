# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azure.cli.core.commands.client_factory import get_subscription_id

from ._constants import CONTAINER_APPS_RP
from ._client_factory import providers_client_factory


def list_resource_locations(cli_ctx, resource_type):
    providers_client = providers_client_factory(cli_ctx, get_subscription_id(cli_ctx))
    resource_types = getattr(providers_client.get(CONTAINER_APPS_RP), 'resource_types', [])
    res_locations = []
    for res in resource_types:
        if res and getattr(res, 'resource_type', "") == resource_type:
            res_locations = getattr(res, 'locations', [])

    res_locations = [res_loc.lower().replace(" ", "").replace("(", "").replace(")", "") for res_loc in res_locations if
                     res_loc.strip()]

    return res_locations

