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


class AwsK8sServicesEc2V1alpha1NATGatewaySpec(object):
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
        'allocation_id': 'str',
        'allocation_ref': 'AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs',
        'connectivity_type': 'str',
        'subnet_id': 'str',
        'subnet_ref': 'AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs',
        'tags': 'list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]'
    }

    attribute_map = {
        'allocation_id': 'allocationID',
        'allocation_ref': 'allocationRef',
        'connectivity_type': 'connectivityType',
        'subnet_id': 'subnetID',
        'subnet_ref': 'subnetRef',
        'tags': 'tags'
    }

    def __init__(self, allocation_id=None, allocation_ref=None, connectivity_type=None, subnet_id=None, subnet_ref=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesEc2V1alpha1NATGatewaySpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allocation_id = None
        self._allocation_ref = None
        self._connectivity_type = None
        self._subnet_id = None
        self._subnet_ref = None
        self._tags = None
        self.discriminator = None

        if allocation_id is not None:
            self.allocation_id = allocation_id
        if allocation_ref is not None:
            self.allocation_ref = allocation_ref
        if connectivity_type is not None:
            self.connectivity_type = connectivity_type
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_ref is not None:
            self.subnet_ref = subnet_ref
        if tags is not None:
            self.tags = tags

    @property
    def allocation_id(self):
        """Gets the allocation_id of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501

        [Public NAT gateways only] The allocation ID of an Elastic IP address to associate with the NAT gateway. You cannot specify an Elastic IP address with a private NAT gateway. If the Elastic IP address is associated with another resource, you must first disassociate it.  # noqa: E501

        :return: The allocation_id of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501
        :rtype: str
        """
        return self._allocation_id

    @allocation_id.setter
    def allocation_id(self, allocation_id):
        """Sets the allocation_id of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.

        [Public NAT gateways only] The allocation ID of an Elastic IP address to associate with the NAT gateway. You cannot specify an Elastic IP address with a private NAT gateway. If the Elastic IP address is associated with another resource, you must first disassociate it.  # noqa: E501

        :param allocation_id: The allocation_id of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501
        :type: str
        """

        self._allocation_id = allocation_id

    @property
    def allocation_ref(self):
        """Gets the allocation_ref of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501


        :return: The allocation_ref of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501
        :rtype: AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs
        """
        return self._allocation_ref

    @allocation_ref.setter
    def allocation_ref(self, allocation_ref):
        """Sets the allocation_ref of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.


        :param allocation_ref: The allocation_ref of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501
        :type: AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs
        """

        self._allocation_ref = allocation_ref

    @property
    def connectivity_type(self):
        """Gets the connectivity_type of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501

        Indicates whether the NAT gateway supports public or private connectivity. The default is public connectivity.  # noqa: E501

        :return: The connectivity_type of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501
        :rtype: str
        """
        return self._connectivity_type

    @connectivity_type.setter
    def connectivity_type(self, connectivity_type):
        """Sets the connectivity_type of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.

        Indicates whether the NAT gateway supports public or private connectivity. The default is public connectivity.  # noqa: E501

        :param connectivity_type: The connectivity_type of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501
        :type: str
        """

        self._connectivity_type = connectivity_type

    @property
    def subnet_id(self):
        """Gets the subnet_id of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501

        The subnet in which to create the NAT gateway.  # noqa: E501

        :return: The subnet_id of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.

        The subnet in which to create the NAT gateway.  # noqa: E501

        :param subnet_id: The subnet_id of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def subnet_ref(self):
        """Gets the subnet_ref of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501


        :return: The subnet_ref of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501
        :rtype: AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs
        """
        return self._subnet_ref

    @subnet_ref.setter
    def subnet_ref(self, subnet_ref):
        """Sets the subnet_ref of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.


        :param subnet_ref: The subnet_ref of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501
        :type: AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs
        """

        self._subnet_ref = subnet_ref

    @property
    def tags(self):
        """Gets the tags of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501

        The tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.  # noqa: E501

        :return: The tags of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.

        The tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.  # noqa: E501

        :param tags: The tags of this AwsK8sServicesEc2V1alpha1NATGatewaySpec.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]
        """

        self._tags = tags

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
        if not isinstance(other, AwsK8sServicesEc2V1alpha1NATGatewaySpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesEc2V1alpha1NATGatewaySpec):
            return True

        return self.to_dict() != other.to_dict()
