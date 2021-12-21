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


class IoXK8sClusterV1alpha4MachinePoolSpec(object):
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
        'failure_domains': 'list[str]',
        'min_ready_seconds': 'int',
        'provider_id_list': 'list[str]',
        'replicas': 'int',
        'template': 'IoXK8sClusterV1alpha4MachineDeploymentSpecTemplate'
    }

    attribute_map = {
        'cluster_name': 'clusterName',
        'failure_domains': 'failureDomains',
        'min_ready_seconds': 'minReadySeconds',
        'provider_id_list': 'providerIDList',
        'replicas': 'replicas',
        'template': 'template'
    }

    def __init__(self, cluster_name=None, failure_domains=None, min_ready_seconds=None, provider_id_list=None, replicas=None, template=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterV1alpha4MachinePoolSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_name = None
        self._failure_domains = None
        self._min_ready_seconds = None
        self._provider_id_list = None
        self._replicas = None
        self._template = None
        self.discriminator = None

        self.cluster_name = cluster_name
        if failure_domains is not None:
            self.failure_domains = failure_domains
        if min_ready_seconds is not None:
            self.min_ready_seconds = min_ready_seconds
        if provider_id_list is not None:
            self.provider_id_list = provider_id_list
        if replicas is not None:
            self.replicas = replicas
        self.template = template

    @property
    def cluster_name(self):
        """Gets the cluster_name of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501

        ClusterName is the name of the Cluster this object belongs to.  # noqa: E501

        :return: The cluster_name of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this IoXK8sClusterV1alpha4MachinePoolSpec.

        ClusterName is the name of the Cluster this object belongs to.  # noqa: E501

        :param cluster_name: The cluster_name of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_name is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cluster_name is not None and len(cluster_name) < 1):
            raise ValueError("Invalid value for `cluster_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._cluster_name = cluster_name

    @property
    def failure_domains(self):
        """Gets the failure_domains of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501

        FailureDomains is the list of failure domains this MachinePool should be attached to.  # noqa: E501

        :return: The failure_domains of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._failure_domains

    @failure_domains.setter
    def failure_domains(self, failure_domains):
        """Sets the failure_domains of this IoXK8sClusterV1alpha4MachinePoolSpec.

        FailureDomains is the list of failure domains this MachinePool should be attached to.  # noqa: E501

        :param failure_domains: The failure_domains of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501
        :type: list[str]
        """

        self._failure_domains = failure_domains

    @property
    def min_ready_seconds(self):
        """Gets the min_ready_seconds of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501

        Minimum number of seconds for which a newly created machine instances should be ready. Defaults to 0 (machine instance will be considered available as soon as it is ready)  # noqa: E501

        :return: The min_ready_seconds of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501
        :rtype: int
        """
        return self._min_ready_seconds

    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds):
        """Sets the min_ready_seconds of this IoXK8sClusterV1alpha4MachinePoolSpec.

        Minimum number of seconds for which a newly created machine instances should be ready. Defaults to 0 (machine instance will be considered available as soon as it is ready)  # noqa: E501

        :param min_ready_seconds: The min_ready_seconds of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501
        :type: int
        """

        self._min_ready_seconds = min_ready_seconds

    @property
    def provider_id_list(self):
        """Gets the provider_id_list of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501

        ProviderIDList are the identification IDs of machine instances provided by the provider. This field must match the provider IDs as seen on the node objects corresponding to a machine pool's machine instances.  # noqa: E501

        :return: The provider_id_list of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._provider_id_list

    @provider_id_list.setter
    def provider_id_list(self, provider_id_list):
        """Sets the provider_id_list of this IoXK8sClusterV1alpha4MachinePoolSpec.

        ProviderIDList are the identification IDs of machine instances provided by the provider. This field must match the provider IDs as seen on the node objects corresponding to a machine pool's machine instances.  # noqa: E501

        :param provider_id_list: The provider_id_list of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501
        :type: list[str]
        """

        self._provider_id_list = provider_id_list

    @property
    def replicas(self):
        """Gets the replicas of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501

        Number of desired machines. Defaults to 1. This is a pointer to distinguish between explicit zero and not specified.  # noqa: E501

        :return: The replicas of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this IoXK8sClusterV1alpha4MachinePoolSpec.

        Number of desired machines. Defaults to 1. This is a pointer to distinguish between explicit zero and not specified.  # noqa: E501

        :param replicas: The replicas of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def template(self):
        """Gets the template of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501


        :return: The template of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501
        :rtype: IoXK8sClusterV1alpha4MachineDeploymentSpecTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this IoXK8sClusterV1alpha4MachinePoolSpec.


        :param template: The template of this IoXK8sClusterV1alpha4MachinePoolSpec.  # noqa: E501
        :type: IoXK8sClusterV1alpha4MachineDeploymentSpecTemplate
        """
        if self.local_vars_configuration.client_side_validation and template is None:  # noqa: E501
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, IoXK8sClusterV1alpha4MachinePoolSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterV1alpha4MachinePoolSpec):
            return True

        return self.to_dict() != other.to_dict()
