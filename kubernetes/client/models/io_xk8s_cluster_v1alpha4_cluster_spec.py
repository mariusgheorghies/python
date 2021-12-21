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


class IoXK8sClusterV1alpha4ClusterSpec(object):
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
        'cluster_network': 'IoXK8sClusterV1alpha3ClusterSpecClusterNetwork',
        'control_plane_endpoint': 'IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecControlPlaneEndpoint',
        'control_plane_ref': 'IoXK8sClusterV1alpha3ClusterSpecControlPlaneRef',
        'infrastructure_ref': 'IoXK8sClusterV1alpha3ClusterSpecInfrastructureRef',
        'paused': 'bool',
        'topology': 'IoXK8sClusterV1alpha4ClusterSpecTopology'
    }

    attribute_map = {
        'cluster_network': 'clusterNetwork',
        'control_plane_endpoint': 'controlPlaneEndpoint',
        'control_plane_ref': 'controlPlaneRef',
        'infrastructure_ref': 'infrastructureRef',
        'paused': 'paused',
        'topology': 'topology'
    }

    def __init__(self, cluster_network=None, control_plane_endpoint=None, control_plane_ref=None, infrastructure_ref=None, paused=None, topology=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterV1alpha4ClusterSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_network = None
        self._control_plane_endpoint = None
        self._control_plane_ref = None
        self._infrastructure_ref = None
        self._paused = None
        self._topology = None
        self.discriminator = None

        if cluster_network is not None:
            self.cluster_network = cluster_network
        if control_plane_endpoint is not None:
            self.control_plane_endpoint = control_plane_endpoint
        if control_plane_ref is not None:
            self.control_plane_ref = control_plane_ref
        if infrastructure_ref is not None:
            self.infrastructure_ref = infrastructure_ref
        if paused is not None:
            self.paused = paused
        if topology is not None:
            self.topology = topology

    @property
    def cluster_network(self):
        """Gets the cluster_network of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501


        :return: The cluster_network of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501
        :rtype: IoXK8sClusterV1alpha3ClusterSpecClusterNetwork
        """
        return self._cluster_network

    @cluster_network.setter
    def cluster_network(self, cluster_network):
        """Sets the cluster_network of this IoXK8sClusterV1alpha4ClusterSpec.


        :param cluster_network: The cluster_network of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501
        :type: IoXK8sClusterV1alpha3ClusterSpecClusterNetwork
        """

        self._cluster_network = cluster_network

    @property
    def control_plane_endpoint(self):
        """Gets the control_plane_endpoint of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501


        :return: The control_plane_endpoint of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecControlPlaneEndpoint
        """
        return self._control_plane_endpoint

    @control_plane_endpoint.setter
    def control_plane_endpoint(self, control_plane_endpoint):
        """Sets the control_plane_endpoint of this IoXK8sClusterV1alpha4ClusterSpec.


        :param control_plane_endpoint: The control_plane_endpoint of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecControlPlaneEndpoint
        """

        self._control_plane_endpoint = control_plane_endpoint

    @property
    def control_plane_ref(self):
        """Gets the control_plane_ref of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501


        :return: The control_plane_ref of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501
        :rtype: IoXK8sClusterV1alpha3ClusterSpecControlPlaneRef
        """
        return self._control_plane_ref

    @control_plane_ref.setter
    def control_plane_ref(self, control_plane_ref):
        """Sets the control_plane_ref of this IoXK8sClusterV1alpha4ClusterSpec.


        :param control_plane_ref: The control_plane_ref of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501
        :type: IoXK8sClusterV1alpha3ClusterSpecControlPlaneRef
        """

        self._control_plane_ref = control_plane_ref

    @property
    def infrastructure_ref(self):
        """Gets the infrastructure_ref of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501


        :return: The infrastructure_ref of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501
        :rtype: IoXK8sClusterV1alpha3ClusterSpecInfrastructureRef
        """
        return self._infrastructure_ref

    @infrastructure_ref.setter
    def infrastructure_ref(self, infrastructure_ref):
        """Sets the infrastructure_ref of this IoXK8sClusterV1alpha4ClusterSpec.


        :param infrastructure_ref: The infrastructure_ref of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501
        :type: IoXK8sClusterV1alpha3ClusterSpecInfrastructureRef
        """

        self._infrastructure_ref = infrastructure_ref

    @property
    def paused(self):
        """Gets the paused of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501

        Paused can be used to prevent controllers from processing the Cluster and all its associated objects.  # noqa: E501

        :return: The paused of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this IoXK8sClusterV1alpha4ClusterSpec.

        Paused can be used to prevent controllers from processing the Cluster and all its associated objects.  # noqa: E501

        :param paused: The paused of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501
        :type: bool
        """

        self._paused = paused

    @property
    def topology(self):
        """Gets the topology of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501


        :return: The topology of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501
        :rtype: IoXK8sClusterV1alpha4ClusterSpecTopology
        """
        return self._topology

    @topology.setter
    def topology(self, topology):
        """Sets the topology of this IoXK8sClusterV1alpha4ClusterSpec.


        :param topology: The topology of this IoXK8sClusterV1alpha4ClusterSpec.  # noqa: E501
        :type: IoXK8sClusterV1alpha4ClusterSpecTopology
        """

        self._topology = topology

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
        if not isinstance(other, IoXK8sClusterV1alpha4ClusterSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterV1alpha4ClusterSpec):
            return True

        return self.to_dict() != other.to_dict()
