# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class ComCoreosMonitoringV1AlertmanagerStatus(object):
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
        'available_replicas': 'int',
        'paused': 'bool',
        'replicas': 'int',
        'unavailable_replicas': 'int',
        'updated_replicas': 'int'
    }

    attribute_map = {
        'available_replicas': 'availableReplicas',
        'paused': 'paused',
        'replicas': 'replicas',
        'unavailable_replicas': 'unavailableReplicas',
        'updated_replicas': 'updatedReplicas'
    }

    def __init__(self, available_replicas=None, paused=None, replicas=None, unavailable_replicas=None, updated_replicas=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1AlertmanagerStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._available_replicas = None
        self._paused = None
        self._replicas = None
        self._unavailable_replicas = None
        self._updated_replicas = None
        self.discriminator = None

        self.available_replicas = available_replicas
        self.paused = paused
        self.replicas = replicas
        self.unavailable_replicas = unavailable_replicas
        self.updated_replicas = updated_replicas

    @property
    def available_replicas(self):
        """Gets the available_replicas of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501

        Total number of available pods (ready for at least minReadySeconds) targeted by this Alertmanager cluster.  # noqa: E501

        :return: The available_replicas of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501
        :rtype: int
        """
        return self._available_replicas

    @available_replicas.setter
    def available_replicas(self, available_replicas):
        """Sets the available_replicas of this ComCoreosMonitoringV1AlertmanagerStatus.

        Total number of available pods (ready for at least minReadySeconds) targeted by this Alertmanager cluster.  # noqa: E501

        :param available_replicas: The available_replicas of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and available_replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `available_replicas`, must not be `None`")  # noqa: E501

        self._available_replicas = available_replicas

    @property
    def paused(self):
        """Gets the paused of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501

        Represents whether any actions on the underlying managed objects are being performed. Only delete actions will be performed.  # noqa: E501

        :return: The paused of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this ComCoreosMonitoringV1AlertmanagerStatus.

        Represents whether any actions on the underlying managed objects are being performed. Only delete actions will be performed.  # noqa: E501

        :param paused: The paused of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and paused is None:  # noqa: E501
            raise ValueError("Invalid value for `paused`, must not be `None`")  # noqa: E501

        self._paused = paused

    @property
    def replicas(self):
        """Gets the replicas of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501

        Total number of non-terminated pods targeted by this Alertmanager cluster (their labels match the selector).  # noqa: E501

        :return: The replicas of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this ComCoreosMonitoringV1AlertmanagerStatus.

        Total number of non-terminated pods targeted by this Alertmanager cluster (their labels match the selector).  # noqa: E501

        :param replicas: The replicas of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `replicas`, must not be `None`")  # noqa: E501

        self._replicas = replicas

    @property
    def unavailable_replicas(self):
        """Gets the unavailable_replicas of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501

        Total number of unavailable pods targeted by this Alertmanager cluster.  # noqa: E501

        :return: The unavailable_replicas of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501
        :rtype: int
        """
        return self._unavailable_replicas

    @unavailable_replicas.setter
    def unavailable_replicas(self, unavailable_replicas):
        """Sets the unavailable_replicas of this ComCoreosMonitoringV1AlertmanagerStatus.

        Total number of unavailable pods targeted by this Alertmanager cluster.  # noqa: E501

        :param unavailable_replicas: The unavailable_replicas of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and unavailable_replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `unavailable_replicas`, must not be `None`")  # noqa: E501

        self._unavailable_replicas = unavailable_replicas

    @property
    def updated_replicas(self):
        """Gets the updated_replicas of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501

        Total number of non-terminated pods targeted by this Alertmanager cluster that have the desired version spec.  # noqa: E501

        :return: The updated_replicas of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501
        :rtype: int
        """
        return self._updated_replicas

    @updated_replicas.setter
    def updated_replicas(self, updated_replicas):
        """Sets the updated_replicas of this ComCoreosMonitoringV1AlertmanagerStatus.

        Total number of non-terminated pods targeted by this Alertmanager cluster that have the desired version spec.  # noqa: E501

        :param updated_replicas: The updated_replicas of this ComCoreosMonitoringV1AlertmanagerStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and updated_replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_replicas`, must not be `None`")  # noqa: E501

        self._updated_replicas = updated_replicas

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
        if not isinstance(other, ComCoreosMonitoringV1AlertmanagerStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1AlertmanagerStatus):
            return True

        return self.to_dict() != other.to_dict()
