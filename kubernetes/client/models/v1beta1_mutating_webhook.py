# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1beta1MutatingWebhook(object):
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
        'admission_review_versions': 'list[str]',
        'client_config': 'AdmissionregistrationV1beta1WebhookClientConfig',
        'failure_policy': 'str',
        'match_policy': 'str',
        'name': 'str',
        'namespace_selector': 'V1LabelSelector',
        'object_selector': 'V1LabelSelector',
        'reinvocation_policy': 'str',
        'rules': 'list[V1beta1RuleWithOperations]',
        'side_effects': 'str',
        'timeout_seconds': 'int'
    }

    attribute_map = {
        'admission_review_versions': 'admissionReviewVersions',
        'client_config': 'clientConfig',
        'failure_policy': 'failurePolicy',
        'match_policy': 'matchPolicy',
        'name': 'name',
        'namespace_selector': 'namespaceSelector',
        'object_selector': 'objectSelector',
        'reinvocation_policy': 'reinvocationPolicy',
        'rules': 'rules',
        'side_effects': 'sideEffects',
        'timeout_seconds': 'timeoutSeconds'
    }

    def __init__(self, admission_review_versions=None, client_config=None, failure_policy=None, match_policy=None, name=None, namespace_selector=None, object_selector=None, reinvocation_policy=None, rules=None, side_effects=None, timeout_seconds=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1MutatingWebhook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._admission_review_versions = None
        self._client_config = None
        self._failure_policy = None
        self._match_policy = None
        self._name = None
        self._namespace_selector = None
        self._object_selector = None
        self._reinvocation_policy = None
        self._rules = None
        self._side_effects = None
        self._timeout_seconds = None
        self.discriminator = None

        if admission_review_versions is not None:
            self.admission_review_versions = admission_review_versions
        self.client_config = client_config
        if failure_policy is not None:
            self.failure_policy = failure_policy
        if match_policy is not None:
            self.match_policy = match_policy
        self.name = name
        if namespace_selector is not None:
            self.namespace_selector = namespace_selector
        if object_selector is not None:
            self.object_selector = object_selector
        if reinvocation_policy is not None:
            self.reinvocation_policy = reinvocation_policy
        if rules is not None:
            self.rules = rules
        if side_effects is not None:
            self.side_effects = side_effects
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds

    @property
    def admission_review_versions(self):
        """Gets the admission_review_versions of this V1beta1MutatingWebhook.  # noqa: E501

        AdmissionReviewVersions is an ordered list of preferred `AdmissionReview` versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy. Default to `['v1beta1']`.  # noqa: E501

        :return: The admission_review_versions of this V1beta1MutatingWebhook.  # noqa: E501
        :rtype: list[str]
        """
        return self._admission_review_versions

    @admission_review_versions.setter
    def admission_review_versions(self, admission_review_versions):
        """Sets the admission_review_versions of this V1beta1MutatingWebhook.

        AdmissionReviewVersions is an ordered list of preferred `AdmissionReview` versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy. Default to `['v1beta1']`.  # noqa: E501

        :param admission_review_versions: The admission_review_versions of this V1beta1MutatingWebhook.  # noqa: E501
        :type: list[str]
        """

        self._admission_review_versions = admission_review_versions

    @property
    def client_config(self):
        """Gets the client_config of this V1beta1MutatingWebhook.  # noqa: E501


        :return: The client_config of this V1beta1MutatingWebhook.  # noqa: E501
        :rtype: AdmissionregistrationV1beta1WebhookClientConfig
        """
        return self._client_config

    @client_config.setter
    def client_config(self, client_config):
        """Sets the client_config of this V1beta1MutatingWebhook.


        :param client_config: The client_config of this V1beta1MutatingWebhook.  # noqa: E501
        :type: AdmissionregistrationV1beta1WebhookClientConfig
        """
        if self.local_vars_configuration.client_side_validation and client_config is None:  # noqa: E501
            raise ValueError("Invalid value for `client_config`, must not be `None`")  # noqa: E501

        self._client_config = client_config

    @property
    def failure_policy(self):
        """Gets the failure_policy of this V1beta1MutatingWebhook.  # noqa: E501

        FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Ignore.  # noqa: E501

        :return: The failure_policy of this V1beta1MutatingWebhook.  # noqa: E501
        :rtype: str
        """
        return self._failure_policy

    @failure_policy.setter
    def failure_policy(self, failure_policy):
        """Sets the failure_policy of this V1beta1MutatingWebhook.

        FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Ignore.  # noqa: E501

        :param failure_policy: The failure_policy of this V1beta1MutatingWebhook.  # noqa: E501
        :type: str
        """

        self._failure_policy = failure_policy

    @property
    def match_policy(self):
        """Gets the match_policy of this V1beta1MutatingWebhook.  # noqa: E501

        matchPolicy defines how the \"rules\" list is used to match incoming requests. Allowed values are \"Exact\" or \"Equivalent\".  - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but \"rules\" only included `apiGroups:[\"apps\"], apiVersions:[\"v1\"], resources: [\"deployments\"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.  - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and \"rules\" only included `apiGroups:[\"apps\"], apiVersions:[\"v1\"], resources: [\"deployments\"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook.  Defaults to \"Exact\"  # noqa: E501

        :return: The match_policy of this V1beta1MutatingWebhook.  # noqa: E501
        :rtype: str
        """
        return self._match_policy

    @match_policy.setter
    def match_policy(self, match_policy):
        """Sets the match_policy of this V1beta1MutatingWebhook.

        matchPolicy defines how the \"rules\" list is used to match incoming requests. Allowed values are \"Exact\" or \"Equivalent\".  - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but \"rules\" only included `apiGroups:[\"apps\"], apiVersions:[\"v1\"], resources: [\"deployments\"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.  - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and \"rules\" only included `apiGroups:[\"apps\"], apiVersions:[\"v1\"], resources: [\"deployments\"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook.  Defaults to \"Exact\"  # noqa: E501

        :param match_policy: The match_policy of this V1beta1MutatingWebhook.  # noqa: E501
        :type: str
        """

        self._match_policy = match_policy

    @property
    def name(self):
        """Gets the name of this V1beta1MutatingWebhook.  # noqa: E501

        The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where \"imagepolicy\" is the name of the webhook, and kubernetes.io is the name of the organization. Required.  # noqa: E501

        :return: The name of this V1beta1MutatingWebhook.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1beta1MutatingWebhook.

        The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where \"imagepolicy\" is the name of the webhook, and kubernetes.io is the name of the organization. Required.  # noqa: E501

        :param name: The name of this V1beta1MutatingWebhook.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace_selector(self):
        """Gets the namespace_selector of this V1beta1MutatingWebhook.  # noqa: E501


        :return: The namespace_selector of this V1beta1MutatingWebhook.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._namespace_selector

    @namespace_selector.setter
    def namespace_selector(self, namespace_selector):
        """Sets the namespace_selector of this V1beta1MutatingWebhook.


        :param namespace_selector: The namespace_selector of this V1beta1MutatingWebhook.  # noqa: E501
        :type: V1LabelSelector
        """

        self._namespace_selector = namespace_selector

    @property
    def object_selector(self):
        """Gets the object_selector of this V1beta1MutatingWebhook.  # noqa: E501


        :return: The object_selector of this V1beta1MutatingWebhook.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._object_selector

    @object_selector.setter
    def object_selector(self, object_selector):
        """Sets the object_selector of this V1beta1MutatingWebhook.


        :param object_selector: The object_selector of this V1beta1MutatingWebhook.  # noqa: E501
        :type: V1LabelSelector
        """

        self._object_selector = object_selector

    @property
    def reinvocation_policy(self):
        """Gets the reinvocation_policy of this V1beta1MutatingWebhook.  # noqa: E501

        reinvocationPolicy indicates whether this webhook should be called multiple times as part of a single admission evaluation. Allowed values are \"Never\" and \"IfNeeded\".  Never: the webhook will not be called more than once in a single admission evaluation.  IfNeeded: the webhook will be called at least one additional time as part of the admission evaluation if the object being admitted is modified by other admission plugins after the initial webhook call. Webhooks that specify this option *must* be idempotent, able to process objects they previously admitted. Note: * the number of additional invocations is not guaranteed to be exactly one. * if additional invocations result in further modifications to the object, webhooks are not guaranteed to be invoked again. * webhooks that use this option may be reordered to minimize the number of additional invocations. * to validate an object after all mutations are guaranteed complete, use a validating admission webhook instead.  Defaults to \"Never\".  # noqa: E501

        :return: The reinvocation_policy of this V1beta1MutatingWebhook.  # noqa: E501
        :rtype: str
        """
        return self._reinvocation_policy

    @reinvocation_policy.setter
    def reinvocation_policy(self, reinvocation_policy):
        """Sets the reinvocation_policy of this V1beta1MutatingWebhook.

        reinvocationPolicy indicates whether this webhook should be called multiple times as part of a single admission evaluation. Allowed values are \"Never\" and \"IfNeeded\".  Never: the webhook will not be called more than once in a single admission evaluation.  IfNeeded: the webhook will be called at least one additional time as part of the admission evaluation if the object being admitted is modified by other admission plugins after the initial webhook call. Webhooks that specify this option *must* be idempotent, able to process objects they previously admitted. Note: * the number of additional invocations is not guaranteed to be exactly one. * if additional invocations result in further modifications to the object, webhooks are not guaranteed to be invoked again. * webhooks that use this option may be reordered to minimize the number of additional invocations. * to validate an object after all mutations are guaranteed complete, use a validating admission webhook instead.  Defaults to \"Never\".  # noqa: E501

        :param reinvocation_policy: The reinvocation_policy of this V1beta1MutatingWebhook.  # noqa: E501
        :type: str
        """

        self._reinvocation_policy = reinvocation_policy

    @property
    def rules(self):
        """Gets the rules of this V1beta1MutatingWebhook.  # noqa: E501

        Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects.  # noqa: E501

        :return: The rules of this V1beta1MutatingWebhook.  # noqa: E501
        :rtype: list[V1beta1RuleWithOperations]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this V1beta1MutatingWebhook.

        Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects.  # noqa: E501

        :param rules: The rules of this V1beta1MutatingWebhook.  # noqa: E501
        :type: list[V1beta1RuleWithOperations]
        """

        self._rules = rules

    @property
    def side_effects(self):
        """Gets the side_effects of this V1beta1MutatingWebhook.  # noqa: E501

        SideEffects states whether this webhook has side effects. Acceptable values are: Unknown, None, Some, NoneOnDryRun Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission change and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some. Defaults to Unknown.  # noqa: E501

        :return: The side_effects of this V1beta1MutatingWebhook.  # noqa: E501
        :rtype: str
        """
        return self._side_effects

    @side_effects.setter
    def side_effects(self, side_effects):
        """Sets the side_effects of this V1beta1MutatingWebhook.

        SideEffects states whether this webhook has side effects. Acceptable values are: Unknown, None, Some, NoneOnDryRun Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission change and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some. Defaults to Unknown.  # noqa: E501

        :param side_effects: The side_effects of this V1beta1MutatingWebhook.  # noqa: E501
        :type: str
        """

        self._side_effects = side_effects

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this V1beta1MutatingWebhook.  # noqa: E501

        TimeoutSeconds specifies the timeout for this webhook. After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 30 seconds.  # noqa: E501

        :return: The timeout_seconds of this V1beta1MutatingWebhook.  # noqa: E501
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this V1beta1MutatingWebhook.

        TimeoutSeconds specifies the timeout for this webhook. After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 30 seconds.  # noqa: E501

        :param timeout_seconds: The timeout_seconds of this V1beta1MutatingWebhook.  # noqa: E501
        :type: int
        """

        self._timeout_seconds = timeout_seconds

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
        if not isinstance(other, V1beta1MutatingWebhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1MutatingWebhook):
            return True

        return self.to_dict() != other.to_dict()
