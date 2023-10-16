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


class IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet(object):
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
        'extra_volume_mounts': 'list[ComCoreosMonitoringV1AlertmanagerSpecVolumeMounts]',
        'extra_volumes': 'list[IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetExtraVolumes]'
    }

    attribute_map = {
        'extra_volume_mounts': 'extraVolumeMounts',
        'extra_volumes': 'extraVolumes'
    }

    def __init__(self, extra_volume_mounts=None, extra_volumes=None, local_vars_configuration=None):  # noqa: E501
        """IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._extra_volume_mounts = None
        self._extra_volumes = None
        self.discriminator = None

        if extra_volume_mounts is not None:
            self.extra_volume_mounts = extra_volume_mounts
        if extra_volumes is not None:
            self.extra_volumes = extra_volumes

    @property
    def extra_volume_mounts(self):
        """Gets the extra_volume_mounts of this IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet.  # noqa: E501

        Add additional volume mounts to the QuestDB Pod inside the StatefulSet  # noqa: E501

        :return: The extra_volume_mounts of this IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet.  # noqa: E501
        :rtype: list[ComCoreosMonitoringV1AlertmanagerSpecVolumeMounts]
        """
        return self._extra_volume_mounts

    @extra_volume_mounts.setter
    def extra_volume_mounts(self, extra_volume_mounts):
        """Sets the extra_volume_mounts of this IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet.

        Add additional volume mounts to the QuestDB Pod inside the StatefulSet  # noqa: E501

        :param extra_volume_mounts: The extra_volume_mounts of this IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet.  # noqa: E501
        :type: list[ComCoreosMonitoringV1AlertmanagerSpecVolumeMounts]
        """

        self._extra_volume_mounts = extra_volume_mounts

    @property
    def extra_volumes(self):
        """Gets the extra_volumes of this IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet.  # noqa: E501

        Add additional volumes to the StatefulSet  # noqa: E501

        :return: The extra_volumes of this IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet.  # noqa: E501
        :rtype: list[IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetExtraVolumes]
        """
        return self._extra_volumes

    @extra_volumes.setter
    def extra_volumes(self, extra_volumes):
        """Sets the extra_volumes of this IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet.

        Add additional volumes to the StatefulSet  # noqa: E501

        :param extra_volumes: The extra_volumes of this IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet.  # noqa: E501
        :type: list[IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetExtraVolumes]
        """

        self._extra_volumes = extra_volumes

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
        if not isinstance(other, IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet):
            return True

        return self.to_dict() != other.to_dict()