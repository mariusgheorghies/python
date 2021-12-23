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


class IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration(object):
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
        'api_version': 'str',
        'ca_cert_path': 'str',
        'control_plane': 'IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationControlPlane',
        'discovery': 'IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationDiscovery',
        'kind': 'str',
        'node_registration': 'IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistration'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'ca_cert_path': 'caCertPath',
        'control_plane': 'controlPlane',
        'discovery': 'discovery',
        'kind': 'kind',
        'node_registration': 'nodeRegistration'
    }

    def __init__(self, api_version=None, ca_cert_path=None, control_plane=None, discovery=None, kind=None, node_registration=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._ca_cert_path = None
        self._control_plane = None
        self._discovery = None
        self._kind = None
        self._node_registration = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if ca_cert_path is not None:
            self.ca_cert_path = ca_cert_path
        if control_plane is not None:
            self.control_plane = control_plane
        if discovery is not None:
            self.discovery = discovery
        if kind is not None:
            self.kind = kind
        if node_registration is not None:
            self.node_registration = node_registration

    @property
    def api_version(self):
        """Gets the api_version of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def ca_cert_path(self):
        """Gets the ca_cert_path of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501

        CACertPath is the path to the SSL certificate authority used to secure comunications between node and control-plane. Defaults to \"/etc/kubernetes/pki/ca.crt\". TODO: revisit when there is defaulting from k/k  # noqa: E501

        :return: The ca_cert_path of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert_path

    @ca_cert_path.setter
    def ca_cert_path(self, ca_cert_path):
        """Sets the ca_cert_path of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.

        CACertPath is the path to the SSL certificate authority used to secure comunications between node and control-plane. Defaults to \"/etc/kubernetes/pki/ca.crt\". TODO: revisit when there is defaulting from k/k  # noqa: E501

        :param ca_cert_path: The ca_cert_path of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501
        :type: str
        """

        self._ca_cert_path = ca_cert_path

    @property
    def control_plane(self):
        """Gets the control_plane of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501


        :return: The control_plane of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501
        :rtype: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationControlPlane
        """
        return self._control_plane

    @control_plane.setter
    def control_plane(self, control_plane):
        """Sets the control_plane of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.


        :param control_plane: The control_plane of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501
        :type: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationControlPlane
        """

        self._control_plane = control_plane

    @property
    def discovery(self):
        """Gets the discovery of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501


        :return: The discovery of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501
        :rtype: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationDiscovery
        """
        return self._discovery

    @discovery.setter
    def discovery(self, discovery):
        """Sets the discovery of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.


        :param discovery: The discovery of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501
        :type: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationDiscovery
        """

        self._discovery = discovery

    @property
    def kind(self):
        """Gets the kind of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def node_registration(self):
        """Gets the node_registration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501


        :return: The node_registration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501
        :rtype: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistration
        """
        return self._node_registration

    @node_registration.setter
    def node_registration(self, node_registration):
        """Sets the node_registration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.


        :param node_registration: The node_registration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration.  # noqa: E501
        :type: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistration
        """

        self._node_registration = node_registration

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
        if not isinstance(other, IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration):
            return True

        return self.to_dict() != other.to_dict()
