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


class IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec(object):
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
        'destination': 'IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecDestination',
        'ignore_differences': 'list[IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecIgnoreDifferences]',
        'info': 'list[IoArgoprojV1alpha1ApplicationOperationInfo]',
        'project': 'str',
        'revision_history_limit': 'int',
        'source': 'IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSource',
        'sources': 'list[IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSource]',
        'sync_policy': 'IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSyncPolicy'
    }

    attribute_map = {
        'destination': 'destination',
        'ignore_differences': 'ignoreDifferences',
        'info': 'info',
        'project': 'project',
        'revision_history_limit': 'revisionHistoryLimit',
        'source': 'source',
        'sources': 'sources',
        'sync_policy': 'syncPolicy'
    }

    def __init__(self, destination=None, ignore_differences=None, info=None, project=None, revision_history_limit=None, source=None, sources=None, sync_policy=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._destination = None
        self._ignore_differences = None
        self._info = None
        self._project = None
        self._revision_history_limit = None
        self._source = None
        self._sources = None
        self._sync_policy = None
        self.discriminator = None

        self.destination = destination
        if ignore_differences is not None:
            self.ignore_differences = ignore_differences
        if info is not None:
            self.info = info
        self.project = project
        if revision_history_limit is not None:
            self.revision_history_limit = revision_history_limit
        if source is not None:
            self.source = source
        if sources is not None:
            self.sources = sources
        if sync_policy is not None:
            self.sync_policy = sync_policy

    @property
    def destination(self):
        """Gets the destination of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501


        :return: The destination of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.


        :param destination: The destination of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecDestination
        """
        if self.local_vars_configuration.client_side_validation and destination is None:  # noqa: E501
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def ignore_differences(self):
        """Gets the ignore_differences of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501


        :return: The ignore_differences of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :rtype: list[IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecIgnoreDifferences]
        """
        return self._ignore_differences

    @ignore_differences.setter
    def ignore_differences(self, ignore_differences):
        """Sets the ignore_differences of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.


        :param ignore_differences: The ignore_differences of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :type: list[IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecIgnoreDifferences]
        """

        self._ignore_differences = ignore_differences

    @property
    def info(self):
        """Gets the info of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501


        :return: The info of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :rtype: list[IoArgoprojV1alpha1ApplicationOperationInfo]
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.


        :param info: The info of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :type: list[IoArgoprojV1alpha1ApplicationOperationInfo]
        """

        self._info = info

    @property
    def project(self):
        """Gets the project of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501


        :return: The project of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.


        :param project: The project of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and project is None:  # noqa: E501
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def revision_history_limit(self):
        """Gets the revision_history_limit of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501


        :return: The revision_history_limit of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :rtype: int
        """
        return self._revision_history_limit

    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit):
        """Sets the revision_history_limit of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.


        :param revision_history_limit: The revision_history_limit of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :type: int
        """

        self._revision_history_limit = revision_history_limit

    @property
    def source(self):
        """Gets the source of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501


        :return: The source of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.


        :param source: The source of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSource
        """

        self._source = source

    @property
    def sources(self):
        """Gets the sources of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501


        :return: The sources of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :rtype: list[IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSource]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.


        :param sources: The sources of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :type: list[IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSource]
        """

        self._sources = sources

    @property
    def sync_policy(self):
        """Gets the sync_policy of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501


        :return: The sync_policy of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSyncPolicy
        """
        return self._sync_policy

    @sync_policy.setter
    def sync_policy(self, sync_policy):
        """Sets the sync_policy of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.


        :param sync_policy: The sync_policy of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSyncPolicy
        """

        self._sync_policy = sync_policy

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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpec):
            return True

        return self.to_dict() != other.to_dict()