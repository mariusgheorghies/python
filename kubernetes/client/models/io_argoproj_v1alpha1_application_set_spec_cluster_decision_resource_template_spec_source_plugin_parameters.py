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


class IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters(object):
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
        'array': 'list[str]',
        'map': 'dict(str, str)',
        'name': 'str',
        'string': 'str'
    }

    attribute_map = {
        'array': 'array',
        'map': 'map',
        'name': 'name',
        'string': 'string'
    }

    def __init__(self, array=None, map=None, name=None, string=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._array = None
        self._map = None
        self._name = None
        self._string = None
        self.discriminator = None

        if array is not None:
            self.array = array
        if map is not None:
            self.map = map
        if name is not None:
            self.name = name
        if string is not None:
            self.string = string

    @property
    def array(self):
        """Gets the array of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.  # noqa: E501


        :return: The array of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._array

    @array.setter
    def array(self, array):
        """Sets the array of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.


        :param array: The array of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.  # noqa: E501
        :type: list[str]
        """

        self._array = array

    @property
    def map(self):
        """Gets the map of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.  # noqa: E501


        :return: The map of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.


        :param map: The map of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.  # noqa: E501
        :type: dict(str, str)
        """

        self._map = map

    @property
    def name(self):
        """Gets the name of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.  # noqa: E501


        :return: The name of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.


        :param name: The name of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def string(self):
        """Gets the string of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.  # noqa: E501


        :return: The string of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.  # noqa: E501
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string):
        """Sets the string of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.


        :param string: The string of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters.  # noqa: E501
        :type: str
        """

        self._string = string

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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourcePluginParameters):
            return True

        return self.to_dict() != other.to_dict()
