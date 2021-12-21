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


class V1WindowsSecurityContextOptions(object):
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
        'gmsa_credential_spec': 'str',
        'gmsa_credential_spec_name': 'str',
        'run_as_user_name': 'str'
    }

    attribute_map = {
        'gmsa_credential_spec': 'gmsaCredentialSpec',
        'gmsa_credential_spec_name': 'gmsaCredentialSpecName',
        'run_as_user_name': 'runAsUserName'
    }

    def __init__(self, gmsa_credential_spec=None, gmsa_credential_spec_name=None, run_as_user_name=None, local_vars_configuration=None):  # noqa: E501
        """V1WindowsSecurityContextOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gmsa_credential_spec = None
        self._gmsa_credential_spec_name = None
        self._run_as_user_name = None
        self.discriminator = None

        if gmsa_credential_spec is not None:
            self.gmsa_credential_spec = gmsa_credential_spec
        if gmsa_credential_spec_name is not None:
            self.gmsa_credential_spec_name = gmsa_credential_spec_name
        if run_as_user_name is not None:
            self.run_as_user_name = run_as_user_name

    @property
    def gmsa_credential_spec(self):
        """Gets the gmsa_credential_spec of this V1WindowsSecurityContextOptions.  # noqa: E501

        GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.  # noqa: E501

        :return: The gmsa_credential_spec of this V1WindowsSecurityContextOptions.  # noqa: E501
        :rtype: str
        """
        return self._gmsa_credential_spec

    @gmsa_credential_spec.setter
    def gmsa_credential_spec(self, gmsa_credential_spec):
        """Sets the gmsa_credential_spec of this V1WindowsSecurityContextOptions.

        GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.  # noqa: E501

        :param gmsa_credential_spec: The gmsa_credential_spec of this V1WindowsSecurityContextOptions.  # noqa: E501
        :type: str
        """

        self._gmsa_credential_spec = gmsa_credential_spec

    @property
    def gmsa_credential_spec_name(self):
        """Gets the gmsa_credential_spec_name of this V1WindowsSecurityContextOptions.  # noqa: E501

        GMSACredentialSpecName is the name of the GMSA credential spec to use.  # noqa: E501

        :return: The gmsa_credential_spec_name of this V1WindowsSecurityContextOptions.  # noqa: E501
        :rtype: str
        """
        return self._gmsa_credential_spec_name

    @gmsa_credential_spec_name.setter
    def gmsa_credential_spec_name(self, gmsa_credential_spec_name):
        """Sets the gmsa_credential_spec_name of this V1WindowsSecurityContextOptions.

        GMSACredentialSpecName is the name of the GMSA credential spec to use.  # noqa: E501

        :param gmsa_credential_spec_name: The gmsa_credential_spec_name of this V1WindowsSecurityContextOptions.  # noqa: E501
        :type: str
        """

        self._gmsa_credential_spec_name = gmsa_credential_spec_name

    @property
    def run_as_user_name(self):
        """Gets the run_as_user_name of this V1WindowsSecurityContextOptions.  # noqa: E501

        The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.  # noqa: E501

        :return: The run_as_user_name of this V1WindowsSecurityContextOptions.  # noqa: E501
        :rtype: str
        """
        return self._run_as_user_name

    @run_as_user_name.setter
    def run_as_user_name(self, run_as_user_name):
        """Sets the run_as_user_name of this V1WindowsSecurityContextOptions.

        The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.  # noqa: E501

        :param run_as_user_name: The run_as_user_name of this V1WindowsSecurityContextOptions.  # noqa: E501
        :type: str
        """

        self._run_as_user_name = run_as_user_name

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
        if not isinstance(other, V1WindowsSecurityContextOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1WindowsSecurityContextOptions):
            return True

        return self.to_dict() != other.to_dict()
