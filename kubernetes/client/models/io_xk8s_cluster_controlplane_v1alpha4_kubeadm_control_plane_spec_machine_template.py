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


class IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate(object):
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
        'infrastructure_ref': 'IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplateInfrastructureRef',
        'metadata': 'IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplateMetadata',
        'node_drain_timeout': 'str'
    }

    attribute_map = {
        'infrastructure_ref': 'infrastructureRef',
        'metadata': 'metadata',
        'node_drain_timeout': 'nodeDrainTimeout'
    }

    def __init__(self, infrastructure_ref=None, metadata=None, node_drain_timeout=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._infrastructure_ref = None
        self._metadata = None
        self._node_drain_timeout = None
        self.discriminator = None

        self.infrastructure_ref = infrastructure_ref
        if metadata is not None:
            self.metadata = metadata
        if node_drain_timeout is not None:
            self.node_drain_timeout = node_drain_timeout

    @property
    def infrastructure_ref(self):
        """Gets the infrastructure_ref of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.  # noqa: E501


        :return: The infrastructure_ref of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplateInfrastructureRef
        """
        return self._infrastructure_ref

    @infrastructure_ref.setter
    def infrastructure_ref(self, infrastructure_ref):
        """Sets the infrastructure_ref of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.


        :param infrastructure_ref: The infrastructure_ref of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplateInfrastructureRef
        """
        if self.local_vars_configuration.client_side_validation and infrastructure_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `infrastructure_ref`, must not be `None`")  # noqa: E501

        self._infrastructure_ref = infrastructure_ref

    @property
    def metadata(self):
        """Gets the metadata of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.  # noqa: E501


        :return: The metadata of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplateMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.


        :param metadata: The metadata of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplateMetadata
        """

        self._metadata = metadata

    @property
    def node_drain_timeout(self):
        """Gets the node_drain_timeout of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.  # noqa: E501

        NodeDrainTimeout is the total amount of time that the controller will spend on draining a controlplane node The default value is 0, meaning that the node can be drained without any time limitations. NOTE: NodeDrainTimeout is different from `kubectl drain --timeout`  # noqa: E501

        :return: The node_drain_timeout of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.  # noqa: E501
        :rtype: str
        """
        return self._node_drain_timeout

    @node_drain_timeout.setter
    def node_drain_timeout(self, node_drain_timeout):
        """Sets the node_drain_timeout of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.

        NodeDrainTimeout is the total amount of time that the controller will spend on draining a controlplane node The default value is 0, meaning that the node can be drained without any time limitations. NOTE: NodeDrainTimeout is different from `kubectl drain --timeout`  # noqa: E501

        :param node_drain_timeout: The node_drain_timeout of this IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.  # noqa: E501
        :type: str
        """

        self._node_drain_timeout = node_drain_timeout

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
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate):
            return True

        return self.to_dict() != other.to_dict()
