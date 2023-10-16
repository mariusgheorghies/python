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
from kubernetes.client.models.io_xk8s_hnc_v1alpha2_hnc_configuration_status import IoXK8sHncV1alpha2HNCConfigurationStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sHncV1alpha2HNCConfigurationStatus(unittest.TestCase):
    """IoXK8sHncV1alpha2HNCConfigurationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sHncV1alpha2HNCConfigurationStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_hnc_v1alpha2_hnc_configuration_status.IoXK8sHncV1alpha2HNCConfigurationStatus()  # noqa: E501
        if include_optional :
            return IoXK8sHncV1alpha2HNCConfigurationStatus(
                conditions = [
                    kubernetes.client.models.io_x_k8s_hnc_v1alpha2_hnc_configuration_status_conditions.io_x_k8s_hnc_v1alpha2_HNCConfiguration_status_conditions(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        observed_generation = 0, 
                        reason = 'a', 
                        status = 'True', 
                        type = 'a', )
                    ], 
                resources = [
                    kubernetes.client.models.io_x_k8s_hnc_v1alpha2_hnc_configuration_status_resources.io_x_k8s_hnc_v1alpha2_HNCConfiguration_status_resources(
                        group = '0', 
                        mode = '0', 
                        num_propagated_objects = 0, 
                        num_source_objects = 0, 
                        resource = '0', 
                        version = '0', )
                    ]
            )
        else :
            return IoXK8sHncV1alpha2HNCConfigurationStatus(
        )

    def testIoXK8sHncV1alpha2HNCConfigurationStatus(self):
        """Test IoXK8sHncV1alpha2HNCConfigurationStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()