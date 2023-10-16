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
from kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_data import IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecData  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecData(unittest.TestCase):
    """IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_data.IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecData()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecData(
                remote_ref = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_remote_ref.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_remoteRef(
                    conversion_strategy = '0', 
                    decoding_strategy = '0', 
                    key = '0', 
                    metadata_policy = '0', 
                    property = '0', 
                    version = '0', ), 
                secret_key = '0', 
                source_ref = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_source_ref.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_sourceRef(
                    generator_ref = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_source_ref_generator_ref.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_sourceRef_generatorRef(
                        api_version = '0', 
                        kind = '0', 
                        name = '0', ), 
                    store_ref = kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_secret_store_ref.io_external_secrets_v1alpha1_ExternalSecret_spec_secretStoreRef(
                        kind = '0', 
                        name = '0', ), )
            )
        else :
            return IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecData(
                remote_ref = kubernetes.client.models.io_external_secrets_v1beta1_cluster_external_secret_spec_external_secret_spec_remote_ref.io_external_secrets_v1beta1_ClusterExternalSecret_spec_externalSecretSpec_remoteRef(
                    conversion_strategy = '0', 
                    decoding_strategy = '0', 
                    key = '0', 
                    metadata_policy = '0', 
                    property = '0', 
                    version = '0', ),
                secret_key = '0',
        )

    def testIoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecData(self):
        """Test IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
