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


class IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars(object):
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
        'code': 'bool',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, code=None, name=None, value=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._name = None
        self._value = None
        self.discriminator = None

        if code is not None:
            self.code = code
        self.name = name
        self.value = value

    @property
    def code(self):
        """Gets the code of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars.  # noqa: E501


        :return: The code of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars.  # noqa: E501
        :rtype: bool
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars.


        :param code: The code of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars.  # noqa: E501
        :type: bool
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars.  # noqa: E501


        :return: The name of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars.


        :param name: The name of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars.  # noqa: E501


        :return: The value of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars.


        :param value: The value of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectoryJsonnetExtVars):
            return True

        return self.to_dict() != other.to_dict()
