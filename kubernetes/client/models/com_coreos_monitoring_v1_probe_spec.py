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


class ComCoreosMonitoringV1ProbeSpec(object):
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
        'interval': 'str',
        'job_name': 'str',
        'module': 'str',
        'prober': 'ComCoreosMonitoringV1ProbeSpecProber',
        'scrape_timeout': 'str',
        'targets': 'ComCoreosMonitoringV1ProbeSpecTargets'
    }

    attribute_map = {
        'interval': 'interval',
        'job_name': 'jobName',
        'module': 'module',
        'prober': 'prober',
        'scrape_timeout': 'scrapeTimeout',
        'targets': 'targets'
    }

    def __init__(self, interval=None, job_name=None, module=None, prober=None, scrape_timeout=None, targets=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1ProbeSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._interval = None
        self._job_name = None
        self._module = None
        self._prober = None
        self._scrape_timeout = None
        self._targets = None
        self.discriminator = None

        if interval is not None:
            self.interval = interval
        if job_name is not None:
            self.job_name = job_name
        if module is not None:
            self.module = module
        if prober is not None:
            self.prober = prober
        if scrape_timeout is not None:
            self.scrape_timeout = scrape_timeout
        if targets is not None:
            self.targets = targets

    @property
    def interval(self):
        """Gets the interval of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501

        Interval at which targets are probed using the configured prober. If not specified Prometheus' global scrape interval is used.  # noqa: E501

        :return: The interval of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ComCoreosMonitoringV1ProbeSpec.

        Interval at which targets are probed using the configured prober. If not specified Prometheus' global scrape interval is used.  # noqa: E501

        :param interval: The interval of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501
        :type: str
        """

        self._interval = interval

    @property
    def job_name(self):
        """Gets the job_name of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501

        The job name assigned to scraped metrics by default.  # noqa: E501

        :return: The job_name of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ComCoreosMonitoringV1ProbeSpec.

        The job name assigned to scraped metrics by default.  # noqa: E501

        :param job_name: The job_name of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

    @property
    def module(self):
        """Gets the module of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501

        The module to use for probing specifying how to probe the target. Example module configuring in the blackbox exporter: https://github.com/prometheus/blackbox_exporter/blob/master/example.yml  # noqa: E501

        :return: The module of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this ComCoreosMonitoringV1ProbeSpec.

        The module to use for probing specifying how to probe the target. Example module configuring in the blackbox exporter: https://github.com/prometheus/blackbox_exporter/blob/master/example.yml  # noqa: E501

        :param module: The module of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501
        :type: str
        """

        self._module = module

    @property
    def prober(self):
        """Gets the prober of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501


        :return: The prober of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501
        :rtype: ComCoreosMonitoringV1ProbeSpecProber
        """
        return self._prober

    @prober.setter
    def prober(self, prober):
        """Sets the prober of this ComCoreosMonitoringV1ProbeSpec.


        :param prober: The prober of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501
        :type: ComCoreosMonitoringV1ProbeSpecProber
        """

        self._prober = prober

    @property
    def scrape_timeout(self):
        """Gets the scrape_timeout of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501

        Timeout for scraping metrics from the Prometheus exporter.  # noqa: E501

        :return: The scrape_timeout of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501
        :rtype: str
        """
        return self._scrape_timeout

    @scrape_timeout.setter
    def scrape_timeout(self, scrape_timeout):
        """Sets the scrape_timeout of this ComCoreosMonitoringV1ProbeSpec.

        Timeout for scraping metrics from the Prometheus exporter.  # noqa: E501

        :param scrape_timeout: The scrape_timeout of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501
        :type: str
        """

        self._scrape_timeout = scrape_timeout

    @property
    def targets(self):
        """Gets the targets of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501


        :return: The targets of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501
        :rtype: ComCoreosMonitoringV1ProbeSpecTargets
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this ComCoreosMonitoringV1ProbeSpec.


        :param targets: The targets of this ComCoreosMonitoringV1ProbeSpec.  # noqa: E501
        :type: ComCoreosMonitoringV1ProbeSpecTargets
        """

        self._targets = targets

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
        if not isinstance(other, ComCoreosMonitoringV1ProbeSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1ProbeSpec):
            return True

        return self.to_dict() != other.to_dict()
