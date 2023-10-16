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


class IoQuestdbCrdV1alpha1QuestDBCopySpec(object):
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
        'cloud_ids': 'IoQuestdbCrdV1alpha1QuestDBCopySpecCloudIds',
        'copy_instance_type': 'str',
        'destination': 'IoQuestdbCrdV1alpha1QuestDBCopySpecDestination',
        'options': 'IoQuestdbCrdV1alpha1QuestDBCopySpecOptions',
        'source': 'IoQuestdbCrdV1alpha1QuestDBCopySpecSource'
    }

    attribute_map = {
        'cloud_ids': 'cloudIds',
        'copy_instance_type': 'copyInstanceType',
        'destination': 'destination',
        'options': 'options',
        'source': 'source'
    }

    def __init__(self, cloud_ids=None, copy_instance_type=None, destination=None, options=None, source=None, local_vars_configuration=None):  # noqa: E501
        """IoQuestdbCrdV1alpha1QuestDBCopySpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_ids = None
        self._copy_instance_type = None
        self._destination = None
        self._options = None
        self._source = None
        self.discriminator = None

        self.cloud_ids = cloud_ids
        self.copy_instance_type = copy_instance_type
        self.destination = destination
        if options is not None:
            self.options = options
        self.source = source

    @property
    def cloud_ids(self):
        """Gets the cloud_ids of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501


        :return: The cloud_ids of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501
        :rtype: IoQuestdbCrdV1alpha1QuestDBCopySpecCloudIds
        """
        return self._cloud_ids

    @cloud_ids.setter
    def cloud_ids(self, cloud_ids):
        """Sets the cloud_ids of this IoQuestdbCrdV1alpha1QuestDBCopySpec.


        :param cloud_ids: The cloud_ids of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501
        :type: IoQuestdbCrdV1alpha1QuestDBCopySpecCloudIds
        """
        if self.local_vars_configuration.client_side_validation and cloud_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `cloud_ids`, must not be `None`")  # noqa: E501

        self._cloud_ids = cloud_ids

    @property
    def copy_instance_type(self):
        """Gets the copy_instance_type of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501


        :return: The copy_instance_type of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501
        :rtype: str
        """
        return self._copy_instance_type

    @copy_instance_type.setter
    def copy_instance_type(self, copy_instance_type):
        """Sets the copy_instance_type of this IoQuestdbCrdV1alpha1QuestDBCopySpec.


        :param copy_instance_type: The copy_instance_type of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and copy_instance_type is None:  # noqa: E501
            raise ValueError("Invalid value for `copy_instance_type`, must not be `None`")  # noqa: E501

        self._copy_instance_type = copy_instance_type

    @property
    def destination(self):
        """Gets the destination of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501


        :return: The destination of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501
        :rtype: IoQuestdbCrdV1alpha1QuestDBCopySpecDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this IoQuestdbCrdV1alpha1QuestDBCopySpec.


        :param destination: The destination of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501
        :type: IoQuestdbCrdV1alpha1QuestDBCopySpecDestination
        """
        if self.local_vars_configuration.client_side_validation and destination is None:  # noqa: E501
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def options(self):
        """Gets the options of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501


        :return: The options of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501
        :rtype: IoQuestdbCrdV1alpha1QuestDBCopySpecOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this IoQuestdbCrdV1alpha1QuestDBCopySpec.


        :param options: The options of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501
        :type: IoQuestdbCrdV1alpha1QuestDBCopySpecOptions
        """

        self._options = options

    @property
    def source(self):
        """Gets the source of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501


        :return: The source of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501
        :rtype: IoQuestdbCrdV1alpha1QuestDBCopySpecSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this IoQuestdbCrdV1alpha1QuestDBCopySpec.


        :param source: The source of this IoQuestdbCrdV1alpha1QuestDBCopySpec.  # noqa: E501
        :type: IoQuestdbCrdV1alpha1QuestDBCopySpecSource
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

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
        if not isinstance(other, IoQuestdbCrdV1alpha1QuestDBCopySpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoQuestdbCrdV1alpha1QuestDBCopySpec):
            return True

        return self.to_dict() != other.to_dict()