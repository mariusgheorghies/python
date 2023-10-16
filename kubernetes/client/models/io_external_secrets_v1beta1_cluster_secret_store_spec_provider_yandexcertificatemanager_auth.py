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


class IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderYandexcertificatemanagerAuth(object):
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
        'authorized_key_secret_ref': 'IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderYandexlockboxAuthAuthorizedKeySecretRef'
    }

    attribute_map = {
        'authorized_key_secret_ref': 'authorizedKeySecretRef'
    }

    def __init__(self, authorized_key_secret_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderYandexcertificatemanagerAuth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authorized_key_secret_ref = None
        self.discriminator = None

        if authorized_key_secret_ref is not None:
            self.authorized_key_secret_ref = authorized_key_secret_ref

    @property
    def authorized_key_secret_ref(self):
        """Gets the authorized_key_secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderYandexcertificatemanagerAuth.  # noqa: E501


        :return: The authorized_key_secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderYandexcertificatemanagerAuth.  # noqa: E501
        :rtype: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderYandexlockboxAuthAuthorizedKeySecretRef
        """
        return self._authorized_key_secret_ref

    @authorized_key_secret_ref.setter
    def authorized_key_secret_ref(self, authorized_key_secret_ref):
        """Sets the authorized_key_secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderYandexcertificatemanagerAuth.


        :param authorized_key_secret_ref: The authorized_key_secret_ref of this IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderYandexcertificatemanagerAuth.  # noqa: E501
        :type: IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderYandexlockboxAuthAuthorizedKeySecretRef
        """

        self._authorized_key_secret_ref = authorized_key_secret_ref

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
        if not isinstance(other, IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderYandexcertificatemanagerAuth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderYandexcertificatemanagerAuth):
            return True

        return self.to_dict() != other.to_dict()
