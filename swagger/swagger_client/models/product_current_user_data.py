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


class ProductCurrentUserData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, rating_scout_count=None, rating_scout_average=None, wish_scout_count=None):
        """
        ProductCurrentUserData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'rating_scout_count': 'int',
            'rating_scout_average': 'int',
            'wish_scout_count': 'int'
        }

        self.attribute_map = {
            'rating_scout_count': 'rating_scout_count',
            'rating_scout_average': 'rating_scout_average',
            'wish_scout_count': 'wish_scout_count'
        }

        self._rating_scout_count = rating_scout_count
        self._rating_scout_average = rating_scout_average
        self._wish_scout_count = wish_scout_count

    @property
    def rating_scout_count(self):
        """
        Gets the rating_scout_count of this ProductCurrentUserData.
        NOT WORKING

        :return: The rating_scout_count of this ProductCurrentUserData.
        :rtype: int
        """
        return self._rating_scout_count

    @rating_scout_count.setter
    def rating_scout_count(self, rating_scout_count):
        """
        Sets the rating_scout_count of this ProductCurrentUserData.
        NOT WORKING

        :param rating_scout_count: The rating_scout_count of this ProductCurrentUserData.
        :type: int
        """

        self._rating_scout_count = rating_scout_count

    @property
    def rating_scout_average(self):
        """
        Gets the rating_scout_average of this ProductCurrentUserData.
        NOT WORKING

        :return: The rating_scout_average of this ProductCurrentUserData.
        :rtype: int
        """
        return self._rating_scout_average

    @rating_scout_average.setter
    def rating_scout_average(self, rating_scout_average):
        """
        Sets the rating_scout_average of this ProductCurrentUserData.
        NOT WORKING

        :param rating_scout_average: The rating_scout_average of this ProductCurrentUserData.
        :type: int
        """

        self._rating_scout_average = rating_scout_average

    @property
    def wish_scout_count(self):
        """
        Gets the wish_scout_count of this ProductCurrentUserData.
        NOT WORKING

        :return: The wish_scout_count of this ProductCurrentUserData.
        :rtype: int
        """
        return self._wish_scout_count

    @wish_scout_count.setter
    def wish_scout_count(self, wish_scout_count):
        """
        Sets the wish_scout_count of this ProductCurrentUserData.
        NOT WORKING

        :param wish_scout_count: The wish_scout_count of this ProductCurrentUserData.
        :type: int
        """

        self._wish_scout_count = wish_scout_count

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