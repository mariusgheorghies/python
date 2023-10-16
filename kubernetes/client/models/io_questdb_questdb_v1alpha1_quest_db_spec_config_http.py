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


class IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp(object):
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
        'cache_block_count': 'int',
        'cache_enabled': 'bool',
        'cache_row_count': 'int',
        'connection_limit': 'int',
        'read_only_mode': 'bool',
        'worker_count': 'int'
    }

    attribute_map = {
        'cache_block_count': 'cacheBlockCount',
        'cache_enabled': 'cacheEnabled',
        'cache_row_count': 'cacheRowCount',
        'connection_limit': 'connectionLimit',
        'read_only_mode': 'readOnlyMode',
        'worker_count': 'workerCount'
    }

    def __init__(self, cache_block_count=None, cache_enabled=None, cache_row_count=None, connection_limit=None, read_only_mode=None, worker_count=None, local_vars_configuration=None):  # noqa: E501
        """IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cache_block_count = None
        self._cache_enabled = None
        self._cache_row_count = None
        self._connection_limit = None
        self._read_only_mode = None
        self._worker_count = None
        self.discriminator = None

        if cache_block_count is not None:
            self.cache_block_count = cache_block_count
        if cache_enabled is not None:
            self.cache_enabled = cache_enabled
        if cache_row_count is not None:
            self.cache_row_count = cache_row_count
        if connection_limit is not None:
            self.connection_limit = connection_limit
        if read_only_mode is not None:
            self.read_only_mode = read_only_mode
        if worker_count is not None:
            self.worker_count = worker_count

    @property
    def cache_block_count(self):
        """Gets the cache_block_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501


        :return: The cache_block_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501
        :rtype: int
        """
        return self._cache_block_count

    @cache_block_count.setter
    def cache_block_count(self, cache_block_count):
        """Sets the cache_block_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.


        :param cache_block_count: The cache_block_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501
        :type: int
        """

        self._cache_block_count = cache_block_count

    @property
    def cache_enabled(self):
        """Gets the cache_enabled of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501


        :return: The cache_enabled of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501
        :rtype: bool
        """
        return self._cache_enabled

    @cache_enabled.setter
    def cache_enabled(self, cache_enabled):
        """Sets the cache_enabled of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.


        :param cache_enabled: The cache_enabled of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501
        :type: bool
        """

        self._cache_enabled = cache_enabled

    @property
    def cache_row_count(self):
        """Gets the cache_row_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501


        :return: The cache_row_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501
        :rtype: int
        """
        return self._cache_row_count

    @cache_row_count.setter
    def cache_row_count(self, cache_row_count):
        """Sets the cache_row_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.


        :param cache_row_count: The cache_row_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501
        :type: int
        """

        self._cache_row_count = cache_row_count

    @property
    def connection_limit(self):
        """Gets the connection_limit of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501


        :return: The connection_limit of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501
        :rtype: int
        """
        return self._connection_limit

    @connection_limit.setter
    def connection_limit(self, connection_limit):
        """Sets the connection_limit of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.


        :param connection_limit: The connection_limit of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501
        :type: int
        """

        self._connection_limit = connection_limit

    @property
    def read_only_mode(self):
        """Gets the read_only_mode of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501


        :return: The read_only_mode of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501
        :rtype: bool
        """
        return self._read_only_mode

    @read_only_mode.setter
    def read_only_mode(self, read_only_mode):
        """Sets the read_only_mode of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.


        :param read_only_mode: The read_only_mode of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501
        :type: bool
        """

        self._read_only_mode = read_only_mode

    @property
    def worker_count(self):
        """Gets the worker_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501


        :return: The worker_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501
        :rtype: int
        """
        return self._worker_count

    @worker_count.setter
    def worker_count(self, worker_count):
        """Sets the worker_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.


        :param worker_count: The worker_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp.  # noqa: E501
        :type: int
        """

        self._worker_count = worker_count

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
        if not isinstance(other, IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp):
            return True

        return self.to_dict() != other.to_dict()