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


class IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus(object):
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
        'api_server_elb': 'IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkApiServerElb',
        'security_groups': 'dict(str, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkSecurityGroups)'
    }

    attribute_map = {
        'api_server_elb': 'apiServerElb',
        'security_groups': 'securityGroups'
    }

    def __init__(self, api_server_elb=None, security_groups=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_server_elb = None
        self._security_groups = None
        self.discriminator = None

        if api_server_elb is not None:
            self.api_server_elb = api_server_elb
        if security_groups is not None:
            self.security_groups = security_groups

    @property
    def api_server_elb(self):
        """Gets the api_server_elb of this IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus.  # noqa: E501


        :return: The api_server_elb of this IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus.  # noqa: E501
        :rtype: IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkApiServerElb
        """
        return self._api_server_elb

    @api_server_elb.setter
    def api_server_elb(self, api_server_elb):
        """Sets the api_server_elb of this IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus.


        :param api_server_elb: The api_server_elb of this IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus.  # noqa: E501
        :type: IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkApiServerElb
        """

        self._api_server_elb = api_server_elb

    @property
    def security_groups(self):
        """Gets the security_groups of this IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus.  # noqa: E501

        SecurityGroups is a map from the role/kind of the security group to its unique name, if any.  # noqa: E501

        :return: The security_groups of this IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus.  # noqa: E501
        :rtype: dict(str, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkSecurityGroups)
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus.

        SecurityGroups is a map from the role/kind of the security group to its unique name, if any.  # noqa: E501

        :param security_groups: The security_groups of this IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus.  # noqa: E501
        :type: dict(str, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkSecurityGroups)
        """

        self._security_groups = security_groups

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
        if not isinstance(other, IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus):
            return True

        return self.to_dict() != other.to_dict()
