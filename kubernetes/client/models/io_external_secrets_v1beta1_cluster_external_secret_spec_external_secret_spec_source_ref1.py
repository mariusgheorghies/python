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


class IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1(object):
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
        'generator_ref': 'IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRefGeneratorRef',
        'store_ref': 'IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef'
    }

    attribute_map = {
        'generator_ref': 'generatorRef',
        'store_ref': 'storeRef'
    }

    def __init__(self, generator_ref=None, store_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._generator_ref = None
        self._store_ref = None
        self.discriminator = None

        if generator_ref is not None:
            self.generator_ref = generator_ref
        if store_ref is not None:
            self.store_ref = store_ref

    @property
    def generator_ref(self):
        """Gets the generator_ref of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1.  # noqa: E501


        :return: The generator_ref of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1.  # noqa: E501
        :rtype: IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRefGeneratorRef
        """
        return self._generator_ref

    @generator_ref.setter
    def generator_ref(self, generator_ref):
        """Sets the generator_ref of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1.


        :param generator_ref: The generator_ref of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1.  # noqa: E501
        :type: IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRefGeneratorRef
        """

        self._generator_ref = generator_ref

    @property
    def store_ref(self):
        """Gets the store_ref of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1.  # noqa: E501


        :return: The store_ref of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1.  # noqa: E501
        :rtype: IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef
        """
        return self._store_ref

    @store_ref.setter
    def store_ref(self, store_ref):
        """Sets the store_ref of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1.


        :param store_ref: The store_ref of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1.  # noqa: E501
        :type: IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef
        """

        self._store_ref = store_ref

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
        if not isinstance(other, IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1):
            return True

        return self.to_dict() != other.to_dict()
