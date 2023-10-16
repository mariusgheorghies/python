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


class IoArgoprojV1alpha1ApplicationSpecSyncPolicy(object):
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
        'automated': 'IoArgoprojV1alpha1ApplicationSpecSyncPolicyAutomated',
        'managed_namespace_metadata': 'IoArgoprojV1alpha1ApplicationSpecSyncPolicyManagedNamespaceMetadata',
        'retry': 'IoArgoprojV1alpha1ApplicationSpecSyncPolicyRetry',
        'sync_options': 'list[str]'
    }

    attribute_map = {
        'automated': 'automated',
        'managed_namespace_metadata': 'managedNamespaceMetadata',
        'retry': 'retry',
        'sync_options': 'syncOptions'
    }

    def __init__(self, automated=None, managed_namespace_metadata=None, retry=None, sync_options=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationSpecSyncPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._automated = None
        self._managed_namespace_metadata = None
        self._retry = None
        self._sync_options = None
        self.discriminator = None

        if automated is not None:
            self.automated = automated
        if managed_namespace_metadata is not None:
            self.managed_namespace_metadata = managed_namespace_metadata
        if retry is not None:
            self.retry = retry
        if sync_options is not None:
            self.sync_options = sync_options

    @property
    def automated(self):
        """Gets the automated of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.  # noqa: E501


        :return: The automated of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSpecSyncPolicyAutomated
        """
        return self._automated

    @automated.setter
    def automated(self, automated):
        """Sets the automated of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.


        :param automated: The automated of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSpecSyncPolicyAutomated
        """

        self._automated = automated

    @property
    def managed_namespace_metadata(self):
        """Gets the managed_namespace_metadata of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.  # noqa: E501


        :return: The managed_namespace_metadata of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSpecSyncPolicyManagedNamespaceMetadata
        """
        return self._managed_namespace_metadata

    @managed_namespace_metadata.setter
    def managed_namespace_metadata(self, managed_namespace_metadata):
        """Sets the managed_namespace_metadata of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.


        :param managed_namespace_metadata: The managed_namespace_metadata of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSpecSyncPolicyManagedNamespaceMetadata
        """

        self._managed_namespace_metadata = managed_namespace_metadata

    @property
    def retry(self):
        """Gets the retry of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.  # noqa: E501


        :return: The retry of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSpecSyncPolicyRetry
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        """Sets the retry of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.


        :param retry: The retry of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSpecSyncPolicyRetry
        """

        self._retry = retry

    @property
    def sync_options(self):
        """Gets the sync_options of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.  # noqa: E501

        Options allow you to specify whole app sync-options  # noqa: E501

        :return: The sync_options of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._sync_options

    @sync_options.setter
    def sync_options(self, sync_options):
        """Sets the sync_options of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.

        Options allow you to specify whole app sync-options  # noqa: E501

        :param sync_options: The sync_options of this IoArgoprojV1alpha1ApplicationSpecSyncPolicy.  # noqa: E501
        :type: list[str]
        """

        self._sync_options = sync_options

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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSpecSyncPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSpecSyncPolicy):
            return True

        return self.to_dict() != other.to_dict()
