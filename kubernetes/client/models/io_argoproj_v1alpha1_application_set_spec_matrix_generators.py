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


class IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators(object):
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
        'cluster_decision_resource': 'IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResource',
        'clusters': 'IoArgoprojV1alpha1ApplicationSetSpecClusters',
        'git': 'IoArgoprojV1alpha1ApplicationSetSpecGit',
        'list': 'IoArgoprojV1alpha1ApplicationSetSpecList',
        'matrix': 'object',
        'merge': 'object',
        'pull_request': 'IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequest',
        'scm_provider': 'IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider',
        'selector': 'IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceLabelSelector'
    }

    attribute_map = {
        'cluster_decision_resource': 'clusterDecisionResource',
        'clusters': 'clusters',
        'git': 'git',
        'list': 'list',
        'matrix': 'matrix',
        'merge': 'merge',
        'pull_request': 'pullRequest',
        'scm_provider': 'scmProvider',
        'selector': 'selector'
    }

    def __init__(self, cluster_decision_resource=None, clusters=None, git=None, list=None, matrix=None, merge=None, pull_request=None, scm_provider=None, selector=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_decision_resource = None
        self._clusters = None
        self._git = None
        self._list = None
        self._matrix = None
        self._merge = None
        self._pull_request = None
        self._scm_provider = None
        self._selector = None
        self.discriminator = None

        if cluster_decision_resource is not None:
            self.cluster_decision_resource = cluster_decision_resource
        if clusters is not None:
            self.clusters = clusters
        if git is not None:
            self.git = git
        if list is not None:
            self.list = list
        if matrix is not None:
            self.matrix = matrix
        if merge is not None:
            self.merge = merge
        if pull_request is not None:
            self.pull_request = pull_request
        if scm_provider is not None:
            self.scm_provider = scm_provider
        if selector is not None:
            self.selector = selector

    @property
    def cluster_decision_resource(self):
        """Gets the cluster_decision_resource of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501


        :return: The cluster_decision_resource of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResource
        """
        return self._cluster_decision_resource

    @cluster_decision_resource.setter
    def cluster_decision_resource(self, cluster_decision_resource):
        """Sets the cluster_decision_resource of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.


        :param cluster_decision_resource: The cluster_decision_resource of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResource
        """

        self._cluster_decision_resource = cluster_decision_resource

    @property
    def clusters(self):
        """Gets the clusters of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501


        :return: The clusters of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecClusters
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.


        :param clusters: The clusters of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecClusters
        """

        self._clusters = clusters

    @property
    def git(self):
        """Gets the git of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501


        :return: The git of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecGit
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.


        :param git: The git of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecGit
        """

        self._git = git

    @property
    def list(self):
        """Gets the list of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501


        :return: The list of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecList
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.


        :param list: The list of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecList
        """

        self._list = list

    @property
    def matrix(self):
        """Gets the matrix of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501


        :return: The matrix of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :rtype: object
        """
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        """Sets the matrix of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.


        :param matrix: The matrix of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :type: object
        """

        self._matrix = matrix

    @property
    def merge(self):
        """Gets the merge of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501


        :return: The merge of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :rtype: object
        """
        return self._merge

    @merge.setter
    def merge(self, merge):
        """Sets the merge of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.


        :param merge: The merge of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :type: object
        """

        self._merge = merge

    @property
    def pull_request(self):
        """Gets the pull_request of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501


        :return: The pull_request of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequest
        """
        return self._pull_request

    @pull_request.setter
    def pull_request(self, pull_request):
        """Sets the pull_request of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.


        :param pull_request: The pull_request of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecMatrixPullRequest
        """

        self._pull_request = pull_request

    @property
    def scm_provider(self):
        """Gets the scm_provider of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501


        :return: The scm_provider of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider
        """
        return self._scm_provider

    @scm_provider.setter
    def scm_provider(self, scm_provider):
        """Sets the scm_provider of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.


        :param scm_provider: The scm_provider of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecMatrixScmProvider
        """

        self._scm_provider = scm_provider

    @property
    def selector(self):
        """Gets the selector of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501


        :return: The selector of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceLabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.


        :param selector: The selector of this IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceLabelSelector
        """

        self._selector = selector

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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecMatrixGenerators):
            return True

        return self.to_dict() != other.to_dict()
