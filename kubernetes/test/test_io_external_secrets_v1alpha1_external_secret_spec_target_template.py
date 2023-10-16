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
from kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_target_template import IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplate  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplate(unittest.TestCase):
    """IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_target_template.IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplate()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplate(
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
                    kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_target_template_template_from.io_external_secrets_v1alpha1_ExternalSecret_spec_target_template_templateFrom(
                        config_map = kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_target_template_config_map.io_external_secrets_v1alpha1_ExternalSecret_spec_target_template_configMap(
                            items = [
                                kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_target_template_config_map_items.io_external_secrets_v1alpha1_ExternalSecret_spec_target_template_configMap_items(
                                    key = '0', )
                                ], 
                            name = '0', ), 
                        secret = kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_target_template_config_map.io_external_secrets_v1alpha1_ExternalSecret_spec_target_template_configMap(
                            items = [
                                kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_target_template_config_map_items.io_external_secrets_v1alpha1_ExternalSecret_spec_target_template_configMap_items(
                                    key = '0', )
                                ], 
                            name = '0', ), )
                    ], 
                type = '0'
            )
        else :
            return IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplate(
        )

    def testIoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplate(self):
        """Test IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()