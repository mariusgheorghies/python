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


class ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints(object):
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
        'label_selector': 'ComCoreosMonitoringV1AlertmanagerSpecLabelSelector',
        'match_label_keys': 'list[str]',
        'max_skew': 'int',
        'min_domains': 'int',
        'node_affinity_policy': 'str',
        'node_taints_policy': 'str',
        'topology_key': 'str',
        'when_unsatisfiable': 'str'
    }

    attribute_map = {
        'label_selector': 'labelSelector',
        'match_label_keys': 'matchLabelKeys',
        'max_skew': 'maxSkew',
        'min_domains': 'minDomains',
        'node_affinity_policy': 'nodeAffinityPolicy',
        'node_taints_policy': 'nodeTaintsPolicy',
        'topology_key': 'topologyKey',
        'when_unsatisfiable': 'whenUnsatisfiable'
    }

    def __init__(self, label_selector=None, match_label_keys=None, max_skew=None, min_domains=None, node_affinity_policy=None, node_taints_policy=None, topology_key=None, when_unsatisfiable=None, local_vars_configuration=None):  # noqa: E501
        """ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._label_selector = None
        self._match_label_keys = None
        self._max_skew = None
        self._min_domains = None
        self._node_affinity_policy = None
        self._node_taints_policy = None
        self._topology_key = None
        self._when_unsatisfiable = None
        self.discriminator = None

        if label_selector is not None:
            self.label_selector = label_selector
        if match_label_keys is not None:
            self.match_label_keys = match_label_keys
        self.max_skew = max_skew
        if min_domains is not None:
            self.min_domains = min_domains
        if node_affinity_policy is not None:
            self.node_affinity_policy = node_affinity_policy
        if node_taints_policy is not None:
            self.node_taints_policy = node_taints_policy
        self.topology_key = topology_key
        self.when_unsatisfiable = when_unsatisfiable

    @property
    def label_selector(self):
        """Gets the label_selector of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501


        :return: The label_selector of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :rtype: ComCoreosMonitoringV1AlertmanagerSpecLabelSelector
        """
        return self._label_selector

    @label_selector.setter
    def label_selector(self, label_selector):
        """Sets the label_selector of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.


        :param label_selector: The label_selector of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :type: ComCoreosMonitoringV1AlertmanagerSpecLabelSelector
        """

        self._label_selector = label_selector

    @property
    def match_label_keys(self):
        """Gets the match_label_keys of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501

        MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. Keys that don't exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.  # noqa: E501

        :return: The match_label_keys of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :rtype: list[str]
        """
        return self._match_label_keys

    @match_label_keys.setter
    def match_label_keys(self, match_label_keys):
        """Sets the match_label_keys of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.

        MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. Keys that don't exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.  # noqa: E501

        :param match_label_keys: The match_label_keys of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :type: list[str]
        """

        self._match_label_keys = match_label_keys

    @property
    def max_skew(self):
        """Gets the max_skew of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501

        MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | |  P P  |  P P  |   P   | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed.  # noqa: E501

        :return: The max_skew of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :rtype: int
        """
        return self._max_skew

    @max_skew.setter
    def max_skew(self, max_skew):
        """Sets the max_skew of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.

        MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | |  P P  |  P P  |   P   | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed.  # noqa: E501

        :param max_skew: The max_skew of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_skew is None:  # noqa: E501
            raise ValueError("Invalid value for `max_skew`, must not be `None`")  # noqa: E501

        self._max_skew = max_skew

    @property
    def min_domains(self):
        """Gets the min_domains of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501

        MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats \"global minimum\" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won't schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.   For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | |  P P  |  P P  |  P P  | The number of domains is less than 5(MinDomains), so \"global minimum\" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.   This is a beta field and requires the MinDomainsInPodTopologySpread feature gate to be enabled (enabled by default).  # noqa: E501

        :return: The min_domains of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :rtype: int
        """
        return self._min_domains

    @min_domains.setter
    def min_domains(self, min_domains):
        """Sets the min_domains of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.

        MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats \"global minimum\" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won't schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.   For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | |  P P  |  P P  |  P P  | The number of domains is less than 5(MinDomains), so \"global minimum\" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.   This is a beta field and requires the MinDomainsInPodTopologySpread feature gate to be enabled (enabled by default).  # noqa: E501

        :param min_domains: The min_domains of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :type: int
        """

        self._min_domains = min_domains

    @property
    def node_affinity_policy(self):
        """Gets the node_affinity_policy of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501

        NodeAffinityPolicy indicates how we will treat Pod's nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.   If this value is nil, the behavior is equivalent to the Honor policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.  # noqa: E501

        :return: The node_affinity_policy of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :rtype: str
        """
        return self._node_affinity_policy

    @node_affinity_policy.setter
    def node_affinity_policy(self, node_affinity_policy):
        """Sets the node_affinity_policy of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.

        NodeAffinityPolicy indicates how we will treat Pod's nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.   If this value is nil, the behavior is equivalent to the Honor policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.  # noqa: E501

        :param node_affinity_policy: The node_affinity_policy of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :type: str
        """

        self._node_affinity_policy = node_affinity_policy

    @property
    def node_taints_policy(self):
        """Gets the node_taints_policy of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501

        NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.   If this value is nil, the behavior is equivalent to the Ignore policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.  # noqa: E501

        :return: The node_taints_policy of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :rtype: str
        """
        return self._node_taints_policy

    @node_taints_policy.setter
    def node_taints_policy(self, node_taints_policy):
        """Sets the node_taints_policy of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.

        NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.   If this value is nil, the behavior is equivalent to the Ignore policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.  # noqa: E501

        :param node_taints_policy: The node_taints_policy of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :type: str
        """

        self._node_taints_policy = node_taints_policy

    @property
    def topology_key(self):
        """Gets the topology_key of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501

        TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a \"bucket\", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is \"kubernetes.io/hostname\", each Node is a domain of that topology. And, if TopologyKey is \"topology.kubernetes.io/zone\", each zone is a domain of that topology. It's a required field.  # noqa: E501

        :return: The topology_key of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :rtype: str
        """
        return self._topology_key

    @topology_key.setter
    def topology_key(self, topology_key):
        """Sets the topology_key of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.

        TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a \"bucket\", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is \"kubernetes.io/hostname\", each Node is a domain of that topology. And, if TopologyKey is \"topology.kubernetes.io/zone\", each zone is a domain of that topology. It's a required field.  # noqa: E501

        :param topology_key: The topology_key of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and topology_key is None:  # noqa: E501
            raise ValueError("Invalid value for `topology_key`, must not be `None`")  # noqa: E501

        self._topology_key = topology_key

    @property
    def when_unsatisfiable(self):
        """Gets the when_unsatisfiable of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501

        WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location, but giving higher precedence to topologies that would help reduce the skew. A constraint is considered \"Unsatisfiable\" for an incoming pod if and only if every possible node assignment for that pod would violate \"MaxSkew\" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.  # noqa: E501

        :return: The when_unsatisfiable of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :rtype: str
        """
        return self._when_unsatisfiable

    @when_unsatisfiable.setter
    def when_unsatisfiable(self, when_unsatisfiable):
        """Sets the when_unsatisfiable of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.

        WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location, but giving higher precedence to topologies that would help reduce the skew. A constraint is considered \"Unsatisfiable\" for an incoming pod if and only if every possible node assignment for that pod would violate \"MaxSkew\" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.  # noqa: E501

        :param when_unsatisfiable: The when_unsatisfiable of this ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and when_unsatisfiable is None:  # noqa: E501
            raise ValueError("Invalid value for `when_unsatisfiable`, must not be `None`")  # noqa: E501

        self._when_unsatisfiable = when_unsatisfiable

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
        if not isinstance(other, ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints):
            return True

        return self.to_dict() != other.to_dict()
