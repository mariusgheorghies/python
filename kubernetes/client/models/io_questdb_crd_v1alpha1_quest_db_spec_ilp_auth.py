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


class IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth(object):
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
        'kid': 'str',
        'x': 'str',
        'y': 'str'
    }

    attribute_map = {
        'kid': 'kid',
        'x': 'x',
        'y': 'y'
    }

    def __init__(self, kid=None, x=None, y=None, local_vars_configuration=None):  # noqa: E501
        """IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kid = None
        self._x = None
        self._y = None
        self.discriminator = None

        self.kid = kid
        self.x = x
        self.y = y

    @property
    def kid(self):
        """Gets the kid of this IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.  # noqa: E501


        :return: The kid of this IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.  # noqa: E501
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """Sets the kid of this IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.


        :param kid: The kid of this IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and kid is None:  # noqa: E501
            raise ValueError("Invalid value for `kid`, must not be `None`")  # noqa: E501

        self._kid = kid

    @property
    def x(self):
        """Gets the x of this IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.  # noqa: E501


        :return: The x of this IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.  # noqa: E501
        :rtype: str
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.


        :param x: The x of this IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and x is None:  # noqa: E501
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.  # noqa: E501


        :return: The y of this IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.  # noqa: E501
        :rtype: str
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.


        :param y: The y of this IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and y is None:  # noqa: E501
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y

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
        if not isinstance(other, IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth):
            return True

        return self.to_dict() != other.to_dict()