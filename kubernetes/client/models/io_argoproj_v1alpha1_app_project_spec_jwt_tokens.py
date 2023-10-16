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


class IoArgoprojV1alpha1AppProjectSpecJwtTokens(object):
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
        'exp': 'int',
        'iat': 'int',
        'id': 'str'
    }

    attribute_map = {
        'exp': 'exp',
        'iat': 'iat',
        'id': 'id'
    }

    def __init__(self, exp=None, iat=None, id=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1AppProjectSpecJwtTokens - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exp = None
        self._iat = None
        self._id = None
        self.discriminator = None

        if exp is not None:
            self.exp = exp
        self.iat = iat
        if id is not None:
            self.id = id

    @property
    def exp(self):
        """Gets the exp of this IoArgoprojV1alpha1AppProjectSpecJwtTokens.  # noqa: E501


        :return: The exp of this IoArgoprojV1alpha1AppProjectSpecJwtTokens.  # noqa: E501
        :rtype: int
        """
        return self._exp

    @exp.setter
    def exp(self, exp):
        """Sets the exp of this IoArgoprojV1alpha1AppProjectSpecJwtTokens.


        :param exp: The exp of this IoArgoprojV1alpha1AppProjectSpecJwtTokens.  # noqa: E501
        :type: int
        """

        self._exp = exp

    @property
    def iat(self):
        """Gets the iat of this IoArgoprojV1alpha1AppProjectSpecJwtTokens.  # noqa: E501


        :return: The iat of this IoArgoprojV1alpha1AppProjectSpecJwtTokens.  # noqa: E501
        :rtype: int
        """
        return self._iat

    @iat.setter
    def iat(self, iat):
        """Sets the iat of this IoArgoprojV1alpha1AppProjectSpecJwtTokens.


        :param iat: The iat of this IoArgoprojV1alpha1AppProjectSpecJwtTokens.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and iat is None:  # noqa: E501
            raise ValueError("Invalid value for `iat`, must not be `None`")  # noqa: E501

        self._iat = iat

    @property
    def id(self):
        """Gets the id of this IoArgoprojV1alpha1AppProjectSpecJwtTokens.  # noqa: E501


        :return: The id of this IoArgoprojV1alpha1AppProjectSpecJwtTokens.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IoArgoprojV1alpha1AppProjectSpecJwtTokens.


        :param id: The id of this IoArgoprojV1alpha1AppProjectSpecJwtTokens.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, IoArgoprojV1alpha1AppProjectSpecJwtTokens):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1AppProjectSpecJwtTokens):
            return True

        return self.to_dict() != other.to_dict()
