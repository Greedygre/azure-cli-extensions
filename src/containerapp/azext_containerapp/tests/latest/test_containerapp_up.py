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


    def test_containerapp_up_on_arc_image_e2e(self):
        self.kwargs.update({
            'name': 'mycontainerapp',
            'rg': 'quickup10',
            'cluster_name': 'quickup10-cluster',
            'cluster_type': 'connectedClusters',
            'connected_cluster_id': '/subscriptions/23f95f0e-e782-47be-9f97-56035ec10e42/resourceGroups/quickup10/providers/Microsoft.Kubernetes/connectedClusters/quickup10-cluster',
            'image': 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
        })

        self.cmd('containerapp up -n {name} --connected-cluster-id {connected_cluster_id} --image {image}')

        extension_type = 'microsoft.app.environment'
        installed_exts = self.cmd(
            'k8s-extension list -c {cluster_name} -g {rg} --cluster-type {cluster_type}').get_output_in_json()
        found_extension = False
        for item in installed_exts:
            if item['extensionType'] == extension_type:
                found_extension = True
                break
        self.assertTrue(found_extension)