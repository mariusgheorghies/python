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
from kubernetes.client.models.io_argoproj_v1alpha1_application_set_status_application_status import IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoArgoprojV1alpha1ApplicationSetStatusApplicationStatus(unittest.TestCase):
    """IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_argoproj_v1alpha1_application_set_status_application_status.IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus()  # noqa: E501
        if include_optional :
            return IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus(
                application = '0', 
                last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                message = '0', 
                status = '0', 
                step = '0'
            )
        else :
            return IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus(
                application = '0',
                message = '0',
                status = '0',
                step = '0',
        )

    def testIoArgoprojV1alpha1ApplicationSetStatusApplicationStatus(self):
        """Test IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
