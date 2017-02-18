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


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, username=None, displayed_name=None, first_name=None, last_name=None, gender_label=None):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'username': 'str',
            'displayed_name': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'gender_label': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'displayed_name': 'displayed_name',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'gender_label': 'gender_label'
        }

        self._id = id
        self._username = username
        self._displayed_name = displayed_name
        self._first_name = first_name
        self._last_name = last_name
        self._gender_label = gender_label

    @property
    def id(self):
        """
        Gets the id of this User.
        

        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        

        :param id: The id of this User.
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """
        Gets the username of this User.
        

        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this User.
        

        :param username: The username of this User.
        :type: str
        """

        self._username = username

    @property
    def displayed_name(self):
        """
        Gets the displayed_name of this User.
        

        :return: The displayed_name of this User.
        :rtype: str
        """
        return self._displayed_name

    @displayed_name.setter
    def displayed_name(self, displayed_name):
        """
        Sets the displayed_name of this User.
        

        :param displayed_name: The displayed_name of this User.
        :type: str
        """

        self._displayed_name = displayed_name

    @property
    def first_name(self):
        """
        Gets the first_name of this User.
        

        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this User.
        

        :param first_name: The first_name of this User.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this User.
        

        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this User.
        

        :param last_name: The last_name of this User.
        :type: str
        """

        self._last_name = last_name

    @property
    def gender_label(self):
        """
        Gets the gender_label of this User.
        

        :return: The gender_label of this User.
        :rtype: str
        """
        return self._gender_label

    @gender_label.setter
    def gender_label(self, gender_label):
        """
        Sets the gender_label of this User.
        

        :param gender_label: The gender_label of this User.
        :type: str
        """

        self._gender_label = gender_label

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