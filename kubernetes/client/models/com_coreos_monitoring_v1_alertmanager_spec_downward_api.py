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


class ComCoreosMonitoringV1AlertmanagerSpecDownwardAPI(object):
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
        'default_mode': 'int',
        'items': 'list[ComCoreosMonitoringV1AlertmanagerSpecDownwardAPIItems]'
    }

    attribute_map = {
        'default_mode': 'defaultMode',
        'items': 'items'
    }

    def __init__(self, default_mode=None, items=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1AlertmanagerSpecDownwardAPI - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_mode = None
        self._items = None
        self.discriminator = None

        if default_mode is not None:
            self.default_mode = default_mode
        if items is not None:
            self.items = items

    @property
    def default_mode(self):
        """Gets the default_mode of this ComCoreosMonitoringV1AlertmanagerSpecDownwardAPI.  # noqa: E501

        Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.  # noqa: E501

        :return: The default_mode of this ComCoreosMonitoringV1AlertmanagerSpecDownwardAPI.  # noqa: E501
        :rtype: int
        """
        return self._default_mode

    @default_mode.setter
    def default_mode(self, default_mode):
        """Sets the default_mode of this ComCoreosMonitoringV1AlertmanagerSpecDownwardAPI.

        Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.  # noqa: E501

        :param default_mode: The default_mode of this ComCoreosMonitoringV1AlertmanagerSpecDownwardAPI.  # noqa: E501
        :type: int
        """

        self._default_mode = default_mode

    @property
    def items(self):
        """Gets the items of this ComCoreosMonitoringV1AlertmanagerSpecDownwardAPI.  # noqa: E501

        Items is a list of downward API volume file  # noqa: E501

        :return: The items of this ComCoreosMonitoringV1AlertmanagerSpecDownwardAPI.  # noqa: E501
        :rtype: list[ComCoreosMonitoringV1AlertmanagerSpecDownwardAPIItems]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ComCoreosMonitoringV1AlertmanagerSpecDownwardAPI.

        Items is a list of downward API volume file  # noqa: E501

        :param items: The items of this ComCoreosMonitoringV1AlertmanagerSpecDownwardAPI.  # noqa: E501
        :type: list[ComCoreosMonitoringV1AlertmanagerSpecDownwardAPIItems]
        """

        self._items = items

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
        if not isinstance(other, ComCoreosMonitoringV1AlertmanagerSpecDownwardAPI):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1AlertmanagerSpecDownwardAPI):
            return True

        return self.to_dict() != other.to_dict()
