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
from kubernetes.client.models.aws_k8s_services_v1alpha1_field_export_spec_from import AwsK8sServicesV1alpha1FieldExportSpecFrom  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sServicesV1alpha1FieldExportSpecFrom(unittest.TestCase):
    """AwsK8sServicesV1alpha1FieldExportSpecFrom unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sServicesV1alpha1FieldExportSpecFrom
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_services_v1alpha1_field_export_spec_from.AwsK8sServicesV1alpha1FieldExportSpecFrom()  # noqa: E501
        if include_optional :
            return AwsK8sServicesV1alpha1FieldExportSpecFrom(
                path = '0', 
                resource = kubernetes.client.models.aws_k8s_services_v1alpha1_field_export_spec_from_resource.aws_k8s_services_v1alpha1_FieldExport_spec_from_resource(
                    group = '0', 
                    kind = '0', 
                    name = '0', )
            )
        else :
            return AwsK8sServicesV1alpha1FieldExportSpecFrom(
                path = '0',
                resource = kubernetes.client.models.aws_k8s_services_v1alpha1_field_export_spec_from_resource.aws_k8s_services_v1alpha1_FieldExport_spec_from_resource(
                    group = '0', 
                    kind = '0', 
                    name = '0', ),
        )

    def testAwsK8sServicesV1alpha1FieldExportSpecFrom(self):
        """Test AwsK8sServicesV1alpha1FieldExportSpecFrom"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
