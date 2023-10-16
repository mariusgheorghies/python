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


class IoExternalSecretsGeneratorsV1alpha1PasswordSpec(object):
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
        'allow_repeat': 'bool',
        'digits': 'int',
        'length': 'int',
        'no_upper': 'bool',
        'symbol_characters': 'str',
        'symbols': 'int'
    }

    attribute_map = {
        'allow_repeat': 'allowRepeat',
        'digits': 'digits',
        'length': 'length',
        'no_upper': 'noUpper',
        'symbol_characters': 'symbolCharacters',
        'symbols': 'symbols'
    }

    def __init__(self, allow_repeat=None, digits=None, length=None, no_upper=None, symbol_characters=None, symbols=None, local_vars_configuration=None):  # noqa: E501
        """IoExternalSecretsGeneratorsV1alpha1PasswordSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allow_repeat = None
        self._digits = None
        self._length = None
        self._no_upper = None
        self._symbol_characters = None
        self._symbols = None
        self.discriminator = None

        self.allow_repeat = allow_repeat
        if digits is not None:
            self.digits = digits
        self.length = length
        self.no_upper = no_upper
        if symbol_characters is not None:
            self.symbol_characters = symbol_characters
        if symbols is not None:
            self.symbols = symbols

    @property
    def allow_repeat(self):
        """Gets the allow_repeat of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501

        set AllowRepeat to true to allow repeating characters.  # noqa: E501

        :return: The allow_repeat of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501
        :rtype: bool
        """
        return self._allow_repeat

    @allow_repeat.setter
    def allow_repeat(self, allow_repeat):
        """Sets the allow_repeat of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.

        set AllowRepeat to true to allow repeating characters.  # noqa: E501

        :param allow_repeat: The allow_repeat of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and allow_repeat is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_repeat`, must not be `None`")  # noqa: E501

        self._allow_repeat = allow_repeat

    @property
    def digits(self):
        """Gets the digits of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501

        Digits specifies the number of digits in the generated password. If omitted it defaults to 25% of the length of the password  # noqa: E501

        :return: The digits of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501
        :rtype: int
        """
        return self._digits

    @digits.setter
    def digits(self, digits):
        """Sets the digits of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.

        Digits specifies the number of digits in the generated password. If omitted it defaults to 25% of the length of the password  # noqa: E501

        :param digits: The digits of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501
        :type: int
        """

        self._digits = digits

    @property
    def length(self):
        """Gets the length of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501

        Length of the password to be generated. Defaults to 24  # noqa: E501

        :return: The length of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.

        Length of the password to be generated. Defaults to 24  # noqa: E501

        :param length: The length of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and length is None:  # noqa: E501
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def no_upper(self):
        """Gets the no_upper of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501

        Set NoUpper to disable uppercase characters  # noqa: E501

        :return: The no_upper of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501
        :rtype: bool
        """
        return self._no_upper

    @no_upper.setter
    def no_upper(self, no_upper):
        """Sets the no_upper of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.

        Set NoUpper to disable uppercase characters  # noqa: E501

        :param no_upper: The no_upper of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and no_upper is None:  # noqa: E501
            raise ValueError("Invalid value for `no_upper`, must not be `None`")  # noqa: E501

        self._no_upper = no_upper

    @property
    def symbol_characters(self):
        """Gets the symbol_characters of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501

        SymbolCharacters specifies the special characters that should be used in the generated password.  # noqa: E501

        :return: The symbol_characters of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501
        :rtype: str
        """
        return self._symbol_characters

    @symbol_characters.setter
    def symbol_characters(self, symbol_characters):
        """Sets the symbol_characters of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.

        SymbolCharacters specifies the special characters that should be used in the generated password.  # noqa: E501

        :param symbol_characters: The symbol_characters of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501
        :type: str
        """

        self._symbol_characters = symbol_characters

    @property
    def symbols(self):
        """Gets the symbols of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501

        Symbols specifies the number of symbol characters in the generated password. If omitted it defaults to 25% of the length of the password  # noqa: E501

        :return: The symbols of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501
        :rtype: int
        """
        return self._symbols

    @symbols.setter
    def symbols(self, symbols):
        """Sets the symbols of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.

        Symbols specifies the number of symbol characters in the generated password. If omitted it defaults to 25% of the length of the password  # noqa: E501

        :param symbols: The symbols of this IoExternalSecretsGeneratorsV1alpha1PasswordSpec.  # noqa: E501
        :type: int
        """

        self._symbols = symbols

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
        if not isinstance(other, IoExternalSecretsGeneratorsV1alpha1PasswordSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoExternalSecretsGeneratorsV1alpha1PasswordSpec):
            return True

        return self.to_dict() != other.to_dict()