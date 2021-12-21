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


class IoXK8sClusterInfrastructureV1beta1AWSClusterSpec(object):
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
        'additional_tags': 'dict(str, str)',
        'bastion': 'IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecBastion',
        'control_plane_endpoint': 'IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecControlPlaneEndpoint',
        'control_plane_load_balancer': 'IoXK8sClusterInfrastructureV1beta1AWSClusterSpecControlPlaneLoadBalancer',
        'identity_ref': 'IoXK8sClusterInfrastructureV1alpha3AWSClusterSpecIdentityRef',
        'image_lookup_base_os': 'str',
        'image_lookup_format': 'str',
        'image_lookup_org': 'str',
        'network': 'IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpec',
        'region': 'str',
        'ssh_key_name': 'str'
    }

    attribute_map = {
        'additional_tags': 'additionalTags',
        'bastion': 'bastion',
        'control_plane_endpoint': 'controlPlaneEndpoint',
        'control_plane_load_balancer': 'controlPlaneLoadBalancer',
        'identity_ref': 'identityRef',
        'image_lookup_base_os': 'imageLookupBaseOS',
        'image_lookup_format': 'imageLookupFormat',
        'image_lookup_org': 'imageLookupOrg',
        'network': 'network',
        'region': 'region',
        'ssh_key_name': 'sshKeyName'
    }

    def __init__(self, additional_tags=None, bastion=None, control_plane_endpoint=None, control_plane_load_balancer=None, identity_ref=None, image_lookup_base_os=None, image_lookup_format=None, image_lookup_org=None, network=None, region=None, ssh_key_name=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterInfrastructureV1beta1AWSClusterSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._additional_tags = None
        self._bastion = None
        self._control_plane_endpoint = None
        self._control_plane_load_balancer = None
        self._identity_ref = None
        self._image_lookup_base_os = None
        self._image_lookup_format = None
        self._image_lookup_org = None
        self._network = None
        self._region = None
        self._ssh_key_name = None
        self.discriminator = None

        if additional_tags is not None:
            self.additional_tags = additional_tags
        if bastion is not None:
            self.bastion = bastion
        if control_plane_endpoint is not None:
            self.control_plane_endpoint = control_plane_endpoint
        if control_plane_load_balancer is not None:
            self.control_plane_load_balancer = control_plane_load_balancer
        if identity_ref is not None:
            self.identity_ref = identity_ref
        if image_lookup_base_os is not None:
            self.image_lookup_base_os = image_lookup_base_os
        if image_lookup_format is not None:
            self.image_lookup_format = image_lookup_format
        if image_lookup_org is not None:
            self.image_lookup_org = image_lookup_org
        if network is not None:
            self.network = network
        if region is not None:
            self.region = region
        if ssh_key_name is not None:
            self.ssh_key_name = ssh_key_name

    @property
    def additional_tags(self):
        """Gets the additional_tags of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501

        AdditionalTags is an optional set of tags to add to AWS resources managed by the AWS provider, in addition to the ones added by default.  # noqa: E501

        :return: The additional_tags of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._additional_tags

    @additional_tags.setter
    def additional_tags(self, additional_tags):
        """Sets the additional_tags of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.

        AdditionalTags is an optional set of tags to add to AWS resources managed by the AWS provider, in addition to the ones added by default.  # noqa: E501

        :param additional_tags: The additional_tags of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._additional_tags = additional_tags

    @property
    def bastion(self):
        """Gets the bastion of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501


        :return: The bastion of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecBastion
        """
        return self._bastion

    @bastion.setter
    def bastion(self, bastion):
        """Sets the bastion of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.


        :param bastion: The bastion of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecBastion
        """

        self._bastion = bastion

    @property
    def control_plane_endpoint(self):
        """Gets the control_plane_endpoint of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501


        :return: The control_plane_endpoint of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecControlPlaneEndpoint
        """
        return self._control_plane_endpoint

    @control_plane_endpoint.setter
    def control_plane_endpoint(self, control_plane_endpoint):
        """Sets the control_plane_endpoint of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.


        :param control_plane_endpoint: The control_plane_endpoint of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecControlPlaneEndpoint
        """

        self._control_plane_endpoint = control_plane_endpoint

    @property
    def control_plane_load_balancer(self):
        """Gets the control_plane_load_balancer of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501


        :return: The control_plane_load_balancer of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :rtype: IoXK8sClusterInfrastructureV1beta1AWSClusterSpecControlPlaneLoadBalancer
        """
        return self._control_plane_load_balancer

    @control_plane_load_balancer.setter
    def control_plane_load_balancer(self, control_plane_load_balancer):
        """Sets the control_plane_load_balancer of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.


        :param control_plane_load_balancer: The control_plane_load_balancer of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :type: IoXK8sClusterInfrastructureV1beta1AWSClusterSpecControlPlaneLoadBalancer
        """

        self._control_plane_load_balancer = control_plane_load_balancer

    @property
    def identity_ref(self):
        """Gets the identity_ref of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501


        :return: The identity_ref of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :rtype: IoXK8sClusterInfrastructureV1alpha3AWSClusterSpecIdentityRef
        """
        return self._identity_ref

    @identity_ref.setter
    def identity_ref(self, identity_ref):
        """Sets the identity_ref of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.


        :param identity_ref: The identity_ref of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :type: IoXK8sClusterInfrastructureV1alpha3AWSClusterSpecIdentityRef
        """

        self._identity_ref = identity_ref

    @property
    def image_lookup_base_os(self):
        """Gets the image_lookup_base_os of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501

        ImageLookupBaseOS is the name of the base operating system used to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupBaseOS.  # noqa: E501

        :return: The image_lookup_base_os of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_lookup_base_os

    @image_lookup_base_os.setter
    def image_lookup_base_os(self, image_lookup_base_os):
        """Sets the image_lookup_base_os of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.

        ImageLookupBaseOS is the name of the base operating system used to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupBaseOS.  # noqa: E501

        :param image_lookup_base_os: The image_lookup_base_os of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :type: str
        """

        self._image_lookup_base_os = image_lookup_base_os

    @property
    def image_lookup_format(self):
        """Gets the image_lookup_format of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501

        ImageLookupFormat is the AMI naming format to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg. Supports substitutions for {{.BaseOS}} and {{.K8sVersion}} with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami-{{.BaseOS}}-?{{.K8sVersion}}-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/  # noqa: E501

        :return: The image_lookup_format of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_lookup_format

    @image_lookup_format.setter
    def image_lookup_format(self, image_lookup_format):
        """Sets the image_lookup_format of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.

        ImageLookupFormat is the AMI naming format to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg. Supports substitutions for {{.BaseOS}} and {{.K8sVersion}} with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami-{{.BaseOS}}-?{{.K8sVersion}}-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/  # noqa: E501

        :param image_lookup_format: The image_lookup_format of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :type: str
        """

        self._image_lookup_format = image_lookup_format

    @property
    def image_lookup_org(self):
        """Gets the image_lookup_org of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501

        ImageLookupOrg is the AWS Organization ID to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg.  # noqa: E501

        :return: The image_lookup_org of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_lookup_org

    @image_lookup_org.setter
    def image_lookup_org(self, image_lookup_org):
        """Sets the image_lookup_org of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.

        ImageLookupOrg is the AWS Organization ID to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg.  # noqa: E501

        :param image_lookup_org: The image_lookup_org of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :type: str
        """

        self._image_lookup_org = image_lookup_org

    @property
    def network(self):
        """Gets the network of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501


        :return: The network of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpec
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.


        :param network: The network of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpec
        """

        self._network = network

    @property
    def region(self):
        """Gets the region of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501

        The AWS Region the cluster lives in.  # noqa: E501

        :return: The region of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.

        The AWS Region the cluster lives in.  # noqa: E501

        :param region: The region of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def ssh_key_name(self):
        """Gets the ssh_key_name of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501

        SSHKeyName is the name of the ssh key to attach to the bastion host. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name)  # noqa: E501

        :return: The ssh_key_name of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :rtype: str
        """
        return self._ssh_key_name

    @ssh_key_name.setter
    def ssh_key_name(self, ssh_key_name):
        """Sets the ssh_key_name of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.

        SSHKeyName is the name of the ssh key to attach to the bastion host. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name)  # noqa: E501

        :param ssh_key_name: The ssh_key_name of this IoXK8sClusterInfrastructureV1beta1AWSClusterSpec.  # noqa: E501
        :type: str
        """

        self._ssh_key_name = ssh_key_name

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
        if not isinstance(other, IoXK8sClusterInfrastructureV1beta1AWSClusterSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterInfrastructureV1beta1AWSClusterSpec):
            return True

        return self.to_dict() != other.to_dict()
