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


class IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFromSecret(object):
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
        'key': 'str',
        'name': 'str'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name'
    }

    def __init__(self, key=None, name=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFromSecret - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._name = None
        self.discriminator = None

        self.key = key
        self.name = name

    @property
    def key(self):
        """Gets the key of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFromSecret.  # noqa: E501

        Key is the key in the secret's data map for this value.  # noqa: E501

        :return: The key of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFromSecret.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFromSecret.

        Key is the key in the secret's data map for this value.  # noqa: E501

        :param key: The key of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFromSecret.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def name(self):
        """Gets the name of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFromSecret.  # noqa: E501

        Name of the secret in the KubeadmBootstrapConfig's namespace to use.  # noqa: E501

        :return: The name of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFromSecret.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFromSecret.

        Name of the secret in the KubeadmBootstrapConfig's namespace to use.  # noqa: E501

        :param name: The name of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFromSecret.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFromSecret):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFromSecret):
            return True

        return self.to_dict() != other.to_dict()
