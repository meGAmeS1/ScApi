# coding: utf-8

"""
    SensCritique Mobile API

    Unofficial SensCritique API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class WishesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def users_user_id_products_wish_get(self, user_id, access_token, **kwargs):
        """
        User wishes
        Returns the list of the wishes for a given user

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.users_user_id_products_wish_get(user_id, access_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User id (use 'me' for logged in user) (required)
        :param str access_token: Authenticated token (required)
        :return: PaginatedProductList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.users_user_id_products_wish_get_with_http_info(user_id, access_token, **kwargs)
        else:
            (data) = self.users_user_id_products_wish_get_with_http_info(user_id, access_token, **kwargs)
            return data

    def users_user_id_products_wish_get_with_http_info(self, user_id, access_token, **kwargs):
        """
        User wishes
        Returns the list of the wishes for a given user

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.users_user_id_products_wish_get_with_http_info(user_id, access_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User id (use 'me' for logged in user) (required)
        :param str access_token: Authenticated token (required)
        :return: PaginatedProductList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_user_id_products_wish_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `users_user_id_products_wish_get`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `users_user_id_products_wish_get`")

        resource_path = '/users/{user_id}/products/wish'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PaginatedProductList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
