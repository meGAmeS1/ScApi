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

from pprint import pformat
from six import iteritems
import re


class ListCreationResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, success=None, list=None):
        """
        ListCreationResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'int',
            'success': 'bool',
            'list': 'List'
        }

        self.attribute_map = {
            'code': 'code',
            'success': 'success',
            'list': 'list'
        }

        self._code = code
        self._success = success
        self._list = list

    @property
    def code(self):
        """
        Gets the code of this ListCreationResponse.
        

        :return: The code of this ListCreationResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ListCreationResponse.
        

        :param code: The code of this ListCreationResponse.
        :type: int
        """

        self._code = code

    @property
    def success(self):
        """
        Gets the success of this ListCreationResponse.
        

        :return: The success of this ListCreationResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this ListCreationResponse.
        

        :param success: The success of this ListCreationResponse.
        :type: bool
        """

        self._success = success

    @property
    def list(self):
        """
        Gets the list of this ListCreationResponse.


        :return: The list of this ListCreationResponse.
        :rtype: List
        """
        return self._list

    @list.setter
    def list(self, list):
        """
        Sets the list of this ListCreationResponse.


        :param list: The list of this ListCreationResponse.
        :type: List
        """

        self._list = list

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
