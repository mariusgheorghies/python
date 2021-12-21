# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1_scale_io_persistent_volume_source import V1ScaleIOPersistentVolumeSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1ScaleIOPersistentVolumeSource(unittest.TestCase):
    """V1ScaleIOPersistentVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ScaleIOPersistentVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_scale_io_persistent_volume_source.V1ScaleIOPersistentVolumeSource()  # noqa: E501
        if include_optional :
            return V1ScaleIOPersistentVolumeSource(
                fs_type = '0', 
                gateway = '0', 
                protection_domain = '0', 
                read_only = True, 
                secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '0', 
                    namespace = '0', ), 
                ssl_enabled = True, 
                storage_mode = '0', 
                storage_pool = '0', 
                system = '0', 
                volume_name = '0'
            )
        else :
            return V1ScaleIOPersistentVolumeSource(
                gateway = '0',
                secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '0', 
                    namespace = '0', ),
                system = '0',
        )

    def testV1ScaleIOPersistentVolumeSource(self):
        """Test V1ScaleIOPersistentVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
