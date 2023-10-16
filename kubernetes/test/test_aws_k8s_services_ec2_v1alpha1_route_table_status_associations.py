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
from kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status_associations import AwsK8sServicesEc2V1alpha1RouteTableStatusAssociations  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sServicesEc2V1alpha1RouteTableStatusAssociations(unittest.TestCase):
    """AwsK8sServicesEc2V1alpha1RouteTableStatusAssociations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sServicesEc2V1alpha1RouteTableStatusAssociations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status_associations.AwsK8sServicesEc2V1alpha1RouteTableStatusAssociations()  # noqa: E501
        if include_optional :
            return AwsK8sServicesEc2V1alpha1RouteTableStatusAssociations(
                association_state = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status_association_state.aws_k8s_services_ec2_v1alpha1_RouteTable_status_associationState(
                    state = '0', 
                    status_message = '0', ), 
                gateway_id = '0', 
                main = True, 
                route_table_association_id = '0', 
                route_table_id = '0', 
                subnet_id = '0'
            )
        else :
            return AwsK8sServicesEc2V1alpha1RouteTableStatusAssociations(
        )

    def testAwsK8sServicesEc2V1alpha1RouteTableStatusAssociations(self):
        """Test AwsK8sServicesEc2V1alpha1RouteTableStatusAssociations"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()