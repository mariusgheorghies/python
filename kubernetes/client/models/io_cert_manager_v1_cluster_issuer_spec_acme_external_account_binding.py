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


class IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding(object):
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
        'key_algorithm': 'str',
        'key_id': 'str',
        'key_secret_ref': 'IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRef'
    }

    attribute_map = {
        'key_algorithm': 'keyAlgorithm',
        'key_id': 'keyID',
        'key_secret_ref': 'keySecretRef'
    }

    def __init__(self, key_algorithm=None, key_id=None, key_secret_ref=None, local_vars_configuration=None):  # noqa: E501
        """IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key_algorithm = None
        self._key_id = None
        self._key_secret_ref = None
        self.discriminator = None

        if key_algorithm is not None:
            self.key_algorithm = key_algorithm
        self.key_id = key_id
        self.key_secret_ref = key_secret_ref

    @property
    def key_algorithm(self):
        """Gets the key_algorithm of this IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.  # noqa: E501

        Deprecated: keyAlgorithm field exists for historical compatibility reasons and should not be used. The algorithm is now hardcoded to HS256 in golang/x/crypto/acme.  # noqa: E501

        :return: The key_algorithm of this IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.  # noqa: E501
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """Sets the key_algorithm of this IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.

        Deprecated: keyAlgorithm field exists for historical compatibility reasons and should not be used. The algorithm is now hardcoded to HS256 in golang/x/crypto/acme.  # noqa: E501

        :param key_algorithm: The key_algorithm of this IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.  # noqa: E501
        :type: str
        """
        allowed_values = ["HS256", "HS384", "HS512"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and key_algorithm not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `key_algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(key_algorithm, allowed_values)
            )

        self._key_algorithm = key_algorithm

    @property
    def key_id(self):
        """Gets the key_id of this IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.  # noqa: E501

        keyID is the ID of the CA key that the External Account is bound to.  # noqa: E501

        :return: The key_id of this IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.  # noqa: E501
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.

        keyID is the ID of the CA key that the External Account is bound to.  # noqa: E501

        :param key_id: The key_id of this IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key_id is None:  # noqa: E501
            raise ValueError("Invalid value for `key_id`, must not be `None`")  # noqa: E501

        self._key_id = key_id

    @property
    def key_secret_ref(self):
        """Gets the key_secret_ref of this IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.  # noqa: E501


        :return: The key_secret_ref of this IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.  # noqa: E501
        :rtype: IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRef
        """
        return self._key_secret_ref

    @key_secret_ref.setter
    def key_secret_ref(self, key_secret_ref):
        """Sets the key_secret_ref of this IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.


        :param key_secret_ref: The key_secret_ref of this IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.  # noqa: E501
        :type: IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRef
        """
        if self.local_vars_configuration.client_side_validation and key_secret_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `key_secret_ref`, must not be `None`")  # noqa: E501

        self._key_secret_ref = key_secret_ref

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
        if not isinstance(other, IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding):
            return True

        return self.to_dict() != other.to_dict()
