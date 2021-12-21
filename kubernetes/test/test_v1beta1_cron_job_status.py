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
from kubernetes.client.models.v1beta1_cron_job_status import V1beta1CronJobStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1CronJobStatus(unittest.TestCase):
    """V1beta1CronJobStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1CronJobStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_cron_job_status.V1beta1CronJobStatus()  # noqa: E501
        if include_optional :
            return V1beta1CronJobStatus(
                active = [
                    kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                        api_version = '0', 
                        field_path = '0', 
                        kind = '0', 
                        name = '0', 
                        namespace = '0', 
                        resource_version = '0', 
                        uid = '0', )
                    ], 
                last_schedule_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return V1beta1CronJobStatus(
        )

    def testV1beta1CronJobStatus(self):
        """Test V1beta1CronJobStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
