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


class DevKopfV1ProvisionerSpec(object):
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
        'cloud_provider': 'str',
        'instance_id': 'str',
        'instance_type': 'str',
        'name': 'str',
        'org_id': 'str',
        'region': 'str',
        'volume_id': 'str'
    }

    attribute_map = {
        'cloud_provider': 'cloudProvider',
        'instance_id': 'instanceId',
        'instance_type': 'instanceType',
        'name': 'name',
        'org_id': 'orgId',
        'region': 'region',
        'volume_id': 'volumeId'
    }

    def __init__(self, cloud_provider=None, instance_id=None, instance_type=None, name=None, org_id=None, region=None, volume_id=None, local_vars_configuration=None):  # noqa: E501
        """DevKopfV1ProvisionerSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_provider = None
        self._instance_id = None
        self._instance_type = None
        self._name = None
        self._org_id = None
        self._region = None
        self._volume_id = None
        self.discriminator = None

        if cloud_provider is not None:
            self.cloud_provider = cloud_provider
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type
        if name is not None:
            self.name = name
        if org_id is not None:
            self.org_id = org_id
        if region is not None:
            self.region = region
        if volume_id is not None:
            self.volume_id = volume_id

    @property
    def cloud_provider(self):
        """Gets the cloud_provider of this DevKopfV1ProvisionerSpec.  # noqa: E501


        :return: The cloud_provider of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :rtype: str
        """
        return self._cloud_provider

    @cloud_provider.setter
    def cloud_provider(self, cloud_provider):
        """Sets the cloud_provider of this DevKopfV1ProvisionerSpec.


        :param cloud_provider: The cloud_provider of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :type: str
        """

        self._cloud_provider = cloud_provider

    @property
    def instance_id(self):
        """Gets the instance_id of this DevKopfV1ProvisionerSpec.  # noqa: E501


        :return: The instance_id of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DevKopfV1ProvisionerSpec.


        :param instance_id: The instance_id of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this DevKopfV1ProvisionerSpec.  # noqa: E501


        :return: The instance_type of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this DevKopfV1ProvisionerSpec.


        :param instance_type: The instance_type of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def name(self):
        """Gets the name of this DevKopfV1ProvisionerSpec.  # noqa: E501


        :return: The name of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DevKopfV1ProvisionerSpec.


        :param name: The name of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this DevKopfV1ProvisionerSpec.  # noqa: E501


        :return: The org_id of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this DevKopfV1ProvisionerSpec.


        :param org_id: The org_id of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def region(self):
        """Gets the region of this DevKopfV1ProvisionerSpec.  # noqa: E501


        :return: The region of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DevKopfV1ProvisionerSpec.


        :param region: The region of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def volume_id(self):
        """Gets the volume_id of this DevKopfV1ProvisionerSpec.  # noqa: E501


        :return: The volume_id of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this DevKopfV1ProvisionerSpec.


        :param volume_id: The volume_id of this DevKopfV1ProvisionerSpec.  # noqa: E501
        :type: str
        """

        self._volume_id = volume_id

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
        if not isinstance(other, DevKopfV1ProvisionerSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DevKopfV1ProvisionerSpec):
            return True

        return self.to_dict() != other.to_dict()