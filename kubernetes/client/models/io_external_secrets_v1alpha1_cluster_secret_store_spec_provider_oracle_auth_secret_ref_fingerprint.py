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


class IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint(object):
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
        'name': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'namespace': 'namespace'
    }

    def __init__(self, key=None, name=None, namespace=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._name = None
        self._namespace = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace

    @property
    def key(self):
        """Gets the key of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint.  # noqa: E501

        The key of the entry in the Secret resource's `data` field to be used. Some instances of this field may be defaulted, in others it may be required.  # noqa: E501

        :return: The key of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint.

        The key of the entry in the Secret resource's `data` field to be used. Some instances of this field may be defaulted, in others it may be required.  # noqa: E501

        :param key: The key of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint.  # noqa: E501

        The name of the Secret resource being referred to.  # noqa: E501

        :return: The name of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint.

        The name of the Secret resource being referred to.  # noqa: E501

        :param name: The name of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint.  # noqa: E501

        Namespace of the resource being referred to. Ignored if referent is not cluster-scoped. cluster-scoped defaults to the namespace of the referent.  # noqa: E501

        :return: The namespace of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint.

        Namespace of the resource being referred to. Ignored if referent is not cluster-scoped. cluster-scoped defaults to the namespace of the referent.  # noqa: E501

        :param namespace: The namespace of this IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if not isinstance(other, IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRefFingerprint):
            return True

        return self.to_dict() != other.to_dict()
