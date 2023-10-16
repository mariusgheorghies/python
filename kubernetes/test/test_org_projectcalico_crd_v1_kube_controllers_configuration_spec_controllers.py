# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.25.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.org_projectcalico_crd_v1_kube_controllers_configuration_spec_controllers import OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers  # noqa: E501
from kubernetes.client.rest import ApiException

class TestOrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers(unittest.TestCase):
    """OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.org_projectcalico_crd_v1_kube_controllers_configuration_spec_controllers.OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers()  # noqa: E501
        if include_optional :
            return OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers(
                namespace = kubernetes.client.models.org_projectcalico_crd_v1_kube_controllers_configuration_spec_controllers_namespace.org_projectcalico_crd_v1_KubeControllersConfiguration_spec_controllers_namespace(
                    reconciler_period = '0', ), 
                node = kubernetes.client.models.org_projectcalico_crd_v1_kube_controllers_configuration_spec_controllers_node.org_projectcalico_crd_v1_KubeControllersConfiguration_spec_controllers_node(
                    host_endpoint = kubernetes.client.models.org_projectcalico_crd_v1_kube_controllers_configuration_spec_controllers_node_host_endpoint.org_projectcalico_crd_v1_KubeControllersConfiguration_spec_controllers_node_hostEndpoint(
                        auto_create = '0', ), 
                    reconciler_period = '0', 
                    sync_labels = '0', ), 
                policy = kubernetes.client.models.org_projectcalico_crd_v1_kube_controllers_configuration_spec_controllers_policy.org_projectcalico_crd_v1_KubeControllersConfiguration_spec_controllers_policy(
                    reconciler_period = '0', ), 
                service_account = kubernetes.client.models.org_projectcalico_crd_v1_kube_controllers_configuration_spec_controllers_service_account.org_projectcalico_crd_v1_KubeControllersConfiguration_spec_controllers_serviceAccount(
                    reconciler_period = '0', ), 
                workload_endpoint = kubernetes.client.models.org_projectcalico_crd_v1_kube_controllers_configuration_spec_controllers_workload_endpoint.org_projectcalico_crd_v1_KubeControllersConfiguration_spec_controllers_workloadEndpoint(
                    reconciler_period = '0', )
            )
        else :
            return OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers(
        )

    def testOrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers(self):
        """Test OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()