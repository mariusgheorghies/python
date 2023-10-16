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


class IoArgoprojV1alpha1ApplicationStatusOperationState(object):
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
        'finished_at': 'datetime',
        'message': 'str',
        'operation': 'IoArgoprojV1alpha1ApplicationStatusOperationStateOperation',
        'phase': 'str',
        'retry_count': 'int',
        'started_at': 'datetime',
        'sync_result': 'IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResult'
    }

    attribute_map = {
        'finished_at': 'finishedAt',
        'message': 'message',
        'operation': 'operation',
        'phase': 'phase',
        'retry_count': 'retryCount',
        'started_at': 'startedAt',
        'sync_result': 'syncResult'
    }

    def __init__(self, finished_at=None, message=None, operation=None, phase=None, retry_count=None, started_at=None, sync_result=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationStatusOperationState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._finished_at = None
        self._message = None
        self._operation = None
        self._phase = None
        self._retry_count = None
        self._started_at = None
        self._sync_result = None
        self.discriminator = None

        if finished_at is not None:
            self.finished_at = finished_at
        if message is not None:
            self.message = message
        self.operation = operation
        self.phase = phase
        if retry_count is not None:
            self.retry_count = retry_count
        self.started_at = started_at
        if sync_result is not None:
            self.sync_result = sync_result

    @property
    def finished_at(self):
        """Gets the finished_at of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501

        FinishedAt contains time of operation completion  # noqa: E501

        :return: The finished_at of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this IoArgoprojV1alpha1ApplicationStatusOperationState.

        FinishedAt contains time of operation completion  # noqa: E501

        :param finished_at: The finished_at of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def message(self):
        """Gets the message of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501

        Message holds any pertinent messages when attempting to perform operation (typically errors).  # noqa: E501

        :return: The message of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this IoArgoprojV1alpha1ApplicationStatusOperationState.

        Message holds any pertinent messages when attempting to perform operation (typically errors).  # noqa: E501

        :param message: The message of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def operation(self):
        """Gets the operation of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501


        :return: The operation of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationStatusOperationStateOperation
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this IoArgoprojV1alpha1ApplicationStatusOperationState.


        :param operation: The operation of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationStatusOperationStateOperation
        """
        if self.local_vars_configuration.client_side_validation and operation is None:  # noqa: E501
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def phase(self):
        """Gets the phase of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501

        Phase is the current phase of the operation  # noqa: E501

        :return: The phase of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this IoArgoprojV1alpha1ApplicationStatusOperationState.

        Phase is the current phase of the operation  # noqa: E501

        :param phase: The phase of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and phase is None:  # noqa: E501
            raise ValueError("Invalid value for `phase`, must not be `None`")  # noqa: E501

        self._phase = phase

    @property
    def retry_count(self):
        """Gets the retry_count of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501

        RetryCount contains time of operation retries  # noqa: E501

        :return: The retry_count of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """Sets the retry_count of this IoArgoprojV1alpha1ApplicationStatusOperationState.

        RetryCount contains time of operation retries  # noqa: E501

        :param retry_count: The retry_count of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :type: int
        """

        self._retry_count = retry_count

    @property
    def started_at(self):
        """Gets the started_at of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501

        StartedAt contains time of operation start  # noqa: E501

        :return: The started_at of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this IoArgoprojV1alpha1ApplicationStatusOperationState.

        StartedAt contains time of operation start  # noqa: E501

        :param started_at: The started_at of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def sync_result(self):
        """Gets the sync_result of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501


        :return: The sync_result of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResult
        """
        return self._sync_result

    @sync_result.setter
    def sync_result(self, sync_result):
        """Sets the sync_result of this IoArgoprojV1alpha1ApplicationStatusOperationState.


        :param sync_result: The sync_result of this IoArgoprojV1alpha1ApplicationStatusOperationState.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResult
        """

        self._sync_result = sync_result

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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationStatusOperationState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationStatusOperationState):
            return True

        return self.to_dict() != other.to_dict()
