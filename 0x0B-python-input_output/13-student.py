#!/usr/bin/python3
"""class Student"""


class Student:
    """
        Attributes:
            first_name - first name
            last_name - last name
            age - age
        Methods:
            to_json() - retrieves a dict repr of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json() - retrieves a dict repr of a Student instance """
        list_attrs = {}
        if type(attrs) is not list or attrs is None:
            return self.__dict__
        for key in attrs:
            if type(key) is not str:
                return self.__dict__
            if key in self.__dict__:
                list_attrs[key] = self.__dict__[key]
        return list_attrs

    def reload_from_json(self, json):
        """reload_from_json
            loops through all keys in json dictionary,
            and replaces all attributes in self class
            with attributes found in dict
        """
        copy = self.__dict__
        for attrs in json.keys():
            for attr in copy:
                if attr == attrs:
                    setattr(self, attrs, json[attrs])
