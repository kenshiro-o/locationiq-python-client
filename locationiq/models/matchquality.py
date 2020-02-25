# coding: utf-8

"""
    LocationIQ

    LocationIQ provides flexible enterprise-grade location based solutions. We work with developers, startups and enterprises worldwide serving billions of requests everyday. This page provides an overview of the technical aspects of our API and will help you get started.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from locationiq.configuration import Configuration


class Matchquality(object):
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
        'matchcode': 'str',
        'matchtype': 'str',
        'matchlevel': 'str'
    }

    attribute_map = {
        'matchcode': 'matchcode',
        'matchtype': 'matchtype',
        'matchlevel': 'matchlevel'
    }

    def __init__(self, matchcode=None, matchtype=None, matchlevel=None, local_vars_configuration=None):  # noqa: E501
        """Matchquality - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._matchcode = None
        self._matchtype = None
        self._matchlevel = None
        self.discriminator = None

        if matchcode is not None:
            self.matchcode = matchcode
        if matchtype is not None:
            self.matchtype = matchtype
        if matchlevel is not None:
            self.matchlevel = matchlevel

    @property
    def matchcode(self):
        """Gets the matchcode of this Matchquality.  # noqa: E501


        :return: The matchcode of this Matchquality.  # noqa: E501
        :rtype: str
        """
        return self._matchcode

    @matchcode.setter
    def matchcode(self, matchcode):
        """Sets the matchcode of this Matchquality.


        :param matchcode: The matchcode of this Matchquality.  # noqa: E501
        :type: str
        """

        self._matchcode = matchcode

    @property
    def matchtype(self):
        """Gets the matchtype of this Matchquality.  # noqa: E501


        :return: The matchtype of this Matchquality.  # noqa: E501
        :rtype: str
        """
        return self._matchtype

    @matchtype.setter
    def matchtype(self, matchtype):
        """Sets the matchtype of this Matchquality.


        :param matchtype: The matchtype of this Matchquality.  # noqa: E501
        :type: str
        """

        self._matchtype = matchtype

    @property
    def matchlevel(self):
        """Gets the matchlevel of this Matchquality.  # noqa: E501


        :return: The matchlevel of this Matchquality.  # noqa: E501
        :rtype: str
        """
        return self._matchlevel

    @matchlevel.setter
    def matchlevel(self, matchlevel):
        """Sets the matchlevel of this Matchquality.


        :param matchlevel: The matchlevel of this Matchquality.  # noqa: E501
        :type: str
        """

        self._matchlevel = matchlevel

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
        if not isinstance(other, Matchquality):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Matchquality):
            return True

        return self.to_dict() != other.to_dict()
