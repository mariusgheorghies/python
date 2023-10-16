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


class IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuth(object):
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
        'container_auth': 'IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuthContainerAuth',
        'secret_ref': 'IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderIbmAuthSecretRef'
    }

    attribute_map = {
        'container_auth': 'containerAuth',
        'secret_ref': 'secretRef'
    }

    def __init__(self, container_auth=None, secret_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._container_auth = None
        self._secret_ref = None
        self.discriminator = None

        if container_auth is not None:
            self.container_auth = container_auth
        if secret_ref is not None:
            self.secret_ref = secret_ref

    @property
    def container_auth(self):
        """Gets the container_auth of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuth.  # noqa: E501


        :return: The container_auth of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuth.  # noqa: E501
        :rtype: IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuthContainerAuth
        """
        return self._container_auth

    @container_auth.setter
    def container_auth(self, container_auth):
        """Sets the container_auth of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuth.


        :param container_auth: The container_auth of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuth.  # noqa: E501
        :type: IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuthContainerAuth
        """

        self._container_auth = container_auth

    @property
    def secret_ref(self):
        """Gets the secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuth.  # noqa: E501


        :return: The secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuth.  # noqa: E501
        :rtype: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderIbmAuthSecretRef
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuth.


        :param secret_ref: The secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuth.  # noqa: E501
        :type: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderIbmAuthSecretRef
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
        if not isinstance(other, IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderIbmAuth):
            return True

        return self.to_dict() != other.to_dict()