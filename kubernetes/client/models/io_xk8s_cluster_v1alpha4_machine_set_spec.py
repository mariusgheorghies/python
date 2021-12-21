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


class IoXK8sClusterV1alpha4MachineSetSpec(object):
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
        'cluster_name': 'str',
        'delete_policy': 'str',
        'min_ready_seconds': 'int',
        'replicas': 'int',
        'selector': 'IoXK8sClusterV1alpha3MachineSetSpecSelector',
        'template': 'IoXK8sClusterV1alpha4MachineSetSpecTemplate'
    }

    attribute_map = {
        'cluster_name': 'clusterName',
        'delete_policy': 'deletePolicy',
        'min_ready_seconds': 'minReadySeconds',
        'replicas': 'replicas',
        'selector': 'selector',
        'template': 'template'
    }

    def __init__(self, cluster_name=None, delete_policy=None, min_ready_seconds=None, replicas=None, selector=None, template=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterV1alpha4MachineSetSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_name = None
        self._delete_policy = None
        self._min_ready_seconds = None
        self._replicas = None
        self._selector = None
        self._template = None
        self.discriminator = None

        self.cluster_name = cluster_name
        if delete_policy is not None:
            self.delete_policy = delete_policy
        if min_ready_seconds is not None:
            self.min_ready_seconds = min_ready_seconds
        if replicas is not None:
            self.replicas = replicas
        self.selector = selector
        if template is not None:
            self.template = template

    @property
    def cluster_name(self):
        """Gets the cluster_name of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501

        ClusterName is the name of the Cluster this object belongs to.  # noqa: E501

        :return: The cluster_name of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this IoXK8sClusterV1alpha4MachineSetSpec.

        ClusterName is the name of the Cluster this object belongs to.  # noqa: E501

        :param cluster_name: The cluster_name of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_name is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cluster_name is not None and len(cluster_name) < 1):
            raise ValueError("Invalid value for `cluster_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._cluster_name = cluster_name

    @property
    def delete_policy(self):
        """Gets the delete_policy of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501

        DeletePolicy defines the policy used to identify nodes to delete when downscaling. Defaults to \"Random\".  Valid values are \"Random, \"Newest\", \"Oldest\"  # noqa: E501

        :return: The delete_policy of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501
        :rtype: str
        """
        return self._delete_policy

    @delete_policy.setter
    def delete_policy(self, delete_policy):
        """Sets the delete_policy of this IoXK8sClusterV1alpha4MachineSetSpec.

        DeletePolicy defines the policy used to identify nodes to delete when downscaling. Defaults to \"Random\".  Valid values are \"Random, \"Newest\", \"Oldest\"  # noqa: E501

        :param delete_policy: The delete_policy of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["Random", "Newest", "Oldest"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and delete_policy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `delete_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(delete_policy, allowed_values)
            )

        self._delete_policy = delete_policy

    @property
    def min_ready_seconds(self):
        """Gets the min_ready_seconds of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501

        MinReadySeconds is the minimum number of seconds for which a newly created machine should be ready. Defaults to 0 (machine will be considered available as soon as it is ready)  # noqa: E501

        :return: The min_ready_seconds of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501
        :rtype: int
        """
        return self._min_ready_seconds

    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds):
        """Sets the min_ready_seconds of this IoXK8sClusterV1alpha4MachineSetSpec.

        MinReadySeconds is the minimum number of seconds for which a newly created machine should be ready. Defaults to 0 (machine will be considered available as soon as it is ready)  # noqa: E501

        :param min_ready_seconds: The min_ready_seconds of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501
        :type: int
        """

        self._min_ready_seconds = min_ready_seconds

    @property
    def replicas(self):
        """Gets the replicas of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501

        Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1.  # noqa: E501

        :return: The replicas of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this IoXK8sClusterV1alpha4MachineSetSpec.

        Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1.  # noqa: E501

        :param replicas: The replicas of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def selector(self):
        """Gets the selector of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501


        :return: The selector of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501
        :rtype: IoXK8sClusterV1alpha3MachineSetSpecSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this IoXK8sClusterV1alpha4MachineSetSpec.


        :param selector: The selector of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501
        :type: IoXK8sClusterV1alpha3MachineSetSpecSelector
        """
        if self.local_vars_configuration.client_side_validation and selector is None:  # noqa: E501
            raise ValueError("Invalid value for `selector`, must not be `None`")  # noqa: E501

        self._selector = selector

    @property
    def template(self):
        """Gets the template of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501


        :return: The template of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501
        :rtype: IoXK8sClusterV1alpha4MachineSetSpecTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this IoXK8sClusterV1alpha4MachineSetSpec.


        :param template: The template of this IoXK8sClusterV1alpha4MachineSetSpec.  # noqa: E501
        :type: IoXK8sClusterV1alpha4MachineSetSpecTemplate
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
        if not isinstance(other, IoXK8sClusterV1alpha4MachineSetSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterV1alpha4MachineSetSpec):
            return True

        return self.to_dict() != other.to_dict()
