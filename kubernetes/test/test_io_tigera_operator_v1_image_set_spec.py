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
from kubernetes.client.models.io_tigera_operator_v1_image_set_spec import IoTigeraOperatorV1ImageSetSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoTigeraOperatorV1ImageSetSpec(unittest.TestCase):
    """IoTigeraOperatorV1ImageSetSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoTigeraOperatorV1ImageSetSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_tigera_operator_v1_image_set_spec.IoTigeraOperatorV1ImageSetSpec()  # noqa: E501
        if include_optional :
            return IoTigeraOperatorV1ImageSetSpec(
                images = [
                    kubernetes.client.models.io_tigera_operator_v1_image_set_spec_images.io_tigera_operator_v1_ImageSet_spec_images(
                        digest = '0', 
                        image = '0', )
                    ]
            )
        else :
            return IoTigeraOperatorV1ImageSetSpec(
        )

    def testIoTigeraOperatorV1ImageSetSpec(self):
        """Test IoTigeraOperatorV1ImageSetSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()