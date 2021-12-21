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


class IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions(object):
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
        'max_price': 'str'
    }

    attribute_map = {
        'max_price': 'maxPrice'
    }

    def __init__(self, max_price=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_price = None
        self.discriminator = None

        if max_price is not None:
            self.max_price = max_price

    @property
    def max_price(self):
        """Gets the max_price of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions.  # noqa: E501

        MaxPrice defines the maximum price the user is willing to pay for Spot VM instances  # noqa: E501

        :return: The max_price of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions.  # noqa: E501
        :rtype: str
        """
        return self._max_price

    @max_price.setter
    def max_price(self, max_price):
        """Sets the max_price of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions.

        MaxPrice defines the maximum price the user is willing to pay for Spot VM instances  # noqa: E501

        :param max_price: The max_price of this IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions.  # noqa: E501
        :type: str
        """

        self._max_price = max_price

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
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions):
            return True

        return self.to_dict() != other.to_dict()
