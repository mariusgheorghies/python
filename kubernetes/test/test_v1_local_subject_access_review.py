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
from kubernetes.client.models.v1_local_subject_access_review import V1LocalSubjectAccessReview  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1LocalSubjectAccessReview(unittest.TestCase):
    """V1LocalSubjectAccessReview unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1LocalSubjectAccessReview
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_local_subject_access_review.V1LocalSubjectAccessReview()  # noqa: E501
        if include_optional :
            return V1LocalSubjectAccessReview(
                api_version = '0', 
                kind = '0', 
                metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : '0'
                        }, 
                    cluster_name = '0', 
                    creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletion_grace_period_seconds = 56, 
                    deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finalizers = [
                        '0'
                        ], 
                    generate_name = '0', 
                    generation = 56, 
                    labels = {
                        'key' : '0'
                        }, 
                    managed_fields = [
                        kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                            api_version = '0', 
                            fields_type = '0', 
                            fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                            manager = '0', 
                            operation = '0', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    name = '0', 
                    namespace = '0', 
                    owner_references = [
                        kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                            api_version = '0', 
                            block_owner_deletion = True, 
                            controller = True, 
                            kind = '0', 
                            name = '0', 
                            uid = '0', )
                        ], 
                    resource_version = '0', 
                    self_link = '0', 
                    uid = '0', ), 
                spec = kubernetes.client.models.v1/subject_access_review_spec.v1.SubjectAccessReviewSpec(
                    extra = {
                        'key' : [
                            '0'
                            ]
                        }, 
                    groups = [
                        '0'
                        ], 
                    non_resource_attributes = kubernetes.client.models.v1/non_resource_attributes.v1.NonResourceAttributes(
                        path = '0', 
                        verb = '0', ), 
                    resource_attributes = kubernetes.client.models.v1/resource_attributes.v1.ResourceAttributes(
                        group = '0', 
                        name = '0', 
                        namespace = '0', 
                        resource = '0', 
                        subresource = '0', 
                        verb = '0', 
                        version = '0', ), 
                    uid = '0', 
                    user = '0', ), 
                status = kubernetes.client.models.v1/subject_access_review_status.v1.SubjectAccessReviewStatus(
                    allowed = True, 
                    denied = True, 
                    evaluation_error = '0', 
                    reason = '0', )
            )
        else :
            return V1LocalSubjectAccessReview(
                spec = kubernetes.client.models.v1/subject_access_review_spec.v1.SubjectAccessReviewSpec(
                    extra = {
                        'key' : [
                            '0'
                            ]
                        }, 
                    groups = [
                        '0'
                        ], 
                    non_resource_attributes = kubernetes.client.models.v1/non_resource_attributes.v1.NonResourceAttributes(
                        path = '0', 
                        verb = '0', ), 
                    resource_attributes = kubernetes.client.models.v1/resource_attributes.v1.ResourceAttributes(
                        group = '0', 
                        name = '0', 
                        namespace = '0', 
                        resource = '0', 
                        subresource = '0', 
                        verb = '0', 
                        version = '0', ), 
                    uid = '0', 
                    user = '0', ),
        )

    def testV1LocalSubjectAccessReview(self):
        """Test V1LocalSubjectAccessReview"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
