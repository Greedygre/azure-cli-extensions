# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
from unittest import mock
import time
import requests

from azure.cli.testsdk.reverse_dependency import get_dummy_cli
from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, JMESPathCheck, live_only)
from knack.util import CLIError


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@live_only()
class ContainerAppUpImageTest(ScenarioTest):
    @ResourceGroupPreparer(location="eastus2")
    def test_containerapp_up_image_e2e(self, resource_group):
        env_name = self.create_random_name(prefix='env', length=24)
        self.cmd(f'containerapp env create -g {resource_group} -n {env_name}')
        image = "mcr.microsoft.com/azuredocs/containerapps-helloworld:latest"
        app_name = self.create_random_name(prefix='containerapp', length=24)
        self.cmd(f"containerapp up --image {image} --environment {env_name} -g {resource_group} -n {app_name}")

        app = self.cmd(f"containerapp show -g {resource_group} -n {app_name}").get_output_in_json()
        url = app["properties"]["configuration"]["ingress"]["fqdn"]
        url = url if url.startswith("http") else f"http://{url}"
        resp = requests.get(url)
        self.assertTrue(resp.ok)


    @ResourceGroupPreparer(location="eastus", random_name_length=15)
    def test_containerapp_up_on_arc_image_e2e(self, resource_group):
        aks_name = "my-aks-cluster"
        connected_cluster_name = "my-connected-cluster"
        self.cmd(f'aks create --resource-group {resource_group} --name {aks_name} --enable-aad --generate-ssh-keys')
        self.cmd(f'aks get-credentials --resource-group {resource_group} --name {aks_name} --overwrite-existing --admin')
        self.cmd(f'connectedk8s connect --resource-group {resource_group} --name {connected_cluster_name}')
        connected_cluster = self.cmd(f'az connectedk8s show --resource-group {resource_group} --name {connected_cluster_name}').get_output_in_json()
        connected_cluster_id = connected_cluster['id']
        app_name = 'mycontainerapp'
        app_rg = 'my-containerapp-rg'
        image = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'

        self.cmd(f'containerapp up -n {app_name} -g {app_rg} --connected-cluster-id {connected_cluster_id} --image {image}')

        extension_type = 'microsoft.app.environment'
        installed_exts = self.cmd(f'k8s-extension list -c {connected_cluster_name} -g {resource_group} --cluster-type connectedClusters').get_output_in_json()
        found_extension = False
        for item in installed_exts:
            if item['extensionType'] == extension_type:
                found_extension = True
                break
        self.assertTrue(found_extension)
        self.cmd(f'group delete --name {app_rg} --yes --no-wait')