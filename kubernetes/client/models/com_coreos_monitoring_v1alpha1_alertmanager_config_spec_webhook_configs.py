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


class ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs(object):
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
        'http_config': 'ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig',
        'max_alerts': 'int',
        'send_resolved': 'bool',
        'url': 'str',
        'url_secret': 'ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecUrlSecret'
    }

    attribute_map = {
        'http_config': 'httpConfig',
        'max_alerts': 'maxAlerts',
        'send_resolved': 'sendResolved',
        'url': 'url',
        'url_secret': 'urlSecret'
    }

    def __init__(self, http_config=None, max_alerts=None, send_resolved=None, url=None, url_secret=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._http_config = None
        self._max_alerts = None
        self._send_resolved = None
        self._url = None
        self._url_secret = None
        self.discriminator = None

        if http_config is not None:
            self.http_config = http_config
        if max_alerts is not None:
            self.max_alerts = max_alerts
        if send_resolved is not None:
            self.send_resolved = send_resolved
        if url is not None:
            self.url = url
        if url_secret is not None:
            self.url_secret = url_secret

    @property
    def http_config(self):
        """Gets the http_config of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501


        :return: The http_config of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501
        :rtype: ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig
        """
        return self._http_config

    @http_config.setter
    def http_config(self, http_config):
        """Sets the http_config of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.


        :param http_config: The http_config of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501
        :type: ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig
        """

        self._http_config = http_config

    @property
    def max_alerts(self):
        """Gets the max_alerts of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501

        Maximum number of alerts to be sent per webhook message. When 0, all alerts are included.  # noqa: E501

        :return: The max_alerts of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501
        :rtype: int
        """
        return self._max_alerts

    @max_alerts.setter
    def max_alerts(self, max_alerts):
        """Sets the max_alerts of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.

        Maximum number of alerts to be sent per webhook message. When 0, all alerts are included.  # noqa: E501

        :param max_alerts: The max_alerts of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_alerts is not None and max_alerts < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_alerts`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_alerts = max_alerts

    @property
    def send_resolved(self):
        """Gets the send_resolved of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501

        Whether or not to notify about resolved alerts.  # noqa: E501

        :return: The send_resolved of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501
        :rtype: bool
        """
        return self._send_resolved

    @send_resolved.setter
    def send_resolved(self, send_resolved):
        """Sets the send_resolved of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.

        Whether or not to notify about resolved alerts.  # noqa: E501

        :param send_resolved: The send_resolved of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501
        :type: bool
        """

        self._send_resolved = send_resolved

    @property
    def url(self):
        """Gets the url of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501

        The URL to send HTTP POST requests to. `urlSecret` takes precedence over `url`. One of `urlSecret` and `url` should be defined.  # noqa: E501

        :return: The url of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.

        The URL to send HTTP POST requests to. `urlSecret` takes precedence over `url`. One of `urlSecret` and `url` should be defined.  # noqa: E501

        :param url: The url of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def url_secret(self):
        """Gets the url_secret of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501


        :return: The url_secret of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501
        :rtype: ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecUrlSecret
        """
        return self._url_secret

    @url_secret.setter
    def url_secret(self, url_secret):
        """Sets the url_secret of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.


        :param url_secret: The url_secret of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs.  # noqa: E501
        :type: ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecUrlSecret
        """

        self._url_secret = url_secret

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
        if not isinstance(other, ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs):
            return True

        return self.to_dict() != other.to_dict()