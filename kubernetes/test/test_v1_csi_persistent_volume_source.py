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
from kubernetes.client.models.v1_csi_persistent_volume_source import V1CSIPersistentVolumeSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1CSIPersistentVolumeSource(unittest.TestCase):
    """V1CSIPersistentVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1CSIPersistentVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_csi_persistent_volume_source.V1CSIPersistentVolumeSource()  # noqa: E501
        if include_optional :
            return V1CSIPersistentVolumeSource(
                controller_expand_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '0', 
                    namespace = '0', ), 
                controller_publish_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '0', 
                    namespace = '0', ), 
                driver = '0', 
                fs_type = '0', 
                node_publish_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '0', 
                    namespace = '0', ), 
                node_stage_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '0', 
                    namespace = '0', ), 
                read_only = True, 
                volume_attributes = {
                    'key' : '0'
                    }, 
                volume_handle = '0'
            )
        else :
            return V1CSIPersistentVolumeSource(
                driver = '0',
                volume_handle = '0',
        )

    def testV1CSIPersistentVolumeSource(self):
        """Test V1CSIPersistentVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
