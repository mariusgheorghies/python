# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.25.12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken(object):
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
        'audiences': 'list[str]',
        'expiration_seconds': 'int',
        'service_account_ref': 'IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtKubernetesServiceAccountTokenServiceAccountRef'
    }

    attribute_map = {
        'audiences': 'audiences',
        'expiration_seconds': 'expirationSeconds',
        'service_account_ref': 'serviceAccountRef'
    }

    def __init__(self, audiences=None, expiration_seconds=None, service_account_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._audiences = None
        self._expiration_seconds = None
        self._service_account_ref = None
        self.discriminator = None

        if audiences is not None:
            self.audiences = audiences
        if expiration_seconds is not None:
            self.expiration_seconds = expiration_seconds
        self.service_account_ref = service_account_ref

    @property
    def audiences(self):
        """Gets the audiences of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken.  # noqa: E501

        Optional audiences field that will be used to request a temporary Kubernetes service account token for the service account referenced by `serviceAccountRef`. Defaults to a single audience `vault` it not specified.  # noqa: E501

        :return: The audiences of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken.  # noqa: E501
        :rtype: list[str]
        """
        return self._audiences

    @audiences.setter
    def audiences(self, audiences):
        """Sets the audiences of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken.

        Optional audiences field that will be used to request a temporary Kubernetes service account token for the service account referenced by `serviceAccountRef`. Defaults to a single audience `vault` it not specified.  # noqa: E501

        :param audiences: The audiences of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken.  # noqa: E501
        :type: list[str]
        """

        self._audiences = audiences

    @property
    def expiration_seconds(self):
        """Gets the expiration_seconds of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken.  # noqa: E501

        Optional expiration time in seconds that will be used to request a temporary Kubernetes service account token for the service account referenced by `serviceAccountRef`. Defaults to 10 minutes.  # noqa: E501

        :return: The expiration_seconds of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken.  # noqa: E501
        :rtype: int
        """
        return self._expiration_seconds

    @expiration_seconds.setter
    def expiration_seconds(self, expiration_seconds):
        """Sets the expiration_seconds of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken.

        Optional expiration time in seconds that will be used to request a temporary Kubernetes service account token for the service account referenced by `serviceAccountRef`. Defaults to 10 minutes.  # noqa: E501

        :param expiration_seconds: The expiration_seconds of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken.  # noqa: E501
        :type: int
        """

        self._expiration_seconds = expiration_seconds

    @property
    def service_account_ref(self):
        """Gets the service_account_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken.  # noqa: E501


        :return: The service_account_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken.  # noqa: E501
        :rtype: IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtKubernetesServiceAccountTokenServiceAccountRef
        """
        return self._service_account_ref

    @service_account_ref.setter
    def service_account_ref(self, service_account_ref):
        """Sets the service_account_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken.


        :param service_account_ref: The service_account_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken.  # noqa: E501
        :type: IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtKubernetesServiceAccountTokenServiceAccountRef
        """
        if self.local_vars_configuration.client_side_validation and service_account_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `service_account_ref`, must not be `None`")  # noqa: E501

        self._service_account_ref = service_account_ref

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
        if not isinstance(other, IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken):
            return True

        return self.to_dict() != other.to_dict()
