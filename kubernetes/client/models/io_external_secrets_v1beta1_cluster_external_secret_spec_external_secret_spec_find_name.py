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


class IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFindName(object):
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
        'regexp': 'str'
    }

    attribute_map = {
        'regexp': 'regexp'
    }

    def __init__(self, regexp=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFindName - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._regexp = None
        self.discriminator = None

        if regexp is not None:
            self.regexp = regexp

    @property
    def regexp(self):
        """Gets the regexp of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFindName.  # noqa: E501

        Finds secrets base  # noqa: E501

        :return: The regexp of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFindName.  # noqa: E501
        :rtype: str
        """
        return self._regexp

    @regexp.setter
    def regexp(self, regexp):
        """Sets the regexp of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFindName.

        Finds secrets base  # noqa: E501

        :param regexp: The regexp of this IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFindName.  # noqa: E501
        :type: str
        """

        self._regexp = regexp

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
        if not isinstance(other, IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFindName):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFindName):
            return True

        return self.to_dict() != other.to_dict()
