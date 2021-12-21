# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v2beta1_external_metric_status import V2beta1ExternalMetricStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV2beta1ExternalMetricStatus(unittest.TestCase):
    """V2beta1ExternalMetricStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V2beta1ExternalMetricStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v2beta1_external_metric_status.V2beta1ExternalMetricStatus()  # noqa: E501
        if include_optional :
            return V2beta1ExternalMetricStatus(
                current_average_value = '0', 
                current_value = '0', 
                metric_name = '0', 
                metric_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                    match_expressions = [
                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                            key = '0', 
                            operator = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    match_labels = {
                        'key' : '0'
                        }, )
            )
        else :
            return V2beta1ExternalMetricStatus(
                current_value = '0',
                metric_name = '0',
        )

    def testV2beta1ExternalMetricStatus(self):
        """Test V2beta1ExternalMetricStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
