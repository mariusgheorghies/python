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


class IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm(object):
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
        'file_parameters': 'list[IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelmFileParameters]',
        'ignore_missing_value_files': 'bool',
        'parameters': 'list[IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelmParameters]',
        'pass_credentials': 'bool',
        'release_name': 'str',
        'skip_crds': 'bool',
        'value_files': 'list[str]',
        'values': 'str',
        'version': 'str'
    }

    attribute_map = {
        'file_parameters': 'fileParameters',
        'ignore_missing_value_files': 'ignoreMissingValueFiles',
        'parameters': 'parameters',
        'pass_credentials': 'passCredentials',
        'release_name': 'releaseName',
        'skip_crds': 'skipCrds',
        'value_files': 'valueFiles',
        'values': 'values',
        'version': 'version'
    }

    def __init__(self, file_parameters=None, ignore_missing_value_files=None, parameters=None, pass_credentials=None, release_name=None, skip_crds=None, value_files=None, values=None, version=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_parameters = None
        self._ignore_missing_value_files = None
        self._parameters = None
        self._pass_credentials = None
        self._release_name = None
        self._skip_crds = None
        self._value_files = None
        self._values = None
        self._version = None
        self.discriminator = None

        if file_parameters is not None:
            self.file_parameters = file_parameters
        if ignore_missing_value_files is not None:
            self.ignore_missing_value_files = ignore_missing_value_files
        if parameters is not None:
            self.parameters = parameters
        if pass_credentials is not None:
            self.pass_credentials = pass_credentials
        if release_name is not None:
            self.release_name = release_name
        if skip_crds is not None:
            self.skip_crds = skip_crds
        if value_files is not None:
            self.value_files = value_files
        if values is not None:
            self.values = values
        if version is not None:
            self.version = version

    @property
    def file_parameters(self):
        """Gets the file_parameters of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501


        :return: The file_parameters of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :rtype: list[IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelmFileParameters]
        """
        return self._file_parameters

    @file_parameters.setter
    def file_parameters(self, file_parameters):
        """Sets the file_parameters of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.


        :param file_parameters: The file_parameters of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :type: list[IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelmFileParameters]
        """

        self._file_parameters = file_parameters

    @property
    def ignore_missing_value_files(self):
        """Gets the ignore_missing_value_files of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501


        :return: The ignore_missing_value_files of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_missing_value_files

    @ignore_missing_value_files.setter
    def ignore_missing_value_files(self, ignore_missing_value_files):
        """Sets the ignore_missing_value_files of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.


        :param ignore_missing_value_files: The ignore_missing_value_files of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :type: bool
        """

        self._ignore_missing_value_files = ignore_missing_value_files

    @property
    def parameters(self):
        """Gets the parameters of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501


        :return: The parameters of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :rtype: list[IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelmParameters]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.


        :param parameters: The parameters of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :type: list[IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelmParameters]
        """

        self._parameters = parameters

    @property
    def pass_credentials(self):
        """Gets the pass_credentials of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501


        :return: The pass_credentials of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :rtype: bool
        """
        return self._pass_credentials

    @pass_credentials.setter
    def pass_credentials(self, pass_credentials):
        """Sets the pass_credentials of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.


        :param pass_credentials: The pass_credentials of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :type: bool
        """

        self._pass_credentials = pass_credentials

    @property
    def release_name(self):
        """Gets the release_name of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501


        :return: The release_name of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :rtype: str
        """
        return self._release_name

    @release_name.setter
    def release_name(self, release_name):
        """Sets the release_name of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.


        :param release_name: The release_name of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :type: str
        """

        self._release_name = release_name

    @property
    def skip_crds(self):
        """Gets the skip_crds of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501


        :return: The skip_crds of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :rtype: bool
        """
        return self._skip_crds

    @skip_crds.setter
    def skip_crds(self, skip_crds):
        """Sets the skip_crds of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.


        :param skip_crds: The skip_crds of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :type: bool
        """

        self._skip_crds = skip_crds

    @property
    def value_files(self):
        """Gets the value_files of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501


        :return: The value_files of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :rtype: list[str]
        """
        return self._value_files

    @value_files.setter
    def value_files(self, value_files):
        """Sets the value_files of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.


        :param value_files: The value_files of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :type: list[str]
        """

        self._value_files = value_files

    @property
    def values(self):
        """Gets the values of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501


        :return: The values of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.


        :param values: The values of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :type: str
        """

        self._values = values

    @property
    def version(self):
        """Gets the version of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501


        :return: The version of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.


        :param version: The version of this IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceHelm):
            return True

        return self.to_dict() != other.to_dict()
