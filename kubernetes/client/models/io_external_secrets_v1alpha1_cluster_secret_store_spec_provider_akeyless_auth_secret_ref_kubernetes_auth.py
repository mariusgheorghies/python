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


class IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth(object):
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
        'access_id': 'str',
        'k8s_conf_name': 'str',
        'secret_ref': 'IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuthSecretRef',
        'service_account_ref': 'IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuthServiceAccountRef'
    }

    attribute_map = {
        'access_id': 'accessID',
        'k8s_conf_name': 'k8sConfName',
        'secret_ref': 'secretRef',
        'service_account_ref': 'serviceAccountRef'
    }

    def __init__(self, access_id=None, k8s_conf_name=None, secret_ref=None, service_account_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_id = None
        self._k8s_conf_name = None
        self._secret_ref = None
        self._service_account_ref = None
        self.discriminator = None

        self.access_id = access_id
        self.k8s_conf_name = k8s_conf_name
        if secret_ref is not None:
            self.secret_ref = secret_ref
        if service_account_ref is not None:
            self.service_account_ref = service_account_ref

    @property
    def access_id(self):
        """Gets the access_id of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.  # noqa: E501

        the Akeyless Kubernetes auth-method access-id  # noqa: E501

        :return: The access_id of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.  # noqa: E501
        :rtype: str
        """
        return self._access_id

    @access_id.setter
    def access_id(self, access_id):
        """Sets the access_id of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.

        the Akeyless Kubernetes auth-method access-id  # noqa: E501

        :param access_id: The access_id of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and access_id is None:  # noqa: E501
            raise ValueError("Invalid value for `access_id`, must not be `None`")  # noqa: E501

        self._access_id = access_id

    @property
    def k8s_conf_name(self):
        """Gets the k8s_conf_name of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.  # noqa: E501

        Kubernetes-auth configuration name in Akeyless-Gateway  # noqa: E501

        :return: The k8s_conf_name of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.  # noqa: E501
        :rtype: str
        """
        return self._k8s_conf_name

    @k8s_conf_name.setter
    def k8s_conf_name(self, k8s_conf_name):
        """Sets the k8s_conf_name of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.

        Kubernetes-auth configuration name in Akeyless-Gateway  # noqa: E501

        :param k8s_conf_name: The k8s_conf_name of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and k8s_conf_name is None:  # noqa: E501
            raise ValueError("Invalid value for `k8s_conf_name`, must not be `None`")  # noqa: E501

        self._k8s_conf_name = k8s_conf_name

    @property
    def secret_ref(self):
        """Gets the secret_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.  # noqa: E501


        :return: The secret_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.  # noqa: E501
        :rtype: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuthSecretRef
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.


        :param secret_ref: The secret_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.  # noqa: E501
        :type: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuthSecretRef
        """

        self._secret_ref = secret_ref

    @property
    def service_account_ref(self):
        """Gets the service_account_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.  # noqa: E501


        :return: The service_account_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.  # noqa: E501
        :rtype: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuthServiceAccountRef
        """
        return self._service_account_ref

    @service_account_ref.setter
    def service_account_ref(self, service_account_ref):
        """Sets the service_account_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.


        :param service_account_ref: The service_account_ref of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth.  # noqa: E501
        :type: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuthServiceAccountRef
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
        if not isinstance(other, IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth):
            return True

        return self.to_dict() != other.to_dict()
