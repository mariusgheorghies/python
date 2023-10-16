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


class AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptions(object):
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
        'market_type': 'str',
        'spot_options': 'AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptionsSpotOptions'
    }

    attribute_map = {
        'market_type': 'marketType',
        'spot_options': 'spotOptions'
    }

    def __init__(self, market_type=None, spot_options=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._market_type = None
        self._spot_options = None
        self.discriminator = None

        if market_type is not None:
            self.market_type = market_type
        if spot_options is not None:
            self.spot_options = spot_options

    @property
    def market_type(self):
        """Gets the market_type of this AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptions.  # noqa: E501


        :return: The market_type of this AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptions.  # noqa: E501
        :rtype: str
        """
        return self._market_type

    @market_type.setter
    def market_type(self, market_type):
        """Sets the market_type of this AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptions.


        :param market_type: The market_type of this AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptions.  # noqa: E501
        :type: str
        """

        self._market_type = market_type

    @property
    def spot_options(self):
        """Gets the spot_options of this AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptions.  # noqa: E501


        :return: The spot_options of this AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptions.  # noqa: E501
        :rtype: AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptionsSpotOptions
        """
        return self._spot_options

    @spot_options.setter
    def spot_options(self, spot_options):
        """Sets the spot_options of this AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptions.


        :param spot_options: The spot_options of this AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptions.  # noqa: E501
        :type: AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptionsSpotOptions
        """

        self._spot_options = spot_options

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
        if not isinstance(other, AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesEc2V1alpha1InstanceSpecInstanceMarketOptions):
            return True

        return self.to_dict() != other.to_dict()
