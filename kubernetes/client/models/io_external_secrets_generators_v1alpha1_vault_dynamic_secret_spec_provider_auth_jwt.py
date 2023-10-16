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


class IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt(object):
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
        'kubernetes_service_account_token': 'IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtKubernetesServiceAccountToken',
        'path': 'str',
        'role': 'str',
        'secret_ref': 'IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtSecretRef'
    }

    attribute_map = {
        'kubernetes_service_account_token': 'kubernetesServiceAccountToken',
        'path': 'path',
        'role': 'role',
        'secret_ref': 'secretRef'
    }

    def __init__(self, kubernetes_service_account_token=None, path=None, role=None, secret_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kubernetes_service_account_token = None
        self._path = None
        self._role = None
        self._secret_ref = None
        self.discriminator = None

        if kubernetes_service_account_token is not None:
            self.kubernetes_service_account_token = kubernetes_service_account_token
        self.path = path
        if role is not None:
            self.role = role
        if secret_ref is not None:
            self.secret_ref = secret_ref

    @property
    def kubernetes_service_account_token(self):
        """Gets the kubernetes_service_account_token of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.  # noqa: E501


        :return: The kubernetes_service_account_token of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.  # noqa: E501
        :rtype: IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtKubernetesServiceAccountToken
        """
        return self._kubernetes_service_account_token

    @kubernetes_service_account_token.setter
    def kubernetes_service_account_token(self, kubernetes_service_account_token):
        """Sets the kubernetes_service_account_token of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.


        :param kubernetes_service_account_token: The kubernetes_service_account_token of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.  # noqa: E501
        :type: IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtKubernetesServiceAccountToken
        """

        self._kubernetes_service_account_token = kubernetes_service_account_token

    @property
    def path(self):
        """Gets the path of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.  # noqa: E501

        Path where the JWT authentication backend is mounted in Vault, e.g: \"jwt\"  # noqa: E501

        :return: The path of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.

        Path where the JWT authentication backend is mounted in Vault, e.g: \"jwt\"  # noqa: E501

        :param path: The path of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def role(self):
        """Gets the role of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.  # noqa: E501

        Role is a JWT role to authenticate using the JWT/OIDC Vault authentication method  # noqa: E501

        :return: The role of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.

        Role is a JWT role to authenticate using the JWT/OIDC Vault authentication method  # noqa: E501

        :param role: The role of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def secret_ref(self):
        """Gets the secret_ref of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.  # noqa: E501


        :return: The secret_ref of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.  # noqa: E501
        :rtype: IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtSecretRef
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.


        :param secret_ref: The secret_ref of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt.  # noqa: E501
        :type: IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtSecretRef
        """

        self._secret_ref = secret_ref

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
        if not isinstance(other, IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt):
            return True

        return self.to_dict() != other.to_dict()
