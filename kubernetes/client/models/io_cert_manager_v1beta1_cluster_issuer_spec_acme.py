# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class IoCertManagerV1beta1ClusterIssuerSpecAcme(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'disable_account_key_generation': 'bool',
        'email': 'str',
        'enable_duration_feature': 'bool',
        'external_account_binding': 'IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding',
        'preferred_chain': 'str',
        'private_key_secret_ref': 'IoCertManagerV1ClusterIssuerSpecAcmePrivateKeySecretRef',
        'server': 'str',
        'skip_tls_verify': 'bool',
        'solvers': 'list[IoCertManagerV1beta1ClusterIssuerSpecAcmeSolvers]'
    }

    attribute_map = {
        'disable_account_key_generation': 'disableAccountKeyGeneration',
        'email': 'email',
        'enable_duration_feature': 'enableDurationFeature',
        'external_account_binding': 'externalAccountBinding',
        'preferred_chain': 'preferredChain',
        'private_key_secret_ref': 'privateKeySecretRef',
        'server': 'server',
        'skip_tls_verify': 'skipTLSVerify',
        'solvers': 'solvers'
    }

    def __init__(self, disable_account_key_generation=None, email=None, enable_duration_feature=None, external_account_binding=None, preferred_chain=None, private_key_secret_ref=None, server=None, skip_tls_verify=None, solvers=None, local_vars_configuration=None):  # noqa: E501
        """IoCertManagerV1beta1ClusterIssuerSpecAcme - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._disable_account_key_generation = None
        self._email = None
        self._enable_duration_feature = None
        self._external_account_binding = None
        self._preferred_chain = None
        self._private_key_secret_ref = None
        self._server = None
        self._skip_tls_verify = None
        self._solvers = None
        self.discriminator = None

        if disable_account_key_generation is not None:
            self.disable_account_key_generation = disable_account_key_generation
        if email is not None:
            self.email = email
        if enable_duration_feature is not None:
            self.enable_duration_feature = enable_duration_feature
        if external_account_binding is not None:
            self.external_account_binding = external_account_binding
        if preferred_chain is not None:
            self.preferred_chain = preferred_chain
        self.private_key_secret_ref = private_key_secret_ref
        self.server = server
        if skip_tls_verify is not None:
            self.skip_tls_verify = skip_tls_verify
        if solvers is not None:
            self.solvers = solvers

    @property
    def disable_account_key_generation(self):
        """Gets the disable_account_key_generation of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501

        Enables or disables generating a new ACME account key. If true, the Issuer resource will *not* request a new account but will expect the account key to be supplied via an existing secret. If false, the cert-manager system will generate a new ACME account key for the Issuer. Defaults to false.  # noqa: E501

        :return: The disable_account_key_generation of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :rtype: bool
        """
        return self._disable_account_key_generation

    @disable_account_key_generation.setter
    def disable_account_key_generation(self, disable_account_key_generation):
        """Sets the disable_account_key_generation of this IoCertManagerV1beta1ClusterIssuerSpecAcme.

        Enables or disables generating a new ACME account key. If true, the Issuer resource will *not* request a new account but will expect the account key to be supplied via an existing secret. If false, the cert-manager system will generate a new ACME account key for the Issuer. Defaults to false.  # noqa: E501

        :param disable_account_key_generation: The disable_account_key_generation of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :type: bool
        """

        self._disable_account_key_generation = disable_account_key_generation

    @property
    def email(self):
        """Gets the email of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501

        Email is the email address to be associated with the ACME account. This field is optional, but it is strongly recommended to be set. It will be used to contact you in case of issues with your account or certificates, including expiry notification emails. This field may be updated after the account is initially registered.  # noqa: E501

        :return: The email of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this IoCertManagerV1beta1ClusterIssuerSpecAcme.

        Email is the email address to be associated with the ACME account. This field is optional, but it is strongly recommended to be set. It will be used to contact you in case of issues with your account or certificates, including expiry notification emails. This field may be updated after the account is initially registered.  # noqa: E501

        :param email: The email of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def enable_duration_feature(self):
        """Gets the enable_duration_feature of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501

        Enables requesting a Not After date on certificates that matches the duration of the certificate. This is not supported by all ACME servers like Let's Encrypt. If set to true when the ACME server does not support it it will create an error on the Order. Defaults to false.  # noqa: E501

        :return: The enable_duration_feature of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :rtype: bool
        """
        return self._enable_duration_feature

    @enable_duration_feature.setter
    def enable_duration_feature(self, enable_duration_feature):
        """Sets the enable_duration_feature of this IoCertManagerV1beta1ClusterIssuerSpecAcme.

        Enables requesting a Not After date on certificates that matches the duration of the certificate. This is not supported by all ACME servers like Let's Encrypt. If set to true when the ACME server does not support it it will create an error on the Order. Defaults to false.  # noqa: E501

        :param enable_duration_feature: The enable_duration_feature of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :type: bool
        """

        self._enable_duration_feature = enable_duration_feature

    @property
    def external_account_binding(self):
        """Gets the external_account_binding of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501


        :return: The external_account_binding of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :rtype: IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding
        """
        return self._external_account_binding

    @external_account_binding.setter
    def external_account_binding(self, external_account_binding):
        """Sets the external_account_binding of this IoCertManagerV1beta1ClusterIssuerSpecAcme.


        :param external_account_binding: The external_account_binding of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :type: IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding
        """

        self._external_account_binding = external_account_binding

    @property
    def preferred_chain(self):
        """Gets the preferred_chain of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501

        PreferredChain is the chain to use if the ACME server outputs multiple. PreferredChain is no guarantee that this one gets delivered by the ACME endpoint. For example, for Let's Encrypt's DST crosssign you would use: \"DST Root CA X3\" or \"ISRG Root X1\" for the newer Let's Encrypt root CA. This value picks the first certificate bundle in the ACME alternative chains that has a certificate with this value as its issuer's CN  # noqa: E501

        :return: The preferred_chain of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :rtype: str
        """
        return self._preferred_chain

    @preferred_chain.setter
    def preferred_chain(self, preferred_chain):
        """Sets the preferred_chain of this IoCertManagerV1beta1ClusterIssuerSpecAcme.

        PreferredChain is the chain to use if the ACME server outputs multiple. PreferredChain is no guarantee that this one gets delivered by the ACME endpoint. For example, for Let's Encrypt's DST crosssign you would use: \"DST Root CA X3\" or \"ISRG Root X1\" for the newer Let's Encrypt root CA. This value picks the first certificate bundle in the ACME alternative chains that has a certificate with this value as its issuer's CN  # noqa: E501

        :param preferred_chain: The preferred_chain of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                preferred_chain is not None and len(preferred_chain) > 64):
            raise ValueError("Invalid value for `preferred_chain`, length must be less than or equal to `64`")  # noqa: E501

        self._preferred_chain = preferred_chain

    @property
    def private_key_secret_ref(self):
        """Gets the private_key_secret_ref of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501


        :return: The private_key_secret_ref of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :rtype: IoCertManagerV1ClusterIssuerSpecAcmePrivateKeySecretRef
        """
        return self._private_key_secret_ref

    @private_key_secret_ref.setter
    def private_key_secret_ref(self, private_key_secret_ref):
        """Sets the private_key_secret_ref of this IoCertManagerV1beta1ClusterIssuerSpecAcme.


        :param private_key_secret_ref: The private_key_secret_ref of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :type: IoCertManagerV1ClusterIssuerSpecAcmePrivateKeySecretRef
        """
        if self.local_vars_configuration.client_side_validation and private_key_secret_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `private_key_secret_ref`, must not be `None`")  # noqa: E501

        self._private_key_secret_ref = private_key_secret_ref

    @property
    def server(self):
        """Gets the server of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501

        Server is the URL used to access the ACME server's 'directory' endpoint. For example, for Let's Encrypt's staging endpoint, you would use: \"https://acme-staging-v02.api.letsencrypt.org/directory\". Only ACME v2 endpoints (i.e. RFC 8555) are supported.  # noqa: E501

        :return: The server of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this IoCertManagerV1beta1ClusterIssuerSpecAcme.

        Server is the URL used to access the ACME server's 'directory' endpoint. For example, for Let's Encrypt's staging endpoint, you would use: \"https://acme-staging-v02.api.letsencrypt.org/directory\". Only ACME v2 endpoints (i.e. RFC 8555) are supported.  # noqa: E501

        :param server: The server of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and server is None:  # noqa: E501
            raise ValueError("Invalid value for `server`, must not be `None`")  # noqa: E501

        self._server = server

    @property
    def skip_tls_verify(self):
        """Gets the skip_tls_verify of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501

        Enables or disables validation of the ACME server TLS certificate. If true, requests to the ACME server will not have their TLS certificate validated (i.e. insecure connections will be allowed). Only enable this option in development environments. The cert-manager system installed roots will be used to verify connections to the ACME server if this is false. Defaults to false.  # noqa: E501

        :return: The skip_tls_verify of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :rtype: bool
        """
        return self._skip_tls_verify

    @skip_tls_verify.setter
    def skip_tls_verify(self, skip_tls_verify):
        """Sets the skip_tls_verify of this IoCertManagerV1beta1ClusterIssuerSpecAcme.

        Enables or disables validation of the ACME server TLS certificate. If true, requests to the ACME server will not have their TLS certificate validated (i.e. insecure connections will be allowed). Only enable this option in development environments. The cert-manager system installed roots will be used to verify connections to the ACME server if this is false. Defaults to false.  # noqa: E501

        :param skip_tls_verify: The skip_tls_verify of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :type: bool
        """

        self._skip_tls_verify = skip_tls_verify

    @property
    def solvers(self):
        """Gets the solvers of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501

        Solvers is a list of challenge solvers that will be used to solve ACME challenges for the matching domains. Solver configurations must be provided in order to obtain certificates from an ACME server. For more information, see: https://cert-manager.io/docs/configuration/acme/  # noqa: E501

        :return: The solvers of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :rtype: list[IoCertManagerV1beta1ClusterIssuerSpecAcmeSolvers]
        """
        return self._solvers

    @solvers.setter
    def solvers(self, solvers):
        """Sets the solvers of this IoCertManagerV1beta1ClusterIssuerSpecAcme.

        Solvers is a list of challenge solvers that will be used to solve ACME challenges for the matching domains. Solver configurations must be provided in order to obtain certificates from an ACME server. For more information, see: https://cert-manager.io/docs/configuration/acme/  # noqa: E501

        :param solvers: The solvers of this IoCertManagerV1beta1ClusterIssuerSpecAcme.  # noqa: E501
        :type: list[IoCertManagerV1beta1ClusterIssuerSpecAcmeSolvers]
        """

        self._solvers = solvers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoCertManagerV1beta1ClusterIssuerSpecAcme):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoCertManagerV1beta1ClusterIssuerSpecAcme):
            return True

        return self.to_dict() != other.to_dict()
