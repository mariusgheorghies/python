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
from kubernetes.client.models.aws_k8s_services_v1alpha1_field_export import AwsK8sServicesV1alpha1FieldExport  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sServicesV1alpha1FieldExport(unittest.TestCase):
    """AwsK8sServicesV1alpha1FieldExport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sServicesV1alpha1FieldExport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_services_v1alpha1_field_export.AwsK8sServicesV1alpha1FieldExport()  # noqa: E501
        if include_optional :
            return AwsK8sServicesV1alpha1FieldExport(
                api_version = '0', 
                kind = '0', 
                metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : '0'
                        }, 
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
                            subresource = '0', 
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
                spec = kubernetes.client.models.aws_k8s_services_v1alpha1_field_export_spec.aws_k8s_services_v1alpha1_FieldExport_spec(
                    from = kubernetes.client.models.aws_k8s_services_v1alpha1_field_export_spec_from.aws_k8s_services_v1alpha1_FieldExport_spec_from(
                        path = '0', 
                        resource = kubernetes.client.models.aws_k8s_services_v1alpha1_field_export_spec_from_resource.aws_k8s_services_v1alpha1_FieldExport_spec_from_resource(
                            group = '0', 
                            kind = '0', 
                            name = '0', ), ), 
                    to = kubernetes.client.models.aws_k8s_services_v1alpha1_field_export_spec_to.aws_k8s_services_v1alpha1_FieldExport_spec_to(
                        key = '0', 
                        kind = 'configmap', 
                        name = '0', 
                        namespace = '0', ), ), 
                status = kubernetes.client.models.aws_k8s_services_v1alpha1_field_export_status.aws_k8s_services_v1alpha1_FieldExport_status(
                    conditions = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_status_conditions.aws_k8s_services_ec2_v1alpha1_DHCPOptions_status_conditions(
                            last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            message = '0', 
                            reason = '0', 
                            status = '0', 
                            type = '0', )
                        ], )
            )
        else :
            return AwsK8sServicesV1alpha1FieldExport(
        )

    def testAwsK8sServicesV1alpha1FieldExport(self):
        """Test AwsK8sServicesV1alpha1FieldExport"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
