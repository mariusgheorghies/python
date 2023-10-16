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
from kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template import IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecTargetTemplate  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecTargetTemplate(unittest.TestCase):
    """IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecTargetTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecTargetTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template.IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecTargetTemplate()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecTargetTemplate(
                data = {
                    'key' : '0'
                    }, 
                engine_version = '0', 
                metadata = kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_target_template_metadata.io_external_secrets_v1alpha1_ExternalSecret_spec_target_template_metadata(
                    annotations = {
                        'key' : '0'
                        }, 
                    labels = {
                        'key' : '0'
                        }, ), 
                template_from = [
                    kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template_template_from.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_target_template_templateFrom(
                        config_map = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template_config_map.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_target_template_configMap(
                            items = [
                                kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template_config_map_items.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_target_template_configMap_items(
                                    key = '0', 
                                    template_as = '0', )
                                ], 
                            name = '0', ), 
                        literal = '0', 
                        secret = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template_config_map.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_target_template_configMap(
                            items = [
                                kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_target_template_config_map_items.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_target_template_configMap_items(
                                    key = '0', 
                                    template_as = '0', )
                                ], 
                            name = '0', ), 
                        target = '0', )
                    ], 
                type = '0'
            )
        else :
            return IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecTargetTemplate(
        )

    def testIoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecTargetTemplate(self):
        """Test IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecTargetTemplate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
