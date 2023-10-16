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


class ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs(object):
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
        'api_key': 'ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecApiKey1',
        'api_url': 'str',
        'custom_fields': 'list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHeaders]',
        'entity_display_name': 'str',
        'http_config': 'ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig1',
        'message_type': 'str',
        'monitoring_tool': 'str',
        'routing_key': 'str',
        'send_resolved': 'bool',
        'state_message': 'str'
    }

    attribute_map = {
        'api_key': 'apiKey',
        'api_url': 'apiUrl',
        'custom_fields': 'customFields',
        'entity_display_name': 'entityDisplayName',
        'http_config': 'httpConfig',
        'message_type': 'messageType',
        'monitoring_tool': 'monitoringTool',
        'routing_key': 'routingKey',
        'send_resolved': 'sendResolved',
        'state_message': 'stateMessage'
    }

    def __init__(self, api_key=None, api_url=None, custom_fields=None, entity_display_name=None, http_config=None, message_type=None, monitoring_tool=None, routing_key=None, send_resolved=None, state_message=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_key = None
        self._api_url = None
        self._custom_fields = None
        self._entity_display_name = None
        self._http_config = None
        self._message_type = None
        self._monitoring_tool = None
        self._routing_key = None
        self._send_resolved = None
        self._state_message = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if api_url is not None:
            self.api_url = api_url
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if entity_display_name is not None:
            self.entity_display_name = entity_display_name
        if http_config is not None:
            self.http_config = http_config
        if message_type is not None:
            self.message_type = message_type
        if monitoring_tool is not None:
            self.monitoring_tool = monitoring_tool
        if routing_key is not None:
            self.routing_key = routing_key
        if send_resolved is not None:
            self.send_resolved = send_resolved
        if state_message is not None:
            self.state_message = state_message

    @property
    def api_key(self):
        """Gets the api_key of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501


        :return: The api_key of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :rtype: ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecApiKey1
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.


        :param api_key: The api_key of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :type: ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecApiKey1
        """

        self._api_key = api_key

    @property
    def api_url(self):
        """Gets the api_url of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501

        The VictorOps API URL.  # noqa: E501

        :return: The api_url of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :rtype: str
        """
        return self._api_url

    @api_url.setter
    def api_url(self, api_url):
        """Sets the api_url of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.

        The VictorOps API URL.  # noqa: E501

        :param api_url: The api_url of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :type: str
        """

        self._api_url = api_url

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501

        Additional custom fields for notification.  # noqa: E501

        :return: The custom_fields of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :rtype: list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHeaders]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.

        Additional custom fields for notification.  # noqa: E501

        :param custom_fields: The custom_fields of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :type: list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHeaders]
        """

        self._custom_fields = custom_fields

    @property
    def entity_display_name(self):
        """Gets the entity_display_name of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501

        Contains summary of the alerted problem.  # noqa: E501

        :return: The entity_display_name of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :rtype: str
        """
        return self._entity_display_name

    @entity_display_name.setter
    def entity_display_name(self, entity_display_name):
        """Sets the entity_display_name of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.

        Contains summary of the alerted problem.  # noqa: E501

        :param entity_display_name: The entity_display_name of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :type: str
        """

        self._entity_display_name = entity_display_name

    @property
    def http_config(self):
        """Gets the http_config of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501


        :return: The http_config of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :rtype: ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig1
        """
        return self._http_config

    @http_config.setter
    def http_config(self, http_config):
        """Sets the http_config of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.


        :param http_config: The http_config of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :type: ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig1
        """

        self._http_config = http_config

    @property
    def message_type(self):
        """Gets the message_type of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501

        Describes the behavior of the alert (CRITICAL, WARNING, INFO).  # noqa: E501

        :return: The message_type of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.

        Describes the behavior of the alert (CRITICAL, WARNING, INFO).  # noqa: E501

        :param message_type: The message_type of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :type: str
        """

        self._message_type = message_type

    @property
    def monitoring_tool(self):
        """Gets the monitoring_tool of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501

        The monitoring tool the state message is from.  # noqa: E501

        :return: The monitoring_tool of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :rtype: str
        """
        return self._monitoring_tool

    @monitoring_tool.setter
    def monitoring_tool(self, monitoring_tool):
        """Sets the monitoring_tool of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.

        The monitoring tool the state message is from.  # noqa: E501

        :param monitoring_tool: The monitoring_tool of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :type: str
        """

        self._monitoring_tool = monitoring_tool

    @property
    def routing_key(self):
        """Gets the routing_key of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501

        A key used to map the alert to a team.  # noqa: E501

        :return: The routing_key of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :rtype: str
        """
        return self._routing_key

    @routing_key.setter
    def routing_key(self, routing_key):
        """Sets the routing_key of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.

        A key used to map the alert to a team.  # noqa: E501

        :param routing_key: The routing_key of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :type: str
        """

        self._routing_key = routing_key

    @property
    def send_resolved(self):
        """Gets the send_resolved of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501

        Whether or not to notify about resolved alerts.  # noqa: E501

        :return: The send_resolved of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :rtype: bool
        """
        return self._send_resolved

    @send_resolved.setter
    def send_resolved(self, send_resolved):
        """Sets the send_resolved of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.

        Whether or not to notify about resolved alerts.  # noqa: E501

        :param send_resolved: The send_resolved of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :type: bool
        """

        self._send_resolved = send_resolved

    @property
    def state_message(self):
        """Gets the state_message of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501

        Contains long explanation of the alerted problem.  # noqa: E501

        :return: The state_message of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """Sets the state_message of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.

        Contains long explanation of the alerted problem.  # noqa: E501

        :param state_message: The state_message of this ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs.  # noqa: E501
        :type: str
        """

        self._state_message = state_message

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
        if not isinstance(other, ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs):
            return True

        return self.to_dict() != other.to_dict()
