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


class IoArgoprojV1alpha1ApplicationOperation(object):
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
        'info': 'list[IoArgoprojV1alpha1ApplicationOperationInfo]',
        'initiated_by': 'IoArgoprojV1alpha1ApplicationOperationInitiatedBy',
        'retry': 'IoArgoprojV1alpha1ApplicationOperationRetry',
        'sync': 'IoArgoprojV1alpha1ApplicationOperationSync'
    }

    attribute_map = {
        'info': 'info',
        'initiated_by': 'initiatedBy',
        'retry': 'retry',
        'sync': 'sync'
    }

    def __init__(self, info=None, initiated_by=None, retry=None, sync=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationOperation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._info = None
        self._initiated_by = None
        self._retry = None
        self._sync = None
        self.discriminator = None

        if info is not None:
            self.info = info
        if initiated_by is not None:
            self.initiated_by = initiated_by
        if retry is not None:
            self.retry = retry
        if sync is not None:
            self.sync = sync

    @property
    def info(self):
        """Gets the info of this IoArgoprojV1alpha1ApplicationOperation.  # noqa: E501

        Info is a list of informational items for this operation  # noqa: E501

        :return: The info of this IoArgoprojV1alpha1ApplicationOperation.  # noqa: E501
        :rtype: list[IoArgoprojV1alpha1ApplicationOperationInfo]
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this IoArgoprojV1alpha1ApplicationOperation.

        Info is a list of informational items for this operation  # noqa: E501

        :param info: The info of this IoArgoprojV1alpha1ApplicationOperation.  # noqa: E501
        :type: list[IoArgoprojV1alpha1ApplicationOperationInfo]
        """

        self._info = info

    @property
    def initiated_by(self):
        """Gets the initiated_by of this IoArgoprojV1alpha1ApplicationOperation.  # noqa: E501


        :return: The initiated_by of this IoArgoprojV1alpha1ApplicationOperation.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationOperationInitiatedBy
        """
        return self._initiated_by

    @initiated_by.setter
    def initiated_by(self, initiated_by):
        """Sets the initiated_by of this IoArgoprojV1alpha1ApplicationOperation.


        :param initiated_by: The initiated_by of this IoArgoprojV1alpha1ApplicationOperation.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationOperationInitiatedBy
        """

        self._initiated_by = initiated_by

    @property
    def retry(self):
        """Gets the retry of this IoArgoprojV1alpha1ApplicationOperation.  # noqa: E501


        :return: The retry of this IoArgoprojV1alpha1ApplicationOperation.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationOperationRetry
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        """Sets the retry of this IoArgoprojV1alpha1ApplicationOperation.


        :param retry: The retry of this IoArgoprojV1alpha1ApplicationOperation.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationOperationRetry
        """

        self._retry = retry

    @property
    def sync(self):
        """Gets the sync of this IoArgoprojV1alpha1ApplicationOperation.  # noqa: E501


        :return: The sync of this IoArgoprojV1alpha1ApplicationOperation.  # noqa: E501
        :rtype: IoArgoprojV1alpha1ApplicationOperationSync
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        """Sets the sync of this IoArgoprojV1alpha1ApplicationOperation.


        :param sync: The sync of this IoArgoprojV1alpha1ApplicationOperation.  # noqa: E501
        :type: IoArgoprojV1alpha1ApplicationOperationSync
        """

        self._sync = sync

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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationOperation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationOperation):
            return True

        return self.to_dict() != other.to_dict()
