# coding: utf-8

"""
    LocationIQ

    LocationIQ provides flexible enterprise-grade location based solutions. We work with developers, startups and enterprises worldwide serving billions of requests everyday. This page provides an overview of the technical aspects of our API and will help you get started.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from locationiq.api_client import ApiClient
from locationiq.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ReverseApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def reverse(self, lat, lon, format, normalizecity, **kwargs):  # noqa: E501
        """Reverse Geocoding  # noqa: E501

        Reverse geocoding is the process of converting a coordinate or location (latitude, longitude) to a readable address or place name. This permits the identification of nearby street addresses, places, and/or area subdivisions such as a neighborhood, county, state, or country.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reverse(lat, lon, format, normalizecity, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param float lat: Latitude of the location to generate an address for. (required)
        :param float lon: Longitude of the location to generate an address for. (required)
        :param str format: Format to geocode. Only JSON supported for SDKs (required)
        :param int normalizecity: Normalizes village to city level data to city (required)
        :param int addressdetails: Include a breakdown of the address into elements. Defaults to 1.
        :param str accept_language: Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language=native
        :param int namedetails: Include a list of alternative names in the results. These may include language variants, references, operator and brand.
        :param int extratags: Include additional information in the result if available, e.g. wikipedia link, opening hours.
        :param int statecode: Adds state or province code when available to the statecode key inside the address element. Currently supported for addresses in the USA, Canada and Australia. Defaults to 0
        :param int showdistance: Returns the straight line distance (meters) between the input location and the result's location. Value is set in the distance key of the response. Defaults to 0 [0,1]
        :param int postaladdress: Returns address inside the postaladdress key, that is specifically formatted for each country. Currently supported for addresses in Germany. Defaults to 0 [0,1]
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Location
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.reverse_with_http_info(lat, lon, format, normalizecity, **kwargs)  # noqa: E501

    def reverse_with_http_info(self, lat, lon, format, normalizecity, **kwargs):  # noqa: E501
        """Reverse Geocoding  # noqa: E501

        Reverse geocoding is the process of converting a coordinate or location (latitude, longitude) to a readable address or place name. This permits the identification of nearby street addresses, places, and/or area subdivisions such as a neighborhood, county, state, or country.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reverse_with_http_info(lat, lon, format, normalizecity, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param float lat: Latitude of the location to generate an address for. (required)
        :param float lon: Longitude of the location to generate an address for. (required)
        :param str format: Format to geocode. Only JSON supported for SDKs (required)
        :param int normalizecity: Normalizes village to city level data to city (required)
        :param int addressdetails: Include a breakdown of the address into elements. Defaults to 1.
        :param str accept_language: Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language=native
        :param int namedetails: Include a list of alternative names in the results. These may include language variants, references, operator and brand.
        :param int extratags: Include additional information in the result if available, e.g. wikipedia link, opening hours.
        :param int statecode: Adds state or province code when available to the statecode key inside the address element. Currently supported for addresses in the USA, Canada and Australia. Defaults to 0
        :param int showdistance: Returns the straight line distance (meters) between the input location and the result's location. Value is set in the distance key of the response. Defaults to 0 [0,1]
        :param int postaladdress: Returns address inside the postaladdress key, that is specifically formatted for each country. Currently supported for addresses in Germany. Defaults to 0 [0,1]
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Location, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['lat', 'lon', 'format', 'normalizecity', 'addressdetails', 'accept_language', 'namedetails', 'extratags', 'statecode', 'showdistance', 'postaladdress']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reverse" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'lat' is set
        if self.api_client.client_side_validation and ('lat' not in local_var_params or  # noqa: E501
                                                        local_var_params['lat'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `lat` when calling `reverse`")  # noqa: E501
        # verify the required parameter 'lon' is set
        if self.api_client.client_side_validation and ('lon' not in local_var_params or  # noqa: E501
                                                        local_var_params['lon'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `lon` when calling `reverse`")  # noqa: E501
        # verify the required parameter 'format' is set
        if self.api_client.client_side_validation and ('format' not in local_var_params or  # noqa: E501
                                                        local_var_params['format'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `format` when calling `reverse`")  # noqa: E501
        # verify the required parameter 'normalizecity' is set
        if self.api_client.client_side_validation and ('normalizecity' not in local_var_params or  # noqa: E501
                                                        local_var_params['normalizecity'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `normalizecity` when calling `reverse`")  # noqa: E501

        if self.api_client.client_side_validation and 'lat' in local_var_params and local_var_params['lat'] > 90:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `lat` when calling `reverse`, must be a value less than or equal to `90`")  # noqa: E501
        if self.api_client.client_side_validation and 'lat' in local_var_params and local_var_params['lat'] < -90:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `lat` when calling `reverse`, must be a value greater than or equal to `-90`")  # noqa: E501
        if self.api_client.client_side_validation and 'lon' in local_var_params and local_var_params['lon'] > 180:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `lon` when calling `reverse`, must be a value less than or equal to `180`")  # noqa: E501
        if self.api_client.client_side_validation and 'lon' in local_var_params and local_var_params['lon'] < -180:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `lon` when calling `reverse`, must be a value greater than or equal to `-180`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'lat' in local_var_params and local_var_params['lat'] is not None:  # noqa: E501
            query_params.append(('lat', local_var_params['lat']))  # noqa: E501
        if 'lon' in local_var_params and local_var_params['lon'] is not None:  # noqa: E501
            query_params.append(('lon', local_var_params['lon']))  # noqa: E501
        if 'format' in local_var_params and local_var_params['format'] is not None:  # noqa: E501
            query_params.append(('format', local_var_params['format']))  # noqa: E501
        if 'normalizecity' in local_var_params and local_var_params['normalizecity'] is not None:  # noqa: E501
            query_params.append(('normalizecity', local_var_params['normalizecity']))  # noqa: E501
        if 'addressdetails' in local_var_params and local_var_params['addressdetails'] is not None:  # noqa: E501
            query_params.append(('addressdetails', local_var_params['addressdetails']))  # noqa: E501
        if 'accept_language' in local_var_params and local_var_params['accept_language'] is not None:  # noqa: E501
            query_params.append(('accept-language', local_var_params['accept_language']))  # noqa: E501
        if 'namedetails' in local_var_params and local_var_params['namedetails'] is not None:  # noqa: E501
            query_params.append(('namedetails', local_var_params['namedetails']))  # noqa: E501
        if 'extratags' in local_var_params and local_var_params['extratags'] is not None:  # noqa: E501
            query_params.append(('extratags', local_var_params['extratags']))  # noqa: E501
        if 'statecode' in local_var_params and local_var_params['statecode'] is not None:  # noqa: E501
            query_params.append(('statecode', local_var_params['statecode']))  # noqa: E501
        if 'showdistance' in local_var_params and local_var_params['showdistance'] is not None:  # noqa: E501
            query_params.append(('showdistance', local_var_params['showdistance']))  # noqa: E501
        if 'postaladdress' in local_var_params and local_var_params['postaladdress'] is not None:  # noqa: E501
            query_params.append(('postaladdress', local_var_params['postaladdress']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['key']  # noqa: E501

        return self.api_client.call_api(
            '/reverse.php', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Location',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
