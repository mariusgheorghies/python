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


class IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate(object):
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
        'additional_security_groups': 'list[IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecAdditionalSecurityGroups]',
        'ami': 'IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecAmi',
        'iam_instance_profile': 'str',
        'image_lookup_base_os': 'str',
        'image_lookup_format': 'str',
        'image_lookup_org': 'str',
        'instance_type': 'str',
        'name': 'str',
        'root_volume': 'IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecRootVolume',
        'ssh_key_name': 'str',
        'version_number': 'int'
    }

    attribute_map = {
        'additional_security_groups': 'additionalSecurityGroups',
        'ami': 'ami',
        'iam_instance_profile': 'iamInstanceProfile',
        'image_lookup_base_os': 'imageLookupBaseOS',
        'image_lookup_format': 'imageLookupFormat',
        'image_lookup_org': 'imageLookupOrg',
        'instance_type': 'instanceType',
        'name': 'name',
        'root_volume': 'rootVolume',
        'ssh_key_name': 'sshKeyName',
        'version_number': 'versionNumber'
    }

    def __init__(self, additional_security_groups=None, ami=None, iam_instance_profile=None, image_lookup_base_os=None, image_lookup_format=None, image_lookup_org=None, instance_type=None, name=None, root_volume=None, ssh_key_name=None, version_number=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._additional_security_groups = None
        self._ami = None
        self._iam_instance_profile = None
        self._image_lookup_base_os = None
        self._image_lookup_format = None
        self._image_lookup_org = None
        self._instance_type = None
        self._name = None
        self._root_volume = None
        self._ssh_key_name = None
        self._version_number = None
        self.discriminator = None

        if additional_security_groups is not None:
            self.additional_security_groups = additional_security_groups
        if ami is not None:
            self.ami = ami
        if iam_instance_profile is not None:
            self.iam_instance_profile = iam_instance_profile
        if image_lookup_base_os is not None:
            self.image_lookup_base_os = image_lookup_base_os
        if image_lookup_format is not None:
            self.image_lookup_format = image_lookup_format
        if image_lookup_org is not None:
            self.image_lookup_org = image_lookup_org
        if instance_type is not None:
            self.instance_type = instance_type
        if name is not None:
            self.name = name
        if root_volume is not None:
            self.root_volume = root_volume
        if ssh_key_name is not None:
            self.ssh_key_name = ssh_key_name
        if version_number is not None:
            self.version_number = version_number

    @property
    def additional_security_groups(self):
        """Gets the additional_security_groups of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501

        AdditionalSecurityGroups is an array of references to security groups that should be applied to the instances. These security groups would be set in addition to any security groups defined at the cluster level or in the actuator.  # noqa: E501

        :return: The additional_security_groups of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :rtype: list[IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecAdditionalSecurityGroups]
        """
        return self._additional_security_groups

    @additional_security_groups.setter
    def additional_security_groups(self, additional_security_groups):
        """Sets the additional_security_groups of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.

        AdditionalSecurityGroups is an array of references to security groups that should be applied to the instances. These security groups would be set in addition to any security groups defined at the cluster level or in the actuator.  # noqa: E501

        :param additional_security_groups: The additional_security_groups of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :type: list[IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecAdditionalSecurityGroups]
        """

        self._additional_security_groups = additional_security_groups

    @property
    def ami(self):
        """Gets the ami of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501


        :return: The ami of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :rtype: IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecAmi
        """
        return self._ami

    @ami.setter
    def ami(self, ami):
        """Sets the ami of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.


        :param ami: The ami of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :type: IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecAmi
        """

        self._ami = ami

    @property
    def iam_instance_profile(self):
        """Gets the iam_instance_profile of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501

        The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role.  # noqa: E501

        :return: The iam_instance_profile of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :rtype: str
        """
        return self._iam_instance_profile

    @iam_instance_profile.setter
    def iam_instance_profile(self, iam_instance_profile):
        """Sets the iam_instance_profile of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.

        The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role.  # noqa: E501

        :param iam_instance_profile: The iam_instance_profile of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :type: str
        """

        self._iam_instance_profile = iam_instance_profile

    @property
    def image_lookup_base_os(self):
        """Gets the image_lookup_base_os of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501

        ImageLookupBaseOS is the name of the base operating system to use for image lookup the AMI is not set.  # noqa: E501

        :return: The image_lookup_base_os of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :rtype: str
        """
        return self._image_lookup_base_os

    @image_lookup_base_os.setter
    def image_lookup_base_os(self, image_lookup_base_os):
        """Sets the image_lookup_base_os of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.

        ImageLookupBaseOS is the name of the base operating system to use for image lookup the AMI is not set.  # noqa: E501

        :param image_lookup_base_os: The image_lookup_base_os of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :type: str
        """

        self._image_lookup_base_os = image_lookup_base_os

    @property
    def image_lookup_format(self):
        """Gets the image_lookup_format of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501

        ImageLookupFormat is the AMI naming format to look up the image for this machine It will be ignored if an explicit AMI is set. Supports substitutions for {{.BaseOS}} and {{.K8sVersion}} with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami-{{.BaseOS}}-?{{.K8sVersion}}-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/  # noqa: E501

        :return: The image_lookup_format of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :rtype: str
        """
        return self._image_lookup_format

    @image_lookup_format.setter
    def image_lookup_format(self, image_lookup_format):
        """Sets the image_lookup_format of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.

        ImageLookupFormat is the AMI naming format to look up the image for this machine It will be ignored if an explicit AMI is set. Supports substitutions for {{.BaseOS}} and {{.K8sVersion}} with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami-{{.BaseOS}}-?{{.K8sVersion}}-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/  # noqa: E501

        :param image_lookup_format: The image_lookup_format of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :type: str
        """

        self._image_lookup_format = image_lookup_format

    @property
    def image_lookup_org(self):
        """Gets the image_lookup_org of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501

        ImageLookupOrg is the AWS Organization ID to use for image lookup if AMI is not set.  # noqa: E501

        :return: The image_lookup_org of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :rtype: str
        """
        return self._image_lookup_org

    @image_lookup_org.setter
    def image_lookup_org(self, image_lookup_org):
        """Sets the image_lookup_org of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.

        ImageLookupOrg is the AWS Organization ID to use for image lookup if AMI is not set.  # noqa: E501

        :param image_lookup_org: The image_lookup_org of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :type: str
        """

        self._image_lookup_org = image_lookup_org

    @property
    def instance_type(self):
        """Gets the instance_type of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501

        InstanceType is the type of instance to create. Example: m4.xlarge  # noqa: E501

        :return: The instance_type of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.

        InstanceType is the type of instance to create. Example: m4.xlarge  # noqa: E501

        :param instance_type: The instance_type of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def name(self):
        """Gets the name of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501

        The name of the launch template.  # noqa: E501

        :return: The name of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.

        The name of the launch template.  # noqa: E501

        :param name: The name of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def root_volume(self):
        """Gets the root_volume of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501


        :return: The root_volume of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :rtype: IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecRootVolume
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.


        :param root_volume: The root_volume of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :type: IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecRootVolume
        """

        self._root_volume = root_volume

    @property
    def ssh_key_name(self):
        """Gets the ssh_key_name of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501

        SSHKeyName is the name of the ssh key to attach to the instance. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name)  # noqa: E501

        :return: The ssh_key_name of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :rtype: str
        """
        return self._ssh_key_name

    @ssh_key_name.setter
    def ssh_key_name(self, ssh_key_name):
        """Sets the ssh_key_name of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.

        SSHKeyName is the name of the ssh key to attach to the instance. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name)  # noqa: E501

        :param ssh_key_name: The ssh_key_name of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :type: str
        """

        self._ssh_key_name = ssh_key_name

    @property
    def version_number(self):
        """Gets the version_number of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501

        VersionNumber is the version of the launch template that is applied. Typically a new version is created when at least one of the following happens: 1) A new launch template spec is applied. 2) One or more parameters in an existing template is changed. 3) A new AMI is discovered.  # noqa: E501

        :return: The version_number of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.

        VersionNumber is the version of the launch template that is applied. Typically a new version is created when at least one of the following happens: 1) A new launch template spec is applied. 2) One or more parameters in an existing template is changed. 3) A new AMI is discovered.  # noqa: E501

        :param version_number: The version_number of this IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.  # noqa: E501
        :type: int
        """

        self._version_number = version_number

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
        if not isinstance(other, IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate):
            return True

        return self.to_dict() != other.to_dict()
