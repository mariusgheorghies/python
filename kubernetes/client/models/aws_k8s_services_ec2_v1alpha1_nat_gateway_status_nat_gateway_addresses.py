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


class AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses(object):
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
        'network_interface_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str'
    }

    attribute_map = {
        'allocation_id': 'allocationID',
        'network_interface_id': 'networkInterfaceID',
        'private_ip': 'privateIP',
        'public_ip': 'publicIP'
    }

    def __init__(self, allocation_id=None, network_interface_id=None, private_ip=None, public_ip=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allocation_id = None
        self._network_interface_id = None
        self._private_ip = None
        self._public_ip = None
        self.discriminator = None

        if allocation_id is not None:
            self.allocation_id = allocation_id
        if network_interface_id is not None:
            self.network_interface_id = network_interface_id
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip

    @property
    def allocation_id(self):
        """Gets the allocation_id of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.  # noqa: E501


        :return: The allocation_id of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.  # noqa: E501
        :rtype: str
        """
        return self._allocation_id

    @allocation_id.setter
    def allocation_id(self, allocation_id):
        """Sets the allocation_id of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.


        :param allocation_id: The allocation_id of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.  # noqa: E501
        :type: str
        """

        self._allocation_id = allocation_id

    @property
    def network_interface_id(self):
        """Gets the network_interface_id of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.  # noqa: E501


        :return: The network_interface_id of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_id

    @network_interface_id.setter
    def network_interface_id(self, network_interface_id):
        """Sets the network_interface_id of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.


        :param network_interface_id: The network_interface_id of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.  # noqa: E501
        :type: str
        """

        self._network_interface_id = network_interface_id

    @property
    def private_ip(self):
        """Gets the private_ip of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.  # noqa: E501


        :return: The private_ip of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.  # noqa: E501
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.


        :param private_ip: The private_ip of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.  # noqa: E501
        :type: str
        """

        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.  # noqa: E501


        :return: The public_ip of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.  # noqa: E501
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.


        :param public_ip: The public_ip of this AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.  # noqa: E501
        :type: str
        """

        self._public_ip = public_ip

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
        if not isinstance(other, AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses):
            return True

        return self.to_dict() != other.to_dict()