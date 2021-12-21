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


class ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization(object):
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
        'credentials': 'ComCoreosMonitoringV1PodMonitorSpecAuthorizationCredentials',
        'type': 'str'
    }

    attribute_map = {
        'credentials': 'credentials',
        'type': 'type'
    }

    def __init__(self, credentials=None, type=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._credentials = None
        self._type = None
        self.discriminator = None

        if credentials is not None:
            self.credentials = credentials
        if type is not None:
            self.type = type

    @property
    def credentials(self):
        """Gets the credentials of this ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization.  # noqa: E501


        :return: The credentials of this ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecAuthorizationCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization.


        :param credentials: The credentials of this ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecAuthorizationCredentials
        """

        self._credentials = credentials

    @property
    def type(self):
        """Gets the type of this ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization.  # noqa: E501

        Set the authentication type. Defaults to Bearer, Basic will cause an error  # noqa: E501

        :return: The type of this ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization.

        Set the authentication type. Defaults to Bearer, Basic will cause an error  # noqa: E501

        :param type: The type of this ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization):
            return True

        return self.to_dict() != other.to_dict()
