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
from kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_status_elastic_inference_accelerator_associations import AwsK8sServicesEc2V1alpha1InstanceStatusElasticInferenceAcceleratorAssociations  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sServicesEc2V1alpha1InstanceStatusElasticInferenceAcceleratorAssociations(unittest.TestCase):
    """AwsK8sServicesEc2V1alpha1InstanceStatusElasticInferenceAcceleratorAssociations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sServicesEc2V1alpha1InstanceStatusElasticInferenceAcceleratorAssociations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_status_elastic_inference_accelerator_associations.AwsK8sServicesEc2V1alpha1InstanceStatusElasticInferenceAcceleratorAssociations()  # noqa: E501
        if include_optional :
            return AwsK8sServicesEc2V1alpha1InstanceStatusElasticInferenceAcceleratorAssociations(
                elastic_inference_accelerator_arn = '0', 
                elastic_inference_accelerator_association_id = '0', 
                elastic_inference_accelerator_association_state = '0', 
                elastic_inference_accelerator_association_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return AwsK8sServicesEc2V1alpha1InstanceStatusElasticInferenceAcceleratorAssociations(
        )

    def testAwsK8sServicesEc2V1alpha1InstanceStatusElasticInferenceAcceleratorAssociations(self):
        """Test AwsK8sServicesEc2V1alpha1InstanceStatusElasticInferenceAcceleratorAssociations"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
