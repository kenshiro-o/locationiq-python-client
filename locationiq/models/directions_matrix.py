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


class DirectionsMatrix(object):
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
        'code': 'str',
        'distances': 'list[float]',
        'fallback_speed_cells': 'list[float]',
        'sources': 'list[DirectionsMatrixSources]',
        'destinations': 'list[DirectionsMatrixSources]'
    }

    attribute_map = {
        'code': 'code',
        'distances': 'distances',
        'fallback_speed_cells': 'fallback_speed_cells',
        'sources': 'sources',
        'destinations': 'destinations'
    }

    def __init__(self, code=None, distances=None, fallback_speed_cells=None, sources=None, destinations=None, local_vars_configuration=None):  # noqa: E501
        """DirectionsMatrix - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._distances = None
        self._fallback_speed_cells = None
        self._sources = None
        self._destinations = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if distances is not None:
            self.distances = distances
        if fallback_speed_cells is not None:
            self.fallback_speed_cells = fallback_speed_cells
        if sources is not None:
            self.sources = sources
        if destinations is not None:
            self.destinations = destinations

    @property
    def code(self):
        """Gets the code of this DirectionsMatrix.  # noqa: E501


        :return: The code of this DirectionsMatrix.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DirectionsMatrix.


        :param code: The code of this DirectionsMatrix.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def distances(self):
        """Gets the distances of this DirectionsMatrix.  # noqa: E501


        :return: The distances of this DirectionsMatrix.  # noqa: E501
        :rtype: list[float]
        """
        return self._distances

    @distances.setter
    def distances(self, distances):
        """Sets the distances of this DirectionsMatrix.


        :param distances: The distances of this DirectionsMatrix.  # noqa: E501
        :type: list[float]
        """

        self._distances = distances

    @property
    def fallback_speed_cells(self):
        """Gets the fallback_speed_cells of this DirectionsMatrix.  # noqa: E501


        :return: The fallback_speed_cells of this DirectionsMatrix.  # noqa: E501
        :rtype: list[float]
        """
        return self._fallback_speed_cells

    @fallback_speed_cells.setter
    def fallback_speed_cells(self, fallback_speed_cells):
        """Sets the fallback_speed_cells of this DirectionsMatrix.


        :param fallback_speed_cells: The fallback_speed_cells of this DirectionsMatrix.  # noqa: E501
        :type: list[float]
        """

        self._fallback_speed_cells = fallback_speed_cells

    @property
    def sources(self):
        """Gets the sources of this DirectionsMatrix.  # noqa: E501


        :return: The sources of this DirectionsMatrix.  # noqa: E501
        :rtype: list[DirectionsMatrixSources]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this DirectionsMatrix.


        :param sources: The sources of this DirectionsMatrix.  # noqa: E501
        :type: list[DirectionsMatrixSources]
        """

        self._sources = sources

    @property
    def destinations(self):
        """Gets the destinations of this DirectionsMatrix.  # noqa: E501


        :return: The destinations of this DirectionsMatrix.  # noqa: E501
        :rtype: list[DirectionsMatrixSources]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this DirectionsMatrix.


        :param destinations: The destinations of this DirectionsMatrix.  # noqa: E501
        :type: list[DirectionsMatrixSources]
        """

        self._destinations = destinations

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
        if not isinstance(other, DirectionsMatrix):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DirectionsMatrix):
            return True

        return self.to_dict() != other.to_dict()
