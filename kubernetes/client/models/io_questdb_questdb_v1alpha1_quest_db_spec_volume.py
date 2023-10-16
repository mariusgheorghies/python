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


class IoQuestdbQuestdbV1alpha1QuestDBSpecVolume(object):
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
        'encrypted': 'bool',
        'iops': 'int',
        'size': 'object',
        'throughput': 'int',
        'type': 'str'
    }

    attribute_map = {
        'encrypted': 'encrypted',
        'iops': 'iops',
        'size': 'size',
        'throughput': 'throughput',
        'type': 'type'
    }

    def __init__(self, encrypted=None, iops=None, size=None, throughput=None, type=None, local_vars_configuration=None):  # noqa: E501
        """IoQuestdbQuestdbV1alpha1QuestDBSpecVolume - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._encrypted = None
        self._iops = None
        self._size = None
        self._throughput = None
        self._type = None
        self.discriminator = None

        if encrypted is not None:
            self.encrypted = encrypted
        if iops is not None:
            self.iops = iops
        self.size = size
        if throughput is not None:
            self.throughput = throughput
        self.type = type

    @property
    def encrypted(self):
        """Gets the encrypted of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501


        :return: The encrypted of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.


        :param encrypted: The encrypted of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501
        :type: bool
        """

        self._encrypted = encrypted

    @property
    def iops(self):
        """Gets the iops of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501


        :return: The iops of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.


        :param iops: The iops of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501
        :type: int
        """

        self._iops = iops

    @property
    def size(self):
        """Gets the size of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501


        :return: The size of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501
        :rtype: object
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.


        :param size: The size of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def throughput(self):
        """Gets the throughput of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501


        :return: The throughput of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """Sets the throughput of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.


        :param throughput: The throughput of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501
        :type: int
        """

        self._throughput = throughput

    @property
    def type(self):
        """Gets the type of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501

        Type can be a proxy for storage class  # noqa: E501

        :return: The type of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.

        Type can be a proxy for storage class  # noqa: E501

        :param type: The type of this IoQuestdbQuestdbV1alpha1QuestDBSpecVolume.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, IoQuestdbQuestdbV1alpha1QuestDBSpecVolume):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoQuestdbQuestdbV1alpha1QuestDBSpecVolume):
            return True

        return self.to_dict() != other.to_dict()
