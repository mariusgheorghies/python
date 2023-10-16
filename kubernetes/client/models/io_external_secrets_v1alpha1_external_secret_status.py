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


class IoExternalSecretsV1alpha1ExternalSecretStatus(object):
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
        'conditions': 'list[IoExternalSecretsV1alpha1ClusterSecretStoreStatusConditions]',
        'refresh_time': 'object',
        'synced_resource_version': 'str'
    }

    attribute_map = {
        'conditions': 'conditions',
        'refresh_time': 'refreshTime',
        'synced_resource_version': 'syncedResourceVersion'
    }

    def __init__(self, conditions=None, refresh_time=None, synced_resource_version=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsV1alpha1ExternalSecretStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._refresh_time = None
        self._synced_resource_version = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if refresh_time is not None:
            self.refresh_time = refresh_time
        if synced_resource_version is not None:
            self.synced_resource_version = synced_resource_version

    @property
    def conditions(self):
        """Gets the conditions of this IoExternalSecretsV1alpha1ExternalSecretStatus.  # noqa: E501


        :return: The conditions of this IoExternalSecretsV1alpha1ExternalSecretStatus.  # noqa: E501
        :rtype: list[IoExternalSecretsV1alpha1ClusterSecretStoreStatusConditions]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this IoExternalSecretsV1alpha1ExternalSecretStatus.


        :param conditions: The conditions of this IoExternalSecretsV1alpha1ExternalSecretStatus.  # noqa: E501
        :type: list[IoExternalSecretsV1alpha1ClusterSecretStoreStatusConditions]
        """

        self._conditions = conditions

    @property
    def refresh_time(self):
        """Gets the refresh_time of this IoExternalSecretsV1alpha1ExternalSecretStatus.  # noqa: E501

        refreshTime is the time and date the external secret was fetched and the target secret updated  # noqa: E501

        :return: The refresh_time of this IoExternalSecretsV1alpha1ExternalSecretStatus.  # noqa: E501
        :rtype: object
        """
        return self._refresh_time

    @refresh_time.setter
    def refresh_time(self, refresh_time):
        """Sets the refresh_time of this IoExternalSecretsV1alpha1ExternalSecretStatus.

        refreshTime is the time and date the external secret was fetched and the target secret updated  # noqa: E501

        :param refresh_time: The refresh_time of this IoExternalSecretsV1alpha1ExternalSecretStatus.  # noqa: E501
        :type: object
        """

        self._refresh_time = refresh_time

    @property
    def synced_resource_version(self):
        """Gets the synced_resource_version of this IoExternalSecretsV1alpha1ExternalSecretStatus.  # noqa: E501

        SyncedResourceVersion keeps track of the last synced version  # noqa: E501

        :return: The synced_resource_version of this IoExternalSecretsV1alpha1ExternalSecretStatus.  # noqa: E501
        :rtype: str
        """
        return self._synced_resource_version

    @synced_resource_version.setter
    def synced_resource_version(self, synced_resource_version):
        """Sets the synced_resource_version of this IoExternalSecretsV1alpha1ExternalSecretStatus.

        SyncedResourceVersion keeps track of the last synced version  # noqa: E501

        :param synced_resource_version: The synced_resource_version of this IoExternalSecretsV1alpha1ExternalSecretStatus.  # noqa: E501
        :type: str
        """

        self._synced_resource_version = synced_resource_version

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
        if not isinstance(other, IoExternalSecretsV1alpha1ExternalSecretStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsV1alpha1ExternalSecretStatus):
            return True

        return self.to_dict() != other.to_dict()
