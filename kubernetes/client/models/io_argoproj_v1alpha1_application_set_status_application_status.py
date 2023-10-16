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


class IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus(object):
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
        'application': 'str',
        'last_transition_time': 'datetime',
        'message': 'str',
        'status': 'str',
        'step': 'str'
    }

    attribute_map = {
        'application': 'application',
        'last_transition_time': 'lastTransitionTime',
        'message': 'message',
        'status': 'status',
        'step': 'step'
    }

    def __init__(self, application=None, last_transition_time=None, message=None, status=None, step=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application = None
        self._last_transition_time = None
        self._message = None
        self._status = None
        self._step = None
        self.discriminator = None

        self.application = application
        if last_transition_time is not None:
            self.last_transition_time = last_transition_time
        self.message = message
        self.status = status
        self.step = step

    @property
    def application(self):
        """Gets the application of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501


        :return: The application of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.


        :param application: The application of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and application is None:  # noqa: E501
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def last_transition_time(self):
        """Gets the last_transition_time of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501


        :return: The last_transition_time of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """Sets the last_transition_time of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.


        :param last_transition_time: The last_transition_time of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501
        :type: datetime
        """

        self._last_transition_time = last_transition_time

    @property
    def message(self):
        """Gets the message of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501


        :return: The message of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.


        :param message: The message of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def status(self):
        """Gets the status of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501


        :return: The status of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.


        :param status: The status of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def step(self):
        """Gets the step of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501


        :return: The step of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.


        :param step: The step of this IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and step is None:  # noqa: E501
            raise ValueError("Invalid value for `step`, must not be `None`")  # noqa: E501

        self._step = step

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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetStatusApplicationStatus):
            return True

        return self.to_dict() != other.to_dict()