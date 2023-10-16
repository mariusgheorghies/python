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


class IoQuestdbQuestdbV1alpha1QuestDBSpecConfig(object):
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
        'cairo': 'IoQuestdbQuestdbV1alpha1QuestDBSpecConfigCairo',
        'http': 'IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp',
        'ilp': 'IoQuestdbQuestdbV1alpha1QuestDBSpecConfigIlp',
        'postgres': 'IoQuestdbQuestdbV1alpha1QuestDBSpecConfigPostgres',
        'query_timeout_seconds': 'int',
        'shared_worker_count': 'int'
    }

    attribute_map = {
        'cairo': 'cairo',
        'http': 'http',
        'ilp': 'ilp',
        'postgres': 'postgres',
        'query_timeout_seconds': 'queryTimeoutSeconds',
        'shared_worker_count': 'sharedWorkerCount'
    }

    def __init__(self, cairo=None, http=None, ilp=None, postgres=None, query_timeout_seconds=None, shared_worker_count=None, local_vars_configuration=None):  # noqa: E501
        """IoQuestdbQuestdbV1alpha1QuestDBSpecConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cairo = None
        self._http = None
        self._ilp = None
        self._postgres = None
        self._query_timeout_seconds = None
        self._shared_worker_count = None
        self.discriminator = None

        if cairo is not None:
            self.cairo = cairo
        if http is not None:
            self.http = http
        if ilp is not None:
            self.ilp = ilp
        if postgres is not None:
            self.postgres = postgres
        if query_timeout_seconds is not None:
            self.query_timeout_seconds = query_timeout_seconds
        if shared_worker_count is not None:
            self.shared_worker_count = shared_worker_count

    @property
    def cairo(self):
        """Gets the cairo of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501


        :return: The cairo of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501
        :rtype: IoQuestdbQuestdbV1alpha1QuestDBSpecConfigCairo
        """
        return self._cairo

    @cairo.setter
    def cairo(self, cairo):
        """Sets the cairo of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.


        :param cairo: The cairo of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501
        :type: IoQuestdbQuestdbV1alpha1QuestDBSpecConfigCairo
        """

        self._cairo = cairo

    @property
    def http(self):
        """Gets the http of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501


        :return: The http of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501
        :rtype: IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp
        """
        return self._http

    @http.setter
    def http(self, http):
        """Sets the http of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.


        :param http: The http of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501
        :type: IoQuestdbQuestdbV1alpha1QuestDBSpecConfigHttp
        """

        self._http = http

    @property
    def ilp(self):
        """Gets the ilp of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501


        :return: The ilp of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501
        :rtype: IoQuestdbQuestdbV1alpha1QuestDBSpecConfigIlp
        """
        return self._ilp

    @ilp.setter
    def ilp(self, ilp):
        """Sets the ilp of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.


        :param ilp: The ilp of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501
        :type: IoQuestdbQuestdbV1alpha1QuestDBSpecConfigIlp
        """

        self._ilp = ilp

    @property
    def postgres(self):
        """Gets the postgres of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501


        :return: The postgres of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501
        :rtype: IoQuestdbQuestdbV1alpha1QuestDBSpecConfigPostgres
        """
        return self._postgres

    @postgres.setter
    def postgres(self, postgres):
        """Sets the postgres of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.


        :param postgres: The postgres of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501
        :type: IoQuestdbQuestdbV1alpha1QuestDBSpecConfigPostgres
        """

        self._postgres = postgres

    @property
    def query_timeout_seconds(self):
        """Gets the query_timeout_seconds of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501


        :return: The query_timeout_seconds of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501
        :rtype: int
        """
        return self._query_timeout_seconds

    @query_timeout_seconds.setter
    def query_timeout_seconds(self, query_timeout_seconds):
        """Sets the query_timeout_seconds of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.


        :param query_timeout_seconds: The query_timeout_seconds of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501
        :type: int
        """

        self._query_timeout_seconds = query_timeout_seconds

    @property
    def shared_worker_count(self):
        """Gets the shared_worker_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501


        :return: The shared_worker_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501
        :rtype: int
        """
        return self._shared_worker_count

    @shared_worker_count.setter
    def shared_worker_count(self, shared_worker_count):
        """Sets the shared_worker_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.


        :param shared_worker_count: The shared_worker_count of this IoQuestdbQuestdbV1alpha1QuestDBSpecConfig.  # noqa: E501
        :type: int
        """

        self._shared_worker_count = shared_worker_count

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
        if not isinstance(other, IoQuestdbQuestdbV1alpha1QuestDBSpecConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoQuestdbQuestdbV1alpha1QuestDBSpecConfig):
            return True

        return self.to_dict() != other.to_dict()
