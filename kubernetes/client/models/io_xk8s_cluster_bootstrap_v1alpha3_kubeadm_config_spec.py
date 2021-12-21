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


class IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec(object):
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
        'cluster_configuration': 'IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfiguration',
        'disk_setup': 'IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecDiskSetup',
        'files': 'list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecFiles]',
        'format': 'str',
        'init_configuration': 'IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfiguration',
        'join_configuration': 'IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration',
        'mounts': 'list[list[str]]',
        'ntp': 'IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecNtp',
        'post_kubeadm_commands': 'list[str]',
        'pre_kubeadm_commands': 'list[str]',
        'use_experimental_retry_join': 'bool',
        'users': 'list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecUsers]',
        'verbosity': 'int'
    }

    attribute_map = {
        'cluster_configuration': 'clusterConfiguration',
        'disk_setup': 'diskSetup',
        'files': 'files',
        'format': 'format',
        'init_configuration': 'initConfiguration',
        'join_configuration': 'joinConfiguration',
        'mounts': 'mounts',
        'ntp': 'ntp',
        'post_kubeadm_commands': 'postKubeadmCommands',
        'pre_kubeadm_commands': 'preKubeadmCommands',
        'use_experimental_retry_join': 'useExperimentalRetryJoin',
        'users': 'users',
        'verbosity': 'verbosity'
    }

    def __init__(self, cluster_configuration=None, disk_setup=None, files=None, format=None, init_configuration=None, join_configuration=None, mounts=None, ntp=None, post_kubeadm_commands=None, pre_kubeadm_commands=None, use_experimental_retry_join=None, users=None, verbosity=None, local_vars_configuration=None):  # noqa: E501
        """IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_configuration = None
        self._disk_setup = None
        self._files = None
        self._format = None
        self._init_configuration = None
        self._join_configuration = None
        self._mounts = None
        self._ntp = None
        self._post_kubeadm_commands = None
        self._pre_kubeadm_commands = None
        self._use_experimental_retry_join = None
        self._users = None
        self._verbosity = None
        self.discriminator = None

        if cluster_configuration is not None:
            self.cluster_configuration = cluster_configuration
        if disk_setup is not None:
            self.disk_setup = disk_setup
        if files is not None:
            self.files = files
        if format is not None:
            self.format = format
        if init_configuration is not None:
            self.init_configuration = init_configuration
        if join_configuration is not None:
            self.join_configuration = join_configuration
        if mounts is not None:
            self.mounts = mounts
        if ntp is not None:
            self.ntp = ntp
        if post_kubeadm_commands is not None:
            self.post_kubeadm_commands = post_kubeadm_commands
        if pre_kubeadm_commands is not None:
            self.pre_kubeadm_commands = pre_kubeadm_commands
        if use_experimental_retry_join is not None:
            self.use_experimental_retry_join = use_experimental_retry_join
        if users is not None:
            self.users = users
        if verbosity is not None:
            self.verbosity = verbosity

    @property
    def cluster_configuration(self):
        """Gets the cluster_configuration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501


        :return: The cluster_configuration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfiguration
        """
        return self._cluster_configuration

    @cluster_configuration.setter
    def cluster_configuration(self, cluster_configuration):
        """Sets the cluster_configuration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.


        :param cluster_configuration: The cluster_configuration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfiguration
        """

        self._cluster_configuration = cluster_configuration

    @property
    def disk_setup(self):
        """Gets the disk_setup of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501


        :return: The disk_setup of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecDiskSetup
        """
        return self._disk_setup

    @disk_setup.setter
    def disk_setup(self, disk_setup):
        """Sets the disk_setup of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.


        :param disk_setup: The disk_setup of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecDiskSetup
        """

        self._disk_setup = disk_setup

    @property
    def files(self):
        """Gets the files of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501

        Files specifies extra files to be passed to user_data upon creation.  # noqa: E501

        :return: The files of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecFiles]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.

        Files specifies extra files to be passed to user_data upon creation.  # noqa: E501

        :param files: The files of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecFiles]
        """

        self._files = files

    @property
    def format(self):
        """Gets the format of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501

        Format specifies the output format of the bootstrap data  # noqa: E501

        :return: The format of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.

        Format specifies the output format of the bootstrap data  # noqa: E501

        :param format: The format of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["cloud-config"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def init_configuration(self):
        """Gets the init_configuration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501


        :return: The init_configuration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfiguration
        """
        return self._init_configuration

    @init_configuration.setter
    def init_configuration(self, init_configuration):
        """Sets the init_configuration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.


        :param init_configuration: The init_configuration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfiguration
        """

        self._init_configuration = init_configuration

    @property
    def join_configuration(self):
        """Gets the join_configuration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501


        :return: The join_configuration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration
        """
        return self._join_configuration

    @join_configuration.setter
    def join_configuration(self, join_configuration):
        """Sets the join_configuration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.


        :param join_configuration: The join_configuration of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration
        """

        self._join_configuration = join_configuration

    @property
    def mounts(self):
        """Gets the mounts of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501

        Mounts specifies a list of mount points to be setup.  # noqa: E501

        :return: The mounts of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: list[list[str]]
        """
        return self._mounts

    @mounts.setter
    def mounts(self, mounts):
        """Sets the mounts of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.

        Mounts specifies a list of mount points to be setup.  # noqa: E501

        :param mounts: The mounts of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: list[list[str]]
        """

        self._mounts = mounts

    @property
    def ntp(self):
        """Gets the ntp of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501


        :return: The ntp of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecNtp
        """
        return self._ntp

    @ntp.setter
    def ntp(self, ntp):
        """Sets the ntp of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.


        :param ntp: The ntp of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecNtp
        """

        self._ntp = ntp

    @property
    def post_kubeadm_commands(self):
        """Gets the post_kubeadm_commands of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501

        PostKubeadmCommands specifies extra commands to run after kubeadm runs  # noqa: E501

        :return: The post_kubeadm_commands of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._post_kubeadm_commands

    @post_kubeadm_commands.setter
    def post_kubeadm_commands(self, post_kubeadm_commands):
        """Sets the post_kubeadm_commands of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.

        PostKubeadmCommands specifies extra commands to run after kubeadm runs  # noqa: E501

        :param post_kubeadm_commands: The post_kubeadm_commands of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: list[str]
        """

        self._post_kubeadm_commands = post_kubeadm_commands

    @property
    def pre_kubeadm_commands(self):
        """Gets the pre_kubeadm_commands of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501

        PreKubeadmCommands specifies extra commands to run before kubeadm runs  # noqa: E501

        :return: The pre_kubeadm_commands of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._pre_kubeadm_commands

    @pre_kubeadm_commands.setter
    def pre_kubeadm_commands(self, pre_kubeadm_commands):
        """Sets the pre_kubeadm_commands of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.

        PreKubeadmCommands specifies extra commands to run before kubeadm runs  # noqa: E501

        :param pre_kubeadm_commands: The pre_kubeadm_commands of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: list[str]
        """

        self._pre_kubeadm_commands = pre_kubeadm_commands

    @property
    def use_experimental_retry_join(self):
        """Gets the use_experimental_retry_join of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501

        UseExperimentalRetryJoin replaces a basic kubeadm command with a shell script with retries for joins.   This is meant to be an experimental temporary workaround on some environments where joins fail due to timing (and other issues). The long term goal is to add retries to kubeadm proper and use that functionality.   This will add about 40KB to userdata   For more information, refer to https://github.com/kubernetes-sigs/cluster-api/pull/2763#discussion_r397306055.  # noqa: E501

        :return: The use_experimental_retry_join of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: bool
        """
        return self._use_experimental_retry_join

    @use_experimental_retry_join.setter
    def use_experimental_retry_join(self, use_experimental_retry_join):
        """Sets the use_experimental_retry_join of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.

        UseExperimentalRetryJoin replaces a basic kubeadm command with a shell script with retries for joins.   This is meant to be an experimental temporary workaround on some environments where joins fail due to timing (and other issues). The long term goal is to add retries to kubeadm proper and use that functionality.   This will add about 40KB to userdata   For more information, refer to https://github.com/kubernetes-sigs/cluster-api/pull/2763#discussion_r397306055.  # noqa: E501

        :param use_experimental_retry_join: The use_experimental_retry_join of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: bool
        """

        self._use_experimental_retry_join = use_experimental_retry_join

    @property
    def users(self):
        """Gets the users of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501

        Users specifies extra users to add  # noqa: E501

        :return: The users of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecUsers]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.

        Users specifies extra users to add  # noqa: E501

        :param users: The users of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecUsers]
        """

        self._users = users

    @property
    def verbosity(self):
        """Gets the verbosity of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501

        Verbosity is the number for the kubeadm log level verbosity. It overrides the `--v` flag in kubeadm commands.  # noqa: E501

        :return: The verbosity of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :rtype: int
        """
        return self._verbosity

    @verbosity.setter
    def verbosity(self, verbosity):
        """Sets the verbosity of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.

        Verbosity is the number for the kubeadm log level verbosity. It overrides the `--v` flag in kubeadm commands.  # noqa: E501

        :param verbosity: The verbosity of this IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec.  # noqa: E501
        :type: int
        """

        self._verbosity = verbosity

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
        if not isinstance(other, IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpec):
            return True

        return self.to_dict() != other.to_dict()
