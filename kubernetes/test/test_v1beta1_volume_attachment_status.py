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
from kubernetes.client.models.v1beta1_volume_attachment_status import V1beta1VolumeAttachmentStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1VolumeAttachmentStatus(unittest.TestCase):
    """V1beta1VolumeAttachmentStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1VolumeAttachmentStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_volume_attachment_status.V1beta1VolumeAttachmentStatus()  # noqa: E501
        if include_optional :
            return V1beta1VolumeAttachmentStatus(
                attach_error = kubernetes.client.models.v1beta1/volume_error.v1beta1.VolumeError(
                    message = '0', 
                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                attached = True, 
                attachment_metadata = {
                    'key' : '0'
                    }, 
                detach_error = kubernetes.client.models.v1beta1/volume_error.v1beta1.VolumeError(
                    message = '0', 
                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else :
            return V1beta1VolumeAttachmentStatus(
                attached = True,
        )

    def testV1beta1VolumeAttachmentStatus(self):
        """Test V1beta1VolumeAttachmentStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
