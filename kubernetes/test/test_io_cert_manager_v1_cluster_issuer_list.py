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
from kubernetes.client.models.io_cert_manager_v1_cluster_issuer_list import IoCertManagerV1ClusterIssuerList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerV1ClusterIssuerList(unittest.TestCase):
    """IoCertManagerV1ClusterIssuerList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerV1ClusterIssuerList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_list.IoCertManagerV1ClusterIssuerList()  # noqa: E501
        if include_optional :
            return IoCertManagerV1ClusterIssuerList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.io/cert_manager/v1/cluster_issuer.io.cert-manager.v1.ClusterIssuer(
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
                        spec = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec.io_cert_manager_v1_ClusterIssuer_spec(
                            acme = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_acme.io_cert_manager_v1_ClusterIssuer_spec_acme(
                                disable_account_key_generation = True, 
                                email = '0', 
                                enable_duration_feature = True, 
                                external_account_binding = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_acme_external_account_binding.io_cert_manager_v1_ClusterIssuer_spec_acme_externalAccountBinding(
                                    key_algorithm = 'HS256', 
                                    key_id = '0', 
                                    key_secret_ref = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_acme_external_account_binding_key_secret_ref.io_cert_manager_v1_ClusterIssuer_spec_acme_externalAccountBinding_keySecretRef(
                                        key = '0', 
                                        name = '0', ), ), 
                                preferred_chain = '0', 
                                private_key_secret_ref = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_acme_private_key_secret_ref.io_cert_manager_v1_ClusterIssuer_spec_acme_privateKeySecretRef(
                                    key = '0', 
                                    name = '0', ), 
                                server = '0', 
                                skip_tls_verify = True, 
                                solvers = [
                                    kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_acme_solvers.io_cert_manager_v1_ClusterIssuer_spec_acme_solvers(
                                        dns01 = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01.io_cert_manager_acme_v1_Challenge_spec_solver_dns01(
                                            acme_dns = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS(
                                                account_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns_account_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS_accountSecretRef(
                                                    key = '0', 
                                                    name = '0', ), 
                                                host = '0', ), 
                                            akamai = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_akamai.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_akamai(
                                                access_token_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns_account_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS_accountSecretRef(
                                                    key = '0', 
                                                    name = '0', ), 
                                                kubernetes.client_secret_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns_account_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS_accountSecretRef(
                                                    key = '0', 
                                                    name = '0', ), 
                                                kubernetes.client_token_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns_account_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS_accountSecretRef(
                                                    key = '0', 
                                                    name = '0', ), 
                                                service_consumer_domain = '0', ), 
                                            azure_dns = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_azure_dns.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_azureDNS(
                                                kubernetes.client_id = '0', 
                                                environment = 'AzurePublicCloud', 
                                                hosted_zone_name = '0', 
                                                managed_identity = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_azure_dns_managed_identity.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_azureDNS_managedIdentity(
                                                    kubernetes.client_id = '0', 
                                                    resource_id = '0', ), 
                                                resource_group_name = '0', 
                                                subscription_id = '0', 
                                                tenant_id = '0', ), 
                                            cloud_dns = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_cloud_dns.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_cloudDNS(
                                                hosted_zone_name = '0', 
                                                project = '0', 
                                                service_account_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns_account_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS_accountSecretRef(
                                                    key = '0', 
                                                    name = '0', ), ), 
                                            cloudflare = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_cloudflare.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_cloudflare(
                                                api_key_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_cloudflare_api_key_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_cloudflare_apiKeySecretRef(
                                                    key = '0', 
                                                    name = '0', ), 
                                                api_token_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_cloudflare_api_token_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_cloudflare_apiTokenSecretRef(
                                                    key = '0', 
                                                    name = '0', ), 
                                                email = '0', ), 
                                            cname_strategy = 'None', 
                                            digitalocean = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_digitalocean.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_digitalocean(
                                                token_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns_account_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS_accountSecretRef(
                                                    key = '0', 
                                                    name = '0', ), ), 
                                            rfc2136 = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_rfc2136.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_rfc2136(
                                                nameserver = '0', 
                                                tsig_algorithm = '0', 
                                                tsig_key_name = '0', 
                                                tsig_secret_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_rfc2136_tsig_secret_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_rfc2136_tsigSecretSecretRef(
                                                    key = '0', 
                                                    name = '0', ), ), 
                                            route53 = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_route53.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_route53(
                                                access_key_id = '0', 
                                                hosted_zone_id = '0', 
                                                region = '0', 
                                                role = '0', 
                                                secret_access_key_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_route53_secret_access_key_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_route53_secretAccessKeySecretRef(
                                                    key = '0', 
                                                    name = '0', ), ), 
                                            webhook = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_webhook.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_webhook(
                                                config = kubernetes.client.models.config.config(), 
                                                group_name = '0', 
                                                solver_name = '0', ), ), 
                                        http01 = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01.io_cert_manager_acme_v1_Challenge_spec_solver_http01(
                                            gateway_http_route = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_gateway_http_route.io_cert_manager_acme_v1_Challenge_spec_solver_http01_gatewayHTTPRoute(
                                                service_type = '0', ), 
                                            ingress = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress(
                                                class = '0', 
                                                ingress_template = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_ingress_template.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_ingressTemplate(), 
                                                name = '0', 
                                                pod_template = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate(), 
                                                service_type = '0', ), ), 
                                        selector = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_selector.io_cert_manager_acme_v1_Challenge_spec_solver_selector(
                                            dns_names = [
                                                '0'
                                                ], 
                                            dns_zones = [
                                                '0'
                                                ], 
                                            match_labels = {
                                                'key' : '0'
                                                }, ), )
                                    ], ), 
                            ca = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_ca.io_cert_manager_v1_ClusterIssuer_spec_ca(
                                crl_distribution_points = [
                                    '0'
                                    ], 
                                ocsp_servers = [
                                    '0'
                                    ], 
                                secret_name = '0', ), 
                            self_signed = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_self_signed.io_cert_manager_v1_ClusterIssuer_spec_selfSigned(), 
                            vault = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault.io_cert_manager_v1_ClusterIssuer_spec_vault(
                                auth = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault_auth.io_cert_manager_v1_ClusterIssuer_spec_vault_auth(
                                    app_role = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault_auth_app_role.io_cert_manager_v1_ClusterIssuer_spec_vault_auth_appRole(
                                        path = '0', 
                                        role_id = '0', 
                                        secret_ref = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault_auth_app_role_secret_ref.io_cert_manager_v1_ClusterIssuer_spec_vault_auth_appRole_secretRef(
                                            key = '0', 
                                            name = '0', ), ), 
                                    kubernetes = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault_auth_kubernetes.io_cert_manager_v1_ClusterIssuer_spec_vault_auth_kubernetes(
                                        mount_path = '0', 
                                        role = '0', 
                                        secret_ref = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault_auth_kubernetes_secret_ref.io_cert_manager_v1_ClusterIssuer_spec_vault_auth_kubernetes_secretRef(
                                            key = '0', 
                                            name = '0', ), ), ), 
                                ca_bundle = 'YQ==', 
                                namespace = '0', 
                                path = '0', 
                                server = '0', ), 
                            venafi = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_venafi.io_cert_manager_v1_ClusterIssuer_spec_venafi(
                                cloud = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_venafi_cloud.io_cert_manager_v1_ClusterIssuer_spec_venafi_cloud(
                                    api_token_secret_ref = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_venafi_cloud_api_token_secret_ref.io_cert_manager_v1_ClusterIssuer_spec_venafi_cloud_apiTokenSecretRef(
                                        key = '0', 
                                        name = '0', ), 
                                    url = '0', ), 
                                tpp = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_venafi_tpp.io_cert_manager_v1_ClusterIssuer_spec_venafi_tpp(
                                    ca_bundle = 'YQ==', 
                                    credentials_ref = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_venafi_tpp_credentials_ref.io_cert_manager_v1_ClusterIssuer_spec_venafi_tpp_credentialsRef(
                                        name = '0', ), 
                                    url = '0', ), 
                                zone = '0', ), ), 
                        status = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_status.io_cert_manager_v1_ClusterIssuer_status(
                            conditions = [
                                kubernetes.client.models.io_cert_manager_v1_cluster_issuer_status_conditions.io_cert_manager_v1_ClusterIssuer_status_conditions(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    observed_generation = 56, 
                                    reason = '0', 
                                    status = 'True', 
                                    type = '0', )
                                ], ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return IoCertManagerV1ClusterIssuerList(
                items = [
                    kubernetes.client.models.io/cert_manager/v1/cluster_issuer.io.cert-manager.v1.ClusterIssuer(
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
                        spec = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec.io_cert_manager_v1_ClusterIssuer_spec(
                            acme = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_acme.io_cert_manager_v1_ClusterIssuer_spec_acme(
                                disable_account_key_generation = True, 
                                email = '0', 
                                enable_duration_feature = True, 
                                external_account_binding = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_acme_external_account_binding.io_cert_manager_v1_ClusterIssuer_spec_acme_externalAccountBinding(
                                    key_algorithm = 'HS256', 
                                    key_id = '0', 
                                    key_secret_ref = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_acme_external_account_binding_key_secret_ref.io_cert_manager_v1_ClusterIssuer_spec_acme_externalAccountBinding_keySecretRef(
                                        key = '0', 
                                        name = '0', ), ), 
                                preferred_chain = '0', 
                                private_key_secret_ref = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_acme_private_key_secret_ref.io_cert_manager_v1_ClusterIssuer_spec_acme_privateKeySecretRef(
                                    key = '0', 
                                    name = '0', ), 
                                server = '0', 
                                skip_tls_verify = True, 
                                solvers = [
                                    kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_acme_solvers.io_cert_manager_v1_ClusterIssuer_spec_acme_solvers(
                                        dns01 = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01.io_cert_manager_acme_v1_Challenge_spec_solver_dns01(
                                            acme_dns = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS(
                                                account_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns_account_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS_accountSecretRef(
                                                    key = '0', 
                                                    name = '0', ), 
                                                host = '0', ), 
                                            akamai = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_akamai.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_akamai(
                                                access_token_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns_account_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS_accountSecretRef(
                                                    key = '0', 
                                                    name = '0', ), 
                                                kubernetes.client_secret_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns_account_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS_accountSecretRef(
                                                    key = '0', 
                                                    name = '0', ), 
                                                kubernetes.client_token_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns_account_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS_accountSecretRef(
                                                    key = '0', 
                                                    name = '0', ), 
                                                service_consumer_domain = '0', ), 
                                            azure_dns = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_azure_dns.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_azureDNS(
                                                kubernetes.client_id = '0', 
                                                environment = 'AzurePublicCloud', 
                                                hosted_zone_name = '0', 
                                                managed_identity = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_azure_dns_managed_identity.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_azureDNS_managedIdentity(
                                                    kubernetes.client_id = '0', 
                                                    resource_id = '0', ), 
                                                resource_group_name = '0', 
                                                subscription_id = '0', 
                                                tenant_id = '0', ), 
                                            cloud_dns = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_cloud_dns.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_cloudDNS(
                                                hosted_zone_name = '0', 
                                                project = '0', 
                                                service_account_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns_account_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS_accountSecretRef(
                                                    key = '0', 
                                                    name = '0', ), ), 
                                            cloudflare = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_cloudflare.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_cloudflare(
                                                api_key_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_cloudflare_api_key_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_cloudflare_apiKeySecretRef(
                                                    key = '0', 
                                                    name = '0', ), 
                                                api_token_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_cloudflare_api_token_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_cloudflare_apiTokenSecretRef(
                                                    key = '0', 
                                                    name = '0', ), 
                                                email = '0', ), 
                                            cname_strategy = 'None', 
                                            digitalocean = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_digitalocean.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_digitalocean(
                                                token_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_acme_dns_account_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_acmeDNS_accountSecretRef(
                                                    key = '0', 
                                                    name = '0', ), ), 
                                            rfc2136 = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_rfc2136.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_rfc2136(
                                                nameserver = '0', 
                                                tsig_algorithm = '0', 
                                                tsig_key_name = '0', 
                                                tsig_secret_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_rfc2136_tsig_secret_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_rfc2136_tsigSecretSecretRef(
                                                    key = '0', 
                                                    name = '0', ), ), 
                                            route53 = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_route53.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_route53(
                                                access_key_id = '0', 
                                                hosted_zone_id = '0', 
                                                region = '0', 
                                                role = '0', 
                                                secret_access_key_secret_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_route53_secret_access_key_secret_ref.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_route53_secretAccessKeySecretRef(
                                                    key = '0', 
                                                    name = '0', ), ), 
                                            webhook = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_webhook.io_cert_manager_acme_v1_Challenge_spec_solver_dns01_webhook(
                                                config = kubernetes.client.models.config.config(), 
                                                group_name = '0', 
                                                solver_name = '0', ), ), 
                                        http01 = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01.io_cert_manager_acme_v1_Challenge_spec_solver_http01(
                                            gateway_http_route = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_gateway_http_route.io_cert_manager_acme_v1_Challenge_spec_solver_http01_gatewayHTTPRoute(
                                                service_type = '0', ), 
                                            ingress = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress(
                                                class = '0', 
                                                ingress_template = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_ingress_template.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_ingressTemplate(), 
                                                name = '0', 
                                                pod_template = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate(), 
                                                service_type = '0', ), ), 
                                        selector = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_selector.io_cert_manager_acme_v1_Challenge_spec_solver_selector(
                                            dns_names = [
                                                '0'
                                                ], 
                                            dns_zones = [
                                                '0'
                                                ], 
                                            match_labels = {
                                                'key' : '0'
                                                }, ), )
                                    ], ), 
                            ca = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_ca.io_cert_manager_v1_ClusterIssuer_spec_ca(
                                crl_distribution_points = [
                                    '0'
                                    ], 
                                ocsp_servers = [
                                    '0'
                                    ], 
                                secret_name = '0', ), 
                            self_signed = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_self_signed.io_cert_manager_v1_ClusterIssuer_spec_selfSigned(), 
                            vault = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault.io_cert_manager_v1_ClusterIssuer_spec_vault(
                                auth = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault_auth.io_cert_manager_v1_ClusterIssuer_spec_vault_auth(
                                    app_role = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault_auth_app_role.io_cert_manager_v1_ClusterIssuer_spec_vault_auth_appRole(
                                        path = '0', 
                                        role_id = '0', 
                                        secret_ref = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault_auth_app_role_secret_ref.io_cert_manager_v1_ClusterIssuer_spec_vault_auth_appRole_secretRef(
                                            key = '0', 
                                            name = '0', ), ), 
                                    kubernetes = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault_auth_kubernetes.io_cert_manager_v1_ClusterIssuer_spec_vault_auth_kubernetes(
                                        mount_path = '0', 
                                        role = '0', 
                                        secret_ref = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault_auth_kubernetes_secret_ref.io_cert_manager_v1_ClusterIssuer_spec_vault_auth_kubernetes_secretRef(
                                            key = '0', 
                                            name = '0', ), ), ), 
                                ca_bundle = 'YQ==', 
                                namespace = '0', 
                                path = '0', 
                                server = '0', ), 
                            venafi = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_venafi.io_cert_manager_v1_ClusterIssuer_spec_venafi(
                                cloud = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_venafi_cloud.io_cert_manager_v1_ClusterIssuer_spec_venafi_cloud(
                                    api_token_secret_ref = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_venafi_cloud_api_token_secret_ref.io_cert_manager_v1_ClusterIssuer_spec_venafi_cloud_apiTokenSecretRef(
                                        key = '0', 
                                        name = '0', ), 
                                    url = '0', ), 
                                tpp = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_venafi_tpp.io_cert_manager_v1_ClusterIssuer_spec_venafi_tpp(
                                    ca_bundle = 'YQ==', 
                                    credentials_ref = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_venafi_tpp_credentials_ref.io_cert_manager_v1_ClusterIssuer_spec_venafi_tpp_credentialsRef(
                                        name = '0', ), 
                                    url = '0', ), 
                                zone = '0', ), ), 
                        status = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_status.io_cert_manager_v1_ClusterIssuer_status(
                            conditions = [
                                kubernetes.client.models.io_cert_manager_v1_cluster_issuer_status_conditions.io_cert_manager_v1_ClusterIssuer_status_conditions(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    observed_generation = 56, 
                                    reason = '0', 
                                    status = 'True', 
                                    type = '0', )
                                ], ), )
                    ],
        )

    def testIoCertManagerV1ClusterIssuerList(self):
        """Test IoCertManagerV1ClusterIssuerList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()