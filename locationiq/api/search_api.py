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


class SearchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search(self, q, format, normalizecity, **kwargs):  # noqa: E501
        """Forward Geocoding  # noqa: E501

        The Search API allows converting addresses, such as a street address, into geographic coordinates (latitude and longitude). These coordinates can serve various use-cases, from placing markers on a map to helping algorithms determine nearby bus stops. This process is also known as Forward Geocoding.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search(q, format, normalizecity, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str q: Address to geocode (required)
        :param str format: Format to geocode. Only JSON supported for SDKs (required)
        :param int normalizecity: For responses with no city value in the address section, the next available element in this order - city_district, locality, town, borough, municipality, village, hamlet, quarter, neighbourhood - from the address section will be normalized to city. Defaults to 1 for SDKs. (required)
        :param int addressdetails: Include a breakdown of the address into elements. Defaults to 0.
        :param str viewbox: The preferred area to find search results.  To restrict results to those within the viewbox, use along with the bounded option. Tuple of 4 floats. Any two corner points of the box - `max_lon,max_lat,min_lon,min_lat` or `min_lon,min_lat,max_lon,max_lat` - are accepted in any order as long as they span a real box. 
        :param int bounded: Restrict the results to only items contained with the viewbox
        :param int limit: Limit the number of returned results. Default is 10.
        :param str accept_language: Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language=native
        :param str countrycodes: Limit search to a list of countries.
        :param int namedetails: Include a list of alternative names in the results. These may include language variants, references, operator and brand.
        :param int dedupe: Sometimes you have several objects in OSM identifying the same place or object in reality. The simplest case is a street being split in many different OSM ways due to different characteristics. Nominatim will attempt to detect such duplicates and only return one match; this is controlled by the dedupe parameter which defaults to 1. Since the limit is, for reasons of efficiency, enforced before and not after de-duplicating, it is possible that de-duplicating leaves you with less results than requested.
        :param int extratags: Include additional information in the result if available, e.g. wikipedia link, opening hours.
        :param int statecode: Adds state or province code when available to the statecode key inside the address element. Currently supported for addresses in the USA, Canada and Australia. Defaults to 0
        :param int matchquality: Returns additional information about quality of the result in a matchquality object. Read more Defaults to 0 [0,1]
        :param int postaladdress: Returns address inside the postaladdress key, that is specifically formatted for each country. Currently supported for addresses in Germany. Defaults to 0 [0,1]
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Location]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.search_with_http_info(q, format, normalizecity, **kwargs)  # noqa: E501

    def search_with_http_info(self, q, format, normalizecity, **kwargs):  # noqa: E501
        """Forward Geocoding  # noqa: E501

        The Search API allows converting addresses, such as a street address, into geographic coordinates (latitude and longitude). These coordinates can serve various use-cases, from placing markers on a map to helping algorithms determine nearby bus stops. This process is also known as Forward Geocoding.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_with_http_info(q, format, normalizecity, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str q: Address to geocode (required)
        :param str format: Format to geocode. Only JSON supported for SDKs (required)
        :param int normalizecity: For responses with no city value in the address section, the next available element in this order - city_district, locality, town, borough, municipality, village, hamlet, quarter, neighbourhood - from the address section will be normalized to city. Defaults to 1 for SDKs. (required)
        :param int addressdetails: Include a breakdown of the address into elements. Defaults to 0.
        :param str viewbox: The preferred area to find search results.  To restrict results to those within the viewbox, use along with the bounded option. Tuple of 4 floats. Any two corner points of the box - `max_lon,max_lat,min_lon,min_lat` or `min_lon,min_lat,max_lon,max_lat` - are accepted in any order as long as they span a real box. 
        :param int bounded: Restrict the results to only items contained with the viewbox
        :param int limit: Limit the number of returned results. Default is 10.
        :param str accept_language: Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language=native
        :param str countrycodes: Limit search to a list of countries.
        :param int namedetails: Include a list of alternative names in the results. These may include language variants, references, operator and brand.
        :param int dedupe: Sometimes you have several objects in OSM identifying the same place or object in reality. The simplest case is a street being split in many different OSM ways due to different characteristics. Nominatim will attempt to detect such duplicates and only return one match; this is controlled by the dedupe parameter which defaults to 1. Since the limit is, for reasons of efficiency, enforced before and not after de-duplicating, it is possible that de-duplicating leaves you with less results than requested.
        :param int extratags: Include additional information in the result if available, e.g. wikipedia link, opening hours.
        :param int statecode: Adds state or province code when available to the statecode key inside the address element. Currently supported for addresses in the USA, Canada and Australia. Defaults to 0
        :param int matchquality: Returns additional information about quality of the result in a matchquality object. Read more Defaults to 0 [0,1]
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
        :return: tuple(list[Location], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['q', 'format', 'normalizecity', 'addressdetails', 'viewbox', 'bounded', 'limit', 'accept_language', 'countrycodes', 'namedetails', 'dedupe', 'extratags', 'statecode', 'matchquality', 'postaladdress']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'q' is set
        if self.api_client.client_side_validation and ('q' not in local_var_params or  # noqa: E501
                                                        local_var_params['q'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `q` when calling `search`")  # noqa: E501
        # verify the required parameter 'format' is set
        if self.api_client.client_side_validation and ('format' not in local_var_params or  # noqa: E501
                                                        local_var_params['format'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `format` when calling `search`")  # noqa: E501
        # verify the required parameter 'normalizecity' is set
        if self.api_client.client_side_validation and ('normalizecity' not in local_var_params or  # noqa: E501
                                                        local_var_params['normalizecity'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `normalizecity` when calling `search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in local_var_params and local_var_params['q'] is not None:  # noqa: E501
            query_params.append(('q', local_var_params['q']))  # noqa: E501
        if 'format' in local_var_params and local_var_params['format'] is not None:  # noqa: E501
            query_params.append(('format', local_var_params['format']))  # noqa: E501
        if 'normalizecity' in local_var_params and local_var_params['normalizecity'] is not None:  # noqa: E501
            query_params.append(('normalizecity', local_var_params['normalizecity']))  # noqa: E501
        if 'addressdetails' in local_var_params and local_var_params['addressdetails'] is not None:  # noqa: E501
            query_params.append(('addressdetails', local_var_params['addressdetails']))  # noqa: E501
        if 'viewbox' in local_var_params and local_var_params['viewbox'] is not None:  # noqa: E501
            query_params.append(('viewbox', local_var_params['viewbox']))  # noqa: E501
        if 'bounded' in local_var_params and local_var_params['bounded'] is not None:  # noqa: E501
            query_params.append(('bounded', local_var_params['bounded']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'accept_language' in local_var_params and local_var_params['accept_language'] is not None:  # noqa: E501
            query_params.append(('accept-language', local_var_params['accept_language']))  # noqa: E501
        if 'countrycodes' in local_var_params and local_var_params['countrycodes'] is not None:  # noqa: E501
            query_params.append(('countrycodes', local_var_params['countrycodes']))  # noqa: E501
        if 'namedetails' in local_var_params and local_var_params['namedetails'] is not None:  # noqa: E501
            query_params.append(('namedetails', local_var_params['namedetails']))  # noqa: E501
        if 'dedupe' in local_var_params and local_var_params['dedupe'] is not None:  # noqa: E501
            query_params.append(('dedupe', local_var_params['dedupe']))  # noqa: E501
        if 'extratags' in local_var_params and local_var_params['extratags'] is not None:  # noqa: E501
            query_params.append(('extratags', local_var_params['extratags']))  # noqa: E501
        if 'statecode' in local_var_params and local_var_params['statecode'] is not None:  # noqa: E501
            query_params.append(('statecode', local_var_params['statecode']))  # noqa: E501
        if 'matchquality' in local_var_params and local_var_params['matchquality'] is not None:  # noqa: E501
            query_params.append(('matchquality', local_var_params['matchquality']))  # noqa: E501
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
            '/search.php', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Location]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
