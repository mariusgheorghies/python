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


class IoXK8sClusterInfrastructureV1beta1AWSMachineSpec(object):
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
        'additional_security_groups': 'list[IoXK8sClusterInfrastructureV1beta1AWSMachineSpecAdditionalSecurityGroups]',
        'additional_tags': 'dict(str, str)',
        'ami': 'IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecAmi',
        'cloud_init': 'IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit',
        'failure_domain': 'str',
        'iam_instance_profile': 'str',
        'image_lookup_base_os': 'str',
        'image_lookup_format': 'str',
        'image_lookup_org': 'str',
        'instance_id': 'str',
        'instance_type': 'str',
        'network_interfaces': 'list[str]',
        'non_root_volumes': 'list[IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatusBastionNonRootVolumes]',
        'provider_id': 'str',
        'public_ip': 'bool',
        'root_volume': 'IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecRootVolume',
        'spot_market_options': 'IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecSpotMarketOptions',
        'ssh_key_name': 'str',
        'subnet': 'IoXK8sClusterInfrastructureV1beta1AWSMachineSpecSubnet',
        'tenancy': 'str',
        'uncompressed_user_data': 'bool'
    }

    attribute_map = {
        'additional_security_groups': 'additionalSecurityGroups',
        'additional_tags': 'additionalTags',
        'ami': 'ami',
        'cloud_init': 'cloudInit',
        'failure_domain': 'failureDomain',
        'iam_instance_profile': 'iamInstanceProfile',
        'image_lookup_base_os': 'imageLookupBaseOS',
        'image_lookup_format': 'imageLookupFormat',
        'image_lookup_org': 'imageLookupOrg',
        'instance_id': 'instanceID',
        'instance_type': 'instanceType',
        'network_interfaces': 'networkInterfaces',
        'non_root_volumes': 'nonRootVolumes',
        'provider_id': 'providerID',
        'public_ip': 'publicIP',
        'root_volume': 'rootVolume',
        'spot_market_options': 'spotMarketOptions',
        'ssh_key_name': 'sshKeyName',
        'subnet': 'subnet',
        'tenancy': 'tenancy',
        'uncompressed_user_data': 'uncompressedUserData'
    }

    def __init__(self, additional_security_groups=None, additional_tags=None, ami=None, cloud_init=None, failure_domain=None, iam_instance_profile=None, image_lookup_base_os=None, image_lookup_format=None, image_lookup_org=None, instance_id=None, instance_type=None, network_interfaces=None, non_root_volumes=None, provider_id=None, public_ip=None, root_volume=None, spot_market_options=None, ssh_key_name=None, subnet=None, tenancy=None, uncompressed_user_data=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterInfrastructureV1beta1AWSMachineSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._additional_security_groups = None
        self._additional_tags = None
        self._ami = None
        self._cloud_init = None
        self._failure_domain = None
        self._iam_instance_profile = None
        self._image_lookup_base_os = None
        self._image_lookup_format = None
        self._image_lookup_org = None
        self._instance_id = None
        self._instance_type = None
        self._network_interfaces = None
        self._non_root_volumes = None
        self._provider_id = None
        self._public_ip = None
        self._root_volume = None
        self._spot_market_options = None
        self._ssh_key_name = None
        self._subnet = None
        self._tenancy = None
        self._uncompressed_user_data = None
        self.discriminator = None

        if additional_security_groups is not None:
            self.additional_security_groups = additional_security_groups
        if additional_tags is not None:
            self.additional_tags = additional_tags
        if ami is not None:
            self.ami = ami
        if cloud_init is not None:
            self.cloud_init = cloud_init
        if failure_domain is not None:
            self.failure_domain = failure_domain
        if iam_instance_profile is not None:
            self.iam_instance_profile = iam_instance_profile
        if image_lookup_base_os is not None:
            self.image_lookup_base_os = image_lookup_base_os
        if image_lookup_format is not None:
            self.image_lookup_format = image_lookup_format
        if image_lookup_org is not None:
            self.image_lookup_org = image_lookup_org
        if instance_id is not None:
            self.instance_id = instance_id
        self.instance_type = instance_type
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces
        if non_root_volumes is not None:
            self.non_root_volumes = non_root_volumes
        if provider_id is not None:
            self.provider_id = provider_id
        if public_ip is not None:
            self.public_ip = public_ip
        if root_volume is not None:
            self.root_volume = root_volume
        if spot_market_options is not None:
            self.spot_market_options = spot_market_options
        if ssh_key_name is not None:
            self.ssh_key_name = ssh_key_name
        if subnet is not None:
            self.subnet = subnet
        if tenancy is not None:
            self.tenancy = tenancy
        if uncompressed_user_data is not None:
            self.uncompressed_user_data = uncompressed_user_data

    @property
    def additional_security_groups(self):
        """Gets the additional_security_groups of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        AdditionalSecurityGroups is an array of references to security groups that should be applied to the instance. These security groups would be set in addition to any security groups defined at the cluster level or in the actuator. It is possible to specify either IDs of Filters. Using Filters will cause additional requests to AWS API and if tags change the attached security groups might change too.  # noqa: E501

        :return: The additional_security_groups of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: list[IoXK8sClusterInfrastructureV1beta1AWSMachineSpecAdditionalSecurityGroups]
        """
        return self._additional_security_groups

    @additional_security_groups.setter
    def additional_security_groups(self, additional_security_groups):
        """Sets the additional_security_groups of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        AdditionalSecurityGroups is an array of references to security groups that should be applied to the instance. These security groups would be set in addition to any security groups defined at the cluster level or in the actuator. It is possible to specify either IDs of Filters. Using Filters will cause additional requests to AWS API and if tags change the attached security groups might change too.  # noqa: E501

        :param additional_security_groups: The additional_security_groups of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: list[IoXK8sClusterInfrastructureV1beta1AWSMachineSpecAdditionalSecurityGroups]
        """

        self._additional_security_groups = additional_security_groups

    @property
    def additional_tags(self):
        """Gets the additional_tags of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        AdditionalTags is an optional set of tags to add to an instance, in addition to the ones added by default by the AWS provider. If both the AWSCluster and the AWSMachine specify the same tag name with different values, the AWSMachine's value takes precedence.  # noqa: E501

        :return: The additional_tags of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._additional_tags

    @additional_tags.setter
    def additional_tags(self, additional_tags):
        """Sets the additional_tags of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        AdditionalTags is an optional set of tags to add to an instance, in addition to the ones added by default by the AWS provider. If both the AWSCluster and the AWSMachine specify the same tag name with different values, the AWSMachine's value takes precedence.  # noqa: E501

        :param additional_tags: The additional_tags of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._additional_tags = additional_tags

    @property
    def ami(self):
        """Gets the ami of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501


        :return: The ami of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecAmi
        """
        return self._ami

    @ami.setter
    def ami(self, ami):
        """Sets the ami of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.


        :param ami: The ami of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecAmi
        """

        self._ami = ami

    @property
    def cloud_init(self):
        """Gets the cloud_init of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501


        :return: The cloud_init of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit
        """
        return self._cloud_init

    @cloud_init.setter
    def cloud_init(self, cloud_init):
        """Sets the cloud_init of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.


        :param cloud_init: The cloud_init of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit
        """

        self._cloud_init = cloud_init

    @property
    def failure_domain(self):
        """Gets the failure_domain of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        FailureDomain is the failure domain unique identifier this Machine should be attached to, as defined in Cluster API. For this infrastructure provider, the ID is equivalent to an AWS Availability Zone. If multiple subnets are matched for the availability zone, the first one returned is picked.  # noqa: E501

        :return: The failure_domain of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: str
        """
        return self._failure_domain

    @failure_domain.setter
    def failure_domain(self, failure_domain):
        """Sets the failure_domain of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        FailureDomain is the failure domain unique identifier this Machine should be attached to, as defined in Cluster API. For this infrastructure provider, the ID is equivalent to an AWS Availability Zone. If multiple subnets are matched for the availability zone, the first one returned is picked.  # noqa: E501

        :param failure_domain: The failure_domain of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: str
        """

        self._failure_domain = failure_domain

    @property
    def iam_instance_profile(self):
        """Gets the iam_instance_profile of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        IAMInstanceProfile is a name of an IAM instance profile to assign to the instance  # noqa: E501

        :return: The iam_instance_profile of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: str
        """
        return self._iam_instance_profile

    @iam_instance_profile.setter
    def iam_instance_profile(self, iam_instance_profile):
        """Sets the iam_instance_profile of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        IAMInstanceProfile is a name of an IAM instance profile to assign to the instance  # noqa: E501

        :param iam_instance_profile: The iam_instance_profile of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: str
        """

        self._iam_instance_profile = iam_instance_profile

    @property
    def image_lookup_base_os(self):
        """Gets the image_lookup_base_os of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        ImageLookupBaseOS is the name of the base operating system to use for image lookup the AMI is not set.  # noqa: E501

        :return: The image_lookup_base_os of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_lookup_base_os

    @image_lookup_base_os.setter
    def image_lookup_base_os(self, image_lookup_base_os):
        """Sets the image_lookup_base_os of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        ImageLookupBaseOS is the name of the base operating system to use for image lookup the AMI is not set.  # noqa: E501

        :param image_lookup_base_os: The image_lookup_base_os of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: str
        """

        self._image_lookup_base_os = image_lookup_base_os

    @property
    def image_lookup_format(self):
        """Gets the image_lookup_format of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        ImageLookupFormat is the AMI naming format to look up the image for this machine It will be ignored if an explicit AMI is set. Supports substitutions for {{.BaseOS}} and {{.K8sVersion}} with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami-{{.BaseOS}}-?{{.K8sVersion}}-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/  # noqa: E501

        :return: The image_lookup_format of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_lookup_format

    @image_lookup_format.setter
    def image_lookup_format(self, image_lookup_format):
        """Sets the image_lookup_format of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        ImageLookupFormat is the AMI naming format to look up the image for this machine It will be ignored if an explicit AMI is set. Supports substitutions for {{.BaseOS}} and {{.K8sVersion}} with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami-{{.BaseOS}}-?{{.K8sVersion}}-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/  # noqa: E501

        :param image_lookup_format: The image_lookup_format of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: str
        """

        self._image_lookup_format = image_lookup_format

    @property
    def image_lookup_org(self):
        """Gets the image_lookup_org of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        ImageLookupOrg is the AWS Organization ID to use for image lookup if AMI is not set.  # noqa: E501

        :return: The image_lookup_org of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_lookup_org

    @image_lookup_org.setter
    def image_lookup_org(self, image_lookup_org):
        """Sets the image_lookup_org of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        ImageLookupOrg is the AWS Organization ID to use for image lookup if AMI is not set.  # noqa: E501

        :param image_lookup_org: The image_lookup_org of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: str
        """

        self._image_lookup_org = image_lookup_org

    @property
    def instance_id(self):
        """Gets the instance_id of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        InstanceID is the EC2 instance ID for this machine.  # noqa: E501

        :return: The instance_id of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        InstanceID is the EC2 instance ID for this machine.  # noqa: E501

        :param instance_id: The instance_id of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        InstanceType is the type of instance to create. Example: m4.xlarge  # noqa: E501

        :return: The instance_type of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        InstanceType is the type of instance to create. Example: m4.xlarge  # noqa: E501

        :param instance_type: The instance_type of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and instance_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instance_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instance_type is not None and len(instance_type) < 2):
            raise ValueError("Invalid value for `instance_type`, length must be greater than or equal to `2`")  # noqa: E501

        self._instance_type = instance_type

    @property
    def network_interfaces(self):
        """Gets the network_interfaces of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        NetworkInterfaces is a list of ENIs to associate with the instance. A maximum of 2 may be specified.  # noqa: E501

        :return: The network_interfaces of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        """Sets the network_interfaces of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        NetworkInterfaces is a list of ENIs to associate with the instance. A maximum of 2 may be specified.  # noqa: E501

        :param network_interfaces: The network_interfaces of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: list[str]
        """

        self._network_interfaces = network_interfaces

    @property
    def non_root_volumes(self):
        """Gets the non_root_volumes of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        Configuration options for the non root storage volumes.  # noqa: E501

        :return: The non_root_volumes of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: list[IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatusBastionNonRootVolumes]
        """
        return self._non_root_volumes

    @non_root_volumes.setter
    def non_root_volumes(self, non_root_volumes):
        """Sets the non_root_volumes of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        Configuration options for the non root storage volumes.  # noqa: E501

        :param non_root_volumes: The non_root_volumes of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: list[IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatusBastionNonRootVolumes]
        """

        self._non_root_volumes = non_root_volumes

    @property
    def provider_id(self):
        """Gets the provider_id of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        ProviderID is the unique identifier as specified by the cloud provider.  # noqa: E501

        :return: The provider_id of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        ProviderID is the unique identifier as specified by the cloud provider.  # noqa: E501

        :param provider_id: The provider_id of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

    @property
    def public_ip(self):
        """Gets the public_ip of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        PublicIP specifies whether the instance should get a public IP. Precedence for this setting is as follows: 1. This field if set 2. Cluster/flavor setting 3. Subnet default  # noqa: E501

        :return: The public_ip of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: bool
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        PublicIP specifies whether the instance should get a public IP. Precedence for this setting is as follows: 1. This field if set 2. Cluster/flavor setting 3. Subnet default  # noqa: E501

        :param public_ip: The public_ip of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: bool
        """

        self._public_ip = public_ip

    @property
    def root_volume(self):
        """Gets the root_volume of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501


        :return: The root_volume of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecRootVolume
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.


        :param root_volume: The root_volume of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecRootVolume
        """

        self._root_volume = root_volume

    @property
    def spot_market_options(self):
        """Gets the spot_market_options of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501


        :return: The spot_market_options of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecSpotMarketOptions
        """
        return self._spot_market_options

    @spot_market_options.setter
    def spot_market_options(self, spot_market_options):
        """Sets the spot_market_options of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.


        :param spot_market_options: The spot_market_options of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecSpotMarketOptions
        """

        self._spot_market_options = spot_market_options

    @property
    def ssh_key_name(self):
        """Gets the ssh_key_name of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        SSHKeyName is the name of the ssh key to attach to the instance. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name)  # noqa: E501

        :return: The ssh_key_name of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: str
        """
        return self._ssh_key_name

    @ssh_key_name.setter
    def ssh_key_name(self, ssh_key_name):
        """Sets the ssh_key_name of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        SSHKeyName is the name of the ssh key to attach to the instance. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name)  # noqa: E501

        :param ssh_key_name: The ssh_key_name of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: str
        """

        self._ssh_key_name = ssh_key_name

    @property
    def subnet(self):
        """Gets the subnet of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501


        :return: The subnet of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: IoXK8sClusterInfrastructureV1beta1AWSMachineSpecSubnet
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.


        :param subnet: The subnet of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: IoXK8sClusterInfrastructureV1beta1AWSMachineSpecSubnet
        """

        self._subnet = subnet

    @property
    def tenancy(self):
        """Gets the tenancy of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        Tenancy indicates if instance should run on shared or single-tenant hardware.  # noqa: E501

        :return: The tenancy of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        """Sets the tenancy of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        Tenancy indicates if instance should run on shared or single-tenant hardware.  # noqa: E501

        :param tenancy: The tenancy of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["default", "dedicated", "host"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and tenancy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `tenancy` ({0}), must be one of {1}"  # noqa: E501
                .format(tenancy, allowed_values)
            )

        self._tenancy = tenancy

    @property
    def uncompressed_user_data(self):
        """Gets the uncompressed_user_data of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501

        UncompressedUserData specify whether the user data is gzip-compressed before it is sent to ec2 instance. cloud-init has built-in support for gzip-compressed user data user data stored in aws secret manager is always gzip-compressed.  # noqa: E501

        :return: The uncompressed_user_data of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :rtype: bool
        """
        return self._uncompressed_user_data

    @uncompressed_user_data.setter
    def uncompressed_user_data(self, uncompressed_user_data):
        """Sets the uncompressed_user_data of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.

        UncompressedUserData specify whether the user data is gzip-compressed before it is sent to ec2 instance. cloud-init has built-in support for gzip-compressed user data user data stored in aws secret manager is always gzip-compressed.  # noqa: E501

        :param uncompressed_user_data: The uncompressed_user_data of this IoXK8sClusterInfrastructureV1beta1AWSMachineSpec.  # noqa: E501
        :type: bool
        """

        self._uncompressed_user_data = uncompressed_user_data

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
        if not isinstance(other, IoXK8sClusterInfrastructureV1beta1AWSMachineSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterInfrastructureV1beta1AWSMachineSpec):
            return True

        return self.to_dict() != other.to_dict()
