import jsonstruct
import requests
import hmac
import hashlib
import settings
import urllib
import logging

from models import *

logger = logging.getLogger(__name__)


class SensCritiqueClient(object):
    auth_info = AuthInfo

    def login(self, username, password):
        token_response = requests.get(settings.HOST + '/auth/request_token', params={'app_id': 11})

        if token_response.status_code != 200:
            logger.error("ERROR on login. Status code is different than 200")
            return False

        token = token_response.json().get('request_token')

        password_md5 = hashlib.md5(password).hexdigest()
        nonce = hmac.new(str(token.get('token')), username + password_md5, hashlib.md5).hexdigest()

        login_response = requests.post(settings.HOST + '/auth/login', data={'nonce': nonce,
                                                                            'email': username,
                                                                            'pass': password,
                                                                            'token_id': str(token.get('id'))})
        if login_response.status_code != 200:
            logger.error("ERROR on login. Status code is different than 200")
            return False

        login_data = login_response.json()

        access_token = str(login_data.get('access_token'))

        self.auth_info = AuthInfo(username, access_token)
        return True

    #
    #
    #  GET DATA FOR A SPECIFIC USER
    #
    #

    """
     WARNING: This method will returns the "Movie" wishes if the user does not have
     any wish for the given universe
    """

    def get_wishes_all(self, userId, universe):
        response_object = self.send_request(Method.GET, '/users/' + userId + '/products/wish', {'type_id': universe.value[0]}, None, ProductListResponse)
        return response_object.products

    def get_userinfo(self, userId):
        return self.send_request(Method.GET, '/users/' + userId, {}, None, UserInfoResponse)

    #
    #
    #  GET DATA FOR THE LOGGED IN USER
    #
    #

    def l_get_wishes_all(self, universe):
        return self.get_wishes_all('me', universe)

    def l_get_userinfo(self):
        return self.get_userinfo('me')

    #
    #
    #  SEARCH
    #
    #

    def search(self, query, **params):
        request_params = {'query': query}

        if 'filter' in params:
            request_params['filter'] = params['filter'].value

        found_product_list_response = self.send_request(Method.GET, '/search', request_params, None, SearchResponse)
        return found_product_list_response.products

    #
    #
    #  LISTS
    #
    #

    def create_list(self, sub_universe, name, **params):
        created_list = self.send_request(Method.POST, "/users/me/lists", {}, {"subtype_id": sub_universe.value, "label": name}, ListCreationResponse)
        return created_list.list

    def get_info_list(self, list_id):
        list_info = self.send_request(Method.GET, "/lists/{id}".format(id=list_id), {}, None, ListInfoResponse)
        return list_info

    """NOT WORKING"""
    def delete_list(self, list_id):
        delete_request_status = self.send_request(Method.DELETE, "/lists/{id}".format(id=list_id), {}, None, None)
        return delete_request_status

    def get_product_list_of_list(self, list_id, **params):
        request_params = {}

        if 'limit' in params:
            request_params['limit'] = params['limit']
        else:
            request_params['limit'] = "20"

        if 'offset' in params:
            request_params['offset'] = params['offset']
        else:
            request_params['offset'] = "0"

        product_list = self.send_request(Method.GET, "/lists/{list_id}/products".format(list_id=list_id), request_params, None, ProductListResponse)
        return product_list.products

    def save_product_in_list(self, product_id, list_id, **params):
        found_product_list_response = self.send_request(Method.POST, "/lists/{list_id}/products/{product_id}".format(list_id=list_id, product_id=product_id), {}, None, ProductListResponse)
        return found_product_list_response.products

    def remove_product_in_list(self, product_id, list_id, **params):
        response = self.send_request(Method.DELETE, "/lists/{list_id}/products/{product_id}".format(list_id=list_id, product_id=product_id), {}, None, SuccessStatusResponse)
        return response.success

    #
    #
    #  RATINGS
    #
    #

    def rate_product(self, product_id, rating, **params):
        found_product_list_response = self.send_request(Method.POST, "/products/{product_id}/rate".format(product_id=product_id), {}, {"rating": rating}, SuccessStatusResponse)
        return found_product_list_response.success

    #
    #
    #   HELPERS
    #
    #

    def send_request(self, method, uri, params, data, response_object_type):

        params['access_token'] = self.auth_info.access_token
        params_sanitized = urllib.urlencode(params)

        if method == Method.GET:
            response = requests.get(settings.HOST + uri, params=params_sanitized)
        elif method == Method.POST:
            response = requests.post(settings.HOST + uri, params=params_sanitized, data=data)
        elif method == Method.PUT:
            response = requests.put(settings.HOST + uri, params=params_sanitized, data=data)
        elif method == Method.DELETE:
            response = requests.delete(settings.HOST + uri, params=params_sanitized)
        else:
            response = requests.get(settings.HOST + uri, params=params_sanitized)

        if response_object_type is not None:
            response_object = jsonstruct.decode(response.content, response_object_type)
        else:
            response_object = response.content
        return response_object
