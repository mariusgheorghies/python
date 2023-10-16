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


class ComCoreosMonitoringV1PodMonitorSpec(object):
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
        'attach_metadata': 'ComCoreosMonitoringV1PodMonitorSpecAttachMetadata',
        'job_label': 'str',
        'label_limit': 'int',
        'label_name_length_limit': 'int',
        'label_value_length_limit': 'int',
        'namespace_selector': 'ComCoreosMonitoringV1PodMonitorSpecNamespaceSelector',
        'pod_metrics_endpoints': 'list[ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints]',
        'pod_target_labels': 'list[str]',
        'sample_limit': 'int',
        'selector': 'ComCoreosMonitoringV1PodMonitorSpecSelector',
        'target_limit': 'int'
    }

    attribute_map = {
        'attach_metadata': 'attachMetadata',
        'job_label': 'jobLabel',
        'label_limit': 'labelLimit',
        'label_name_length_limit': 'labelNameLengthLimit',
        'label_value_length_limit': 'labelValueLengthLimit',
        'namespace_selector': 'namespaceSelector',
        'pod_metrics_endpoints': 'podMetricsEndpoints',
        'pod_target_labels': 'podTargetLabels',
        'sample_limit': 'sampleLimit',
        'selector': 'selector',
        'target_limit': 'targetLimit'
    }

    def __init__(self, attach_metadata=None, job_label=None, label_limit=None, label_name_length_limit=None, label_value_length_limit=None, namespace_selector=None, pod_metrics_endpoints=None, pod_target_labels=None, sample_limit=None, selector=None, target_limit=None, local_vars_configuration=None):  # noqa: E501
        """ComCoreosMonitoringV1PodMonitorSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attach_metadata = None
        self._job_label = None
        self._label_limit = None
        self._label_name_length_limit = None
        self._label_value_length_limit = None
        self._namespace_selector = None
        self._pod_metrics_endpoints = None
        self._pod_target_labels = None
        self._sample_limit = None
        self._selector = None
        self._target_limit = None
        self.discriminator = None

        if attach_metadata is not None:
            self.attach_metadata = attach_metadata
        if job_label is not None:
            self.job_label = job_label
        if label_limit is not None:
            self.label_limit = label_limit
        if label_name_length_limit is not None:
            self.label_name_length_limit = label_name_length_limit
        if label_value_length_limit is not None:
            self.label_value_length_limit = label_value_length_limit
        if namespace_selector is not None:
            self.namespace_selector = namespace_selector
        self.pod_metrics_endpoints = pod_metrics_endpoints
        if pod_target_labels is not None:
            self.pod_target_labels = pod_target_labels
        if sample_limit is not None:
            self.sample_limit = sample_limit
        self.selector = selector
        if target_limit is not None:
            self.target_limit = target_limit

    @property
    def attach_metadata(self):
        """Gets the attach_metadata of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501


        :return: The attach_metadata of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecAttachMetadata
        """
        return self._attach_metadata

    @attach_metadata.setter
    def attach_metadata(self, attach_metadata):
        """Sets the attach_metadata of this ComCoreosMonitoringV1PodMonitorSpec.


        :param attach_metadata: The attach_metadata of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecAttachMetadata
        """

        self._attach_metadata = attach_metadata

    @property
    def job_label(self):
        """Gets the job_label of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501

        The label to use to retrieve the job name from.  # noqa: E501

        :return: The job_label of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :rtype: str
        """
        return self._job_label

    @job_label.setter
    def job_label(self, job_label):
        """Sets the job_label of this ComCoreosMonitoringV1PodMonitorSpec.

        The label to use to retrieve the job name from.  # noqa: E501

        :param job_label: The job_label of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :type: str
        """

        self._job_label = job_label

    @property
    def label_limit(self):
        """Gets the label_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501

        Per-scrape limit on number of labels that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.  # noqa: E501

        :return: The label_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :rtype: int
        """
        return self._label_limit

    @label_limit.setter
    def label_limit(self, label_limit):
        """Sets the label_limit of this ComCoreosMonitoringV1PodMonitorSpec.

        Per-scrape limit on number of labels that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.  # noqa: E501

        :param label_limit: The label_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :type: int
        """

        self._label_limit = label_limit

    @property
    def label_name_length_limit(self):
        """Gets the label_name_length_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501

        Per-scrape limit on length of labels name that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.  # noqa: E501

        :return: The label_name_length_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :rtype: int
        """
        return self._label_name_length_limit

    @label_name_length_limit.setter
    def label_name_length_limit(self, label_name_length_limit):
        """Sets the label_name_length_limit of this ComCoreosMonitoringV1PodMonitorSpec.

        Per-scrape limit on length of labels name that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.  # noqa: E501

        :param label_name_length_limit: The label_name_length_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :type: int
        """

        self._label_name_length_limit = label_name_length_limit

    @property
    def label_value_length_limit(self):
        """Gets the label_value_length_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501

        Per-scrape limit on length of labels value that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.  # noqa: E501

        :return: The label_value_length_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :rtype: int
        """
        return self._label_value_length_limit

    @label_value_length_limit.setter
    def label_value_length_limit(self, label_value_length_limit):
        """Sets the label_value_length_limit of this ComCoreosMonitoringV1PodMonitorSpec.

        Per-scrape limit on length of labels value that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.  # noqa: E501

        :param label_value_length_limit: The label_value_length_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :type: int
        """

        self._label_value_length_limit = label_value_length_limit

    @property
    def namespace_selector(self):
        """Gets the namespace_selector of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501


        :return: The namespace_selector of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecNamespaceSelector
        """
        return self._namespace_selector

    @namespace_selector.setter
    def namespace_selector(self, namespace_selector):
        """Sets the namespace_selector of this ComCoreosMonitoringV1PodMonitorSpec.


        :param namespace_selector: The namespace_selector of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecNamespaceSelector
        """

        self._namespace_selector = namespace_selector

    @property
    def pod_metrics_endpoints(self):
        """Gets the pod_metrics_endpoints of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501

        A list of endpoints allowed as part of this PodMonitor.  # noqa: E501

        :return: The pod_metrics_endpoints of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :rtype: list[ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints]
        """
        return self._pod_metrics_endpoints

    @pod_metrics_endpoints.setter
    def pod_metrics_endpoints(self, pod_metrics_endpoints):
        """Sets the pod_metrics_endpoints of this ComCoreosMonitoringV1PodMonitorSpec.

        A list of endpoints allowed as part of this PodMonitor.  # noqa: E501

        :param pod_metrics_endpoints: The pod_metrics_endpoints of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :type: list[ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints]
        """
        if self.local_vars_configuration.client_side_validation and pod_metrics_endpoints is None:  # noqa: E501
            raise ValueError("Invalid value for `pod_metrics_endpoints`, must not be `None`")  # noqa: E501

        self._pod_metrics_endpoints = pod_metrics_endpoints

    @property
    def pod_target_labels(self):
        """Gets the pod_target_labels of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501

        PodTargetLabels transfers labels on the Kubernetes Pod onto the target.  # noqa: E501

        :return: The pod_target_labels of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._pod_target_labels

    @pod_target_labels.setter
    def pod_target_labels(self, pod_target_labels):
        """Sets the pod_target_labels of this ComCoreosMonitoringV1PodMonitorSpec.

        PodTargetLabels transfers labels on the Kubernetes Pod onto the target.  # noqa: E501

        :param pod_target_labels: The pod_target_labels of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :type: list[str]
        """

        self._pod_target_labels = pod_target_labels

    @property
    def sample_limit(self):
        """Gets the sample_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501

        SampleLimit defines per-scrape limit on number of scraped samples that will be accepted.  # noqa: E501

        :return: The sample_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :rtype: int
        """
        return self._sample_limit

    @sample_limit.setter
    def sample_limit(self, sample_limit):
        """Sets the sample_limit of this ComCoreosMonitoringV1PodMonitorSpec.

        SampleLimit defines per-scrape limit on number of scraped samples that will be accepted.  # noqa: E501

        :param sample_limit: The sample_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :type: int
        """

        self._sample_limit = sample_limit

    @property
    def selector(self):
        """Gets the selector of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501


        :return: The selector of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :rtype: ComCoreosMonitoringV1PodMonitorSpecSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this ComCoreosMonitoringV1PodMonitorSpec.


        :param selector: The selector of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :type: ComCoreosMonitoringV1PodMonitorSpecSelector
        """
        if self.local_vars_configuration.client_side_validation and selector is None:  # noqa: E501
            raise ValueError("Invalid value for `selector`, must not be `None`")  # noqa: E501

        self._selector = selector

    @property
    def target_limit(self):
        """Gets the target_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501

        TargetLimit defines a limit on the number of scraped targets that will be accepted.  # noqa: E501

        :return: The target_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :rtype: int
        """
        return self._target_limit

    @target_limit.setter
    def target_limit(self, target_limit):
        """Sets the target_limit of this ComCoreosMonitoringV1PodMonitorSpec.

        TargetLimit defines a limit on the number of scraped targets that will be accepted.  # noqa: E501

        :param target_limit: The target_limit of this ComCoreosMonitoringV1PodMonitorSpec.  # noqa: E501
        :type: int
        """

        self._target_limit = target_limit

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
        if not isinstance(other, ComCoreosMonitoringV1PodMonitorSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComCoreosMonitoringV1PodMonitorSpec):
            return True

        return self.to_dict() != other.to_dict()
