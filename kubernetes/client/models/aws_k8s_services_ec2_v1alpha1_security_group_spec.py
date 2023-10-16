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


class AwsK8sServicesEc2V1alpha1SecurityGroupSpec(object):
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
        'description': 'str',
        'egress_rules': 'list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules]',
        'ingress_rules': 'list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules]',
        'name': 'str',
        'tags': 'list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]',
        'vpc_id': 'str',
        'vpc_ref': 'AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs'
    }

    attribute_map = {
        'description': 'description',
        'egress_rules': 'egressRules',
        'ingress_rules': 'ingressRules',
        'name': 'name',
        'tags': 'tags',
        'vpc_id': 'vpcID',
        'vpc_ref': 'vpcRef'
    }

    def __init__(self, description=None, egress_rules=None, ingress_rules=None, name=None, tags=None, vpc_id=None, vpc_ref=None, local_vars_configuration=None):  # noqa: E501
        """AwsK8sServicesEc2V1alpha1SecurityGroupSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._egress_rules = None
        self._ingress_rules = None
        self._name = None
        self._tags = None
        self._vpc_id = None
        self._vpc_ref = None
        self.discriminator = None

        self.description = description
        if egress_rules is not None:
            self.egress_rules = egress_rules
        if ingress_rules is not None:
            self.ingress_rules = ingress_rules
        self.name = name
        if tags is not None:
            self.tags = tags
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_ref is not None:
            self.vpc_ref = vpc_ref

    @property
    def description(self):
        """Gets the description of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501

        A description for the security group. This is informational only.   Constraints: Up to 255 characters in length   Constraints for EC2-Classic: ASCII characters   Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*  # noqa: E501

        :return: The description of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.

        A description for the security group. This is informational only.   Constraints: Up to 255 characters in length   Constraints for EC2-Classic: ASCII characters   Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*  # noqa: E501

        :param description: The description of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def egress_rules(self):
        """Gets the egress_rules of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501


        :return: The egress_rules of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules]
        """
        return self._egress_rules

    @egress_rules.setter
    def egress_rules(self, egress_rules):
        """Sets the egress_rules of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.


        :param egress_rules: The egress_rules of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules]
        """

        self._egress_rules = egress_rules

    @property
    def ingress_rules(self):
        """Gets the ingress_rules of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501


        :return: The ingress_rules of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules]
        """
        return self._ingress_rules

    @ingress_rules.setter
    def ingress_rules(self, ingress_rules):
        """Sets the ingress_rules of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.


        :param ingress_rules: The ingress_rules of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules]
        """

        self._ingress_rules = ingress_rules

    @property
    def name(self):
        """Gets the name of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501

        The name of the security group.   Constraints: Up to 255 characters in length. Cannot start with sg-.   Constraints for EC2-Classic: ASCII characters   Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*  # noqa: E501

        :return: The name of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.

        The name of the security group.   Constraints: Up to 255 characters in length. Cannot start with sg-.   Constraints for EC2-Classic: ASCII characters   Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*  # noqa: E501

        :param name: The name of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501

        The tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.  # noqa: E501

        :return: The tags of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :rtype: list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.

        The tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.  # noqa: E501

        :param tags: The tags of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :type: list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]
        """

        self._tags = tags

    @property
    def vpc_id(self):
        """Gets the vpc_id of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501

        [EC2-VPC] The ID of the VPC. Required for EC2-VPC.  # noqa: E501

        :return: The vpc_id of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.

        [EC2-VPC] The ID of the VPC. Required for EC2-VPC.  # noqa: E501

        :param vpc_id: The vpc_id of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def vpc_ref(self):
        """Gets the vpc_ref of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501


        :return: The vpc_ref of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :rtype: AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs
        """
        return self._vpc_ref

    @vpc_ref.setter
    def vpc_ref(self, vpc_ref):
        """Sets the vpc_ref of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.


        :param vpc_ref: The vpc_ref of this AwsK8sServicesEc2V1alpha1SecurityGroupSpec.  # noqa: E501
        :type: AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs
        """

        self._vpc_ref = vpc_ref

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
        if not isinstance(other, AwsK8sServicesEc2V1alpha1SecurityGroupSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsK8sServicesEc2V1alpha1SecurityGroupSpec):
            return True

        return self.to_dict() != other.to_dict()