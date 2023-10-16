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


class OrgProjectcalicoCrdV1IPAMConfigSpec(object):
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
        'auto_allocate_blocks': 'bool',
        'max_blocks_per_host': 'int',
        'strict_affinity': 'bool'
    }

    attribute_map = {
        'auto_allocate_blocks': 'autoAllocateBlocks',
        'max_blocks_per_host': 'maxBlocksPerHost',
        'strict_affinity': 'strictAffinity'
    }

    def __init__(self, auto_allocate_blocks=None, max_blocks_per_host=None, strict_affinity=None, local_vars_configuration=None):  # noqa: E501
        """OrgProjectcalicoCrdV1IPAMConfigSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auto_allocate_blocks = None
        self._max_blocks_per_host = None
        self._strict_affinity = None
        self.discriminator = None

        self.auto_allocate_blocks = auto_allocate_blocks
        if max_blocks_per_host is not None:
            self.max_blocks_per_host = max_blocks_per_host
        self.strict_affinity = strict_affinity

    @property
    def auto_allocate_blocks(self):
        """Gets the auto_allocate_blocks of this OrgProjectcalicoCrdV1IPAMConfigSpec.  # noqa: E501


        :return: The auto_allocate_blocks of this OrgProjectcalicoCrdV1IPAMConfigSpec.  # noqa: E501
        :rtype: bool
        """
        return self._auto_allocate_blocks

    @auto_allocate_blocks.setter
    def auto_allocate_blocks(self, auto_allocate_blocks):
        """Sets the auto_allocate_blocks of this OrgProjectcalicoCrdV1IPAMConfigSpec.


        :param auto_allocate_blocks: The auto_allocate_blocks of this OrgProjectcalicoCrdV1IPAMConfigSpec.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and auto_allocate_blocks is None:  # noqa: E501
            raise ValueError("Invalid value for `auto_allocate_blocks`, must not be `None`")  # noqa: E501

        self._auto_allocate_blocks = auto_allocate_blocks

    @property
    def max_blocks_per_host(self):
        """Gets the max_blocks_per_host of this OrgProjectcalicoCrdV1IPAMConfigSpec.  # noqa: E501

        MaxBlocksPerHost, if non-zero, is the max number of blocks that can be affine to each host.  # noqa: E501

        :return: The max_blocks_per_host of this OrgProjectcalicoCrdV1IPAMConfigSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_blocks_per_host

    @max_blocks_per_host.setter
    def max_blocks_per_host(self, max_blocks_per_host):
        """Sets the max_blocks_per_host of this OrgProjectcalicoCrdV1IPAMConfigSpec.

        MaxBlocksPerHost, if non-zero, is the max number of blocks that can be affine to each host.  # noqa: E501

        :param max_blocks_per_host: The max_blocks_per_host of this OrgProjectcalicoCrdV1IPAMConfigSpec.  # noqa: E501
        :type: int
        """

        self._max_blocks_per_host = max_blocks_per_host

    @property
    def strict_affinity(self):
        """Gets the strict_affinity of this OrgProjectcalicoCrdV1IPAMConfigSpec.  # noqa: E501


        :return: The strict_affinity of this OrgProjectcalicoCrdV1IPAMConfigSpec.  # noqa: E501
        :rtype: bool
        """
        return self._strict_affinity

    @strict_affinity.setter
    def strict_affinity(self, strict_affinity):
        """Sets the strict_affinity of this OrgProjectcalicoCrdV1IPAMConfigSpec.


        :param strict_affinity: The strict_affinity of this OrgProjectcalicoCrdV1IPAMConfigSpec.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and strict_affinity is None:  # noqa: E501
            raise ValueError("Invalid value for `strict_affinity`, must not be `None`")  # noqa: E501

        self._strict_affinity = strict_affinity

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
        if not isinstance(other, OrgProjectcalicoCrdV1IPAMConfigSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrgProjectcalicoCrdV1IPAMConfigSpec):
            return True

        return self.to_dict() != other.to_dict()
