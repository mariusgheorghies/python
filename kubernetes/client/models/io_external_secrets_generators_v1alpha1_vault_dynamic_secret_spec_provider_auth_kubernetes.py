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


class IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes(object):
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
        'mount_path': 'str',
        'role': 'str',
        'secret_ref': 'IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetesSecretRef',
        'service_account_ref': 'IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetesServiceAccountRef'
    }

    attribute_map = {
        'mount_path': 'mountPath',
        'role': 'role',
        'secret_ref': 'secretRef',
        'service_account_ref': 'serviceAccountRef'
    }

    def __init__(self, mount_path=None, role=None, secret_ref=None, service_account_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mount_path = None
        self._role = None
        self._secret_ref = None
        self._service_account_ref = None
        self.discriminator = None

        self.mount_path = mount_path
        self.role = role
        if secret_ref is not None:
            self.secret_ref = secret_ref
        if service_account_ref is not None:
            self.service_account_ref = service_account_ref

    @property
    def mount_path(self):
        """Gets the mount_path of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.  # noqa: E501

        Path where the Kubernetes authentication backend is mounted in Vault, e.g: \"kubernetes\"  # noqa: E501

        :return: The mount_path of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.  # noqa: E501
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """Sets the mount_path of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.

        Path where the Kubernetes authentication backend is mounted in Vault, e.g: \"kubernetes\"  # noqa: E501

        :param mount_path: The mount_path of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mount_path is None:  # noqa: E501
            raise ValueError("Invalid value for `mount_path`, must not be `None`")  # noqa: E501

        self._mount_path = mount_path

    @property
    def role(self):
        """Gets the role of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.  # noqa: E501

        A required field containing the Vault Role to assume. A Role binds a Kubernetes ServiceAccount with a set of Vault policies.  # noqa: E501

        :return: The role of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.

        A required field containing the Vault Role to assume. A Role binds a Kubernetes ServiceAccount with a set of Vault policies.  # noqa: E501

        :param role: The role of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and role is None:  # noqa: E501
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def secret_ref(self):
        """Gets the secret_ref of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.  # noqa: E501


        :return: The secret_ref of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.  # noqa: E501
        :rtype: IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetesSecretRef
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.


        :param secret_ref: The secret_ref of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.  # noqa: E501
        :type: IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetesSecretRef
        """

        self._secret_ref = secret_ref

    @property
    def service_account_ref(self):
        """Gets the service_account_ref of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.  # noqa: E501


        :return: The service_account_ref of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.  # noqa: E501
        :rtype: IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetesServiceAccountRef
        """
        return self._service_account_ref

    @service_account_ref.setter
    def service_account_ref(self, service_account_ref):
        """Sets the service_account_ref of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.


        :param service_account_ref: The service_account_ref of this IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.  # noqa: E501
        :type: IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetesServiceAccountRef
        """

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
        if not isinstance(other, IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes):
            return True

        return self.to_dict() != other.to_dict()