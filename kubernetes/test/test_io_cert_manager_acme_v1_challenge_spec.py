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
from kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec import IoCertManagerAcmeV1ChallengeSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerAcmeV1ChallengeSpec(unittest.TestCase):
    """IoCertManagerAcmeV1ChallengeSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerAcmeV1ChallengeSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec.IoCertManagerAcmeV1ChallengeSpec()  # noqa: E501
        if include_optional :
            return IoCertManagerAcmeV1ChallengeSpec(
                authorization_url = '0', 
                dns_name = '0', 
                issuer_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_issuer_ref.io_cert_manager_acme_v1_Challenge_spec_issuerRef(
                    group = '0', 
                    kind = '0', 
                    name = '0', ), 
                key = '0', 
                solver = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver.io_cert_manager_acme_v1_Challenge_spec_solver(
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
                            labels = {
                                'key' : '0'
                                }, 
                            service_type = '0', ), 
                        ingress = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress(
                            class = '0', 
                            ingress_template = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_ingress_template.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_ingressTemplate(
                                metadata = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_ingress_template_metadata.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_ingressTemplate_metadata(
                                    annotations = {
                                        'key' : '0'
                                        }, ), ), 
                            name = '0', 
                            pod_template = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate(
                                spec = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec(
                                    affinity = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec_affinity.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec_affinity(
                                        node_affinity = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity(
                                            preferred_during_scheduling_ignored_during_execution = [
                                                kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preferredDuringSchedulingIgnoredDuringExecution(
                                                    preference = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference(
                                                        match_expressions = [
                                                            kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference_matchExpressions(
                                                                key = '0', 
                                                                operator = '0', 
                                                                values = [
                                                                    '0'
                                                                    ], )
                                                            ], 
                                                        match_fields = [
                                                            kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference_matchExpressions(
                                                                key = '0', 
                                                                operator = '0', )
                                                            ], ), 
                                                    weight = 56, )
                                                ], 
                                            required_during_scheduling_ignored_during_execution = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_required_during_scheduling_ignored_during_execution.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_requiredDuringSchedulingIgnoredDuringExecution(
                                                node_selector_terms = [
                                                    kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_requiredDuringSchedulingIgnoredDuringExecution_nodeSelectorTerms()
                                                    ], ), ), 
                                        pod_affinity = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity(), 
                                        pod_anti_affinity = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_anti_affinity.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAntiAffinity(), ), 
                                    node_selector = {
                                        'key' : '0'
                                        }, 
                                    priority_class_name = '0', 
                                    service_account_name = '0', 
                                    tolerations = [
                                        kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_tolerations.com_coreos_monitoring_v1_Alertmanager_spec_tolerations(
                                            effect = '0', 
                                            key = '0', 
                                            operator = '0', 
                                            toleration_seconds = 56, 
                                            value = '0', )
                                        ], ), ), 
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
                            }, ), ), 
                token = '0', 
                type = 'HTTP-01', 
                url = '0', 
                wildcard = True
            )
        else :
            return IoCertManagerAcmeV1ChallengeSpec(
                authorization_url = '0',
                dns_name = '0',
                issuer_ref = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_issuer_ref.io_cert_manager_acme_v1_Challenge_spec_issuerRef(
                    group = '0', 
                    kind = '0', 
                    name = '0', ),
                key = '0',
                solver = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver.io_cert_manager_acme_v1_Challenge_spec_solver(
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
                            labels = {
                                'key' : '0'
                                }, 
                            service_type = '0', ), 
                        ingress = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress(
                            class = '0', 
                            ingress_template = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_ingress_template.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_ingressTemplate(
                                metadata = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_ingress_template_metadata.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_ingressTemplate_metadata(
                                    annotations = {
                                        'key' : '0'
                                        }, ), ), 
                            name = '0', 
                            pod_template = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate(
                                spec = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec(
                                    affinity = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec_affinity.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec_affinity(
                                        node_affinity = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity(
                                            preferred_during_scheduling_ignored_during_execution = [
                                                kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preferredDuringSchedulingIgnoredDuringExecution(
                                                    preference = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference(
                                                        match_expressions = [
                                                            kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference_matchExpressions(
                                                                key = '0', 
                                                                operator = '0', 
                                                                values = [
                                                                    '0'
                                                                    ], )
                                                            ], 
                                                        match_fields = [
                                                            kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference_matchExpressions(
                                                                key = '0', 
                                                                operator = '0', )
                                                            ], ), 
                                                    weight = 56, )
                                                ], 
                                            required_during_scheduling_ignored_during_execution = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_required_during_scheduling_ignored_during_execution.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_requiredDuringSchedulingIgnoredDuringExecution(
                                                node_selector_terms = [
                                                    kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_requiredDuringSchedulingIgnoredDuringExecution_nodeSelectorTerms()
                                                    ], ), ), 
                                        pod_affinity = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity(), 
                                        pod_anti_affinity = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_anti_affinity.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAntiAffinity(), ), 
                                    node_selector = {
                                        'key' : '0'
                                        }, 
                                    priority_class_name = '0', 
                                    service_account_name = '0', 
                                    tolerations = [
                                        kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_tolerations.com_coreos_monitoring_v1_Alertmanager_spec_tolerations(
                                            effect = '0', 
                                            key = '0', 
                                            operator = '0', 
                                            toleration_seconds = 56, 
                                            value = '0', )
                                        ], ), ), 
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
                            }, ), ),
                token = '0',
                type = 'HTTP-01',
                url = '0',
        )

    def testIoCertManagerAcmeV1ChallengeSpec(self):
        """Test IoCertManagerAcmeV1ChallengeSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
