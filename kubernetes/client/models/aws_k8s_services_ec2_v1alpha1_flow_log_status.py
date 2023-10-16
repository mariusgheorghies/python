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


class AwsK8sServicesEc2V1alpha1FlowLogStatus(object):
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
        'ack_resource_metadata': 'AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata',
        'client_token': 'str',
        'conditions': 'list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]',
        'flow_log_id': 'str',
        'unsuccessful': 'list[AwsK8sServicesEc2V1alpha1FlowLogStatusUnsuccessful]'
    }

    attribute_map = {
        'ack_resource_metadata': 'ackResourceMetadata',
        'client_token': 'clientToken',
        'conditions': 'conditions',
        'flow_log_id': 'flowLogID',
        'unsuccessful': 'unsuccessful'
    }

    def __init__(self, ack_resource_metadata=None, client_token=None, conditions=None, flow_log_id=None, unsuccessful=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesEc2V1alpha1FlowLogStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ack_resource_metadata = None
        self._client_token = None
        self._conditions = None
        self._flow_log_id = None
        self._unsuccessful = None
        self.discriminator = None

        if ack_resource_metadata is not None:
            self.ack_resource_metadata = ack_resource_metadata
        if client_token is not None:
            self.client_token = client_token
        if conditions is not None:
            self.conditions = conditions
        if flow_log_id is not None:
            self.flow_log_id = flow_log_id
        if unsuccessful is not None:
            self.unsuccessful = unsuccessful

    @property
    def ack_resource_metadata(self):
        """Gets the ack_resource_metadata of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501


        :return: The ack_resource_metadata of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501
        :rtype: AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata
        """
        return self._ack_resource_metadata

    @ack_resource_metadata.setter
    def ack_resource_metadata(self, ack_resource_metadata):
        """Sets the ack_resource_metadata of this AwsK8sServicesEc2V1alpha1FlowLogStatus.


        :param ack_resource_metadata: The ack_resource_metadata of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501
        :type: AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata
        """

        self._ack_resource_metadata = ack_resource_metadata

    @property
    def client_token(self):
        """Gets the client_token of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501

        Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  # noqa: E501

        :return: The client_token of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this AwsK8sServicesEc2V1alpha1FlowLogStatus.

        Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  # noqa: E501

        :param client_token: The client_token of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def conditions(self):
        """Gets the conditions of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501

        All CRS managed by ACK have a common `Status.Conditions` member that contains a collection of `ackv1alpha1.Condition` objects that describe the various terminal states of the CR and its backend AWS service API resource  # noqa: E501

        :return: The conditions of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this AwsK8sServicesEc2V1alpha1FlowLogStatus.

        All CRS managed by ACK have a common `Status.Conditions` member that contains a collection of `ackv1alpha1.Condition` objects that describe the various terminal states of the CR and its backend AWS service API resource  # noqa: E501

        :param conditions: The conditions of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]
        """

        self._conditions = conditions

    @property
    def flow_log_id(self):
        """Gets the flow_log_id of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501


        :return: The flow_log_id of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501
        :rtype: str
        """
        return self._flow_log_id

    @flow_log_id.setter
    def flow_log_id(self, flow_log_id):
        """Sets the flow_log_id of this AwsK8sServicesEc2V1alpha1FlowLogStatus.


        :param flow_log_id: The flow_log_id of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501
        :type: str
        """

        self._flow_log_id = flow_log_id

    @property
    def unsuccessful(self):
        """Gets the unsuccessful of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501

        Information about the flow logs that could not be created successfully.  # noqa: E501

        :return: The unsuccessful of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1FlowLogStatusUnsuccessful]
        """
        return self._unsuccessful

    @unsuccessful.setter
    def unsuccessful(self, unsuccessful):
        """Sets the unsuccessful of this AwsK8sServicesEc2V1alpha1FlowLogStatus.

        Information about the flow logs that could not be created successfully.  # noqa: E501

        :param unsuccessful: The unsuccessful of this AwsK8sServicesEc2V1alpha1FlowLogStatus.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1FlowLogStatusUnsuccessful]
        """

        self._unsuccessful = unsuccessful

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
        if not isinstance(other, AwsK8sServicesEc2V1alpha1FlowLogStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesEc2V1alpha1FlowLogStatus):
            return True

        return self.to_dict() != other.to_dict()