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


class IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider(object):
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
        'azure_dev_ops': 'IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderAzureDevOps',
        'bitbucket': 'IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderBitbucket',
        'bitbucket_server': 'IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderBitbucketServer',
        'clone_protocol': 'str',
        'filters': 'list[IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderFilters]',
        'gitea': 'IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGitea',
        'github': 'IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub',
        'gitlab': 'IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGitlab',
        'requeue_after_seconds': 'int',
        'template': 'IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplate'
    }

    attribute_map = {
        'azure_dev_ops': 'azureDevOps',
        'bitbucket': 'bitbucket',
        'bitbucket_server': 'bitbucketServer',
        'clone_protocol': 'cloneProtocol',
        'filters': 'filters',
        'gitea': 'gitea',
        'github': 'github',
        'gitlab': 'gitlab',
        'requeue_after_seconds': 'requeueAfterSeconds',
        'template': 'template'
    }

    def __init__(self, azure_dev_ops=None, bitbucket=None, bitbucket_server=None, clone_protocol=None, filters=None, gitea=None, github=None, gitlab=None, requeue_after_seconds=None, template=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._azure_dev_ops = None
        self._bitbucket = None
        self._bitbucket_server = None
        self._clone_protocol = None
        self._filters = None
        self._gitea = None
        self._github = None
        self._gitlab = None
        self._requeue_after_seconds = None
        self._template = None
        self.discriminator = None

        if azure_dev_ops is not None:
            self.azure_dev_ops = azure_dev_ops
        if bitbucket is not None:
            self.bitbucket = bitbucket
        if bitbucket_server is not None:
            self.bitbucket_server = bitbucket_server
        if clone_protocol is not None:
            self.clone_protocol = clone_protocol
        if filters is not None:
            self.filters = filters
        if gitea is not None:
            self.gitea = gitea
        if github is not None:
            self.github = github
        if gitlab is not None:
            self.gitlab = gitlab
        if requeue_after_seconds is not None:
            self.requeue_after_seconds = requeue_after_seconds
        if template is not None:
            self.template = template

    @property
    def azure_dev_ops(self):
        """Gets the azure_dev_ops of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501


        :return: The azure_dev_ops of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderAzureDevOps
        """
        return self._azure_dev_ops

    @azure_dev_ops.setter
    def azure_dev_ops(self, azure_dev_ops):
        """Sets the azure_dev_ops of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.


        :param azure_dev_ops: The azure_dev_ops of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderAzureDevOps
        """

        self._azure_dev_ops = azure_dev_ops

    @property
    def bitbucket(self):
        """Gets the bitbucket of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501


        :return: The bitbucket of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderBitbucket
        """
        return self._bitbucket

    @bitbucket.setter
    def bitbucket(self, bitbucket):
        """Sets the bitbucket of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.


        :param bitbucket: The bitbucket of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderBitbucket
        """

        self._bitbucket = bitbucket

    @property
    def bitbucket_server(self):
        """Gets the bitbucket_server of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501


        :return: The bitbucket_server of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderBitbucketServer
        """
        return self._bitbucket_server

    @bitbucket_server.setter
    def bitbucket_server(self, bitbucket_server):
        """Sets the bitbucket_server of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.


        :param bitbucket_server: The bitbucket_server of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderBitbucketServer
        """

        self._bitbucket_server = bitbucket_server

    @property
    def clone_protocol(self):
        """Gets the clone_protocol of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501


        :return: The clone_protocol of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :rtype: str
        """
        return self._clone_protocol

    @clone_protocol.setter
    def clone_protocol(self, clone_protocol):
        """Sets the clone_protocol of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.


        :param clone_protocol: The clone_protocol of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :type: str
        """

        self._clone_protocol = clone_protocol

    @property
    def filters(self):
        """Gets the filters of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501


        :return: The filters of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :rtype: list[IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderFilters]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.


        :param filters: The filters of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :type: list[IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderFilters]
        """

        self._filters = filters

    @property
    def gitea(self):
        """Gets the gitea of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501


        :return: The gitea of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGitea
        """
        return self._gitea

    @gitea.setter
    def gitea(self, gitea):
        """Sets the gitea of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.


        :param gitea: The gitea of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGitea
        """

        self._gitea = gitea

    @property
    def github(self):
        """Gets the github of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501


        :return: The github of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub
        """
        return self._github

    @github.setter
    def github(self, github):
        """Sets the github of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.


        :param github: The github of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGithub
        """

        self._github = github

    @property
    def gitlab(self):
        """Gets the gitlab of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501


        :return: The gitlab of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGitlab
        """
        return self._gitlab

    @gitlab.setter
    def gitlab(self, gitlab):
        """Sets the gitlab of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.


        :param gitlab: The gitlab of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProviderGitlab
        """

        self._gitlab = gitlab

    @property
    def requeue_after_seconds(self):
        """Gets the requeue_after_seconds of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501


        :return: The requeue_after_seconds of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :rtype: int
        """
        return self._requeue_after_seconds

    @requeue_after_seconds.setter
    def requeue_after_seconds(self, requeue_after_seconds):
        """Sets the requeue_after_seconds of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.


        :param requeue_after_seconds: The requeue_after_seconds of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :type: int
        """

        self._requeue_after_seconds = requeue_after_seconds

    @property
    def template(self):
        """Gets the template of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501


        :return: The template of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.


        :param template: The template of this IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplate
        """

        self._template = template

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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider):
            return True

        return self.to_dict() != other.to_dict()
