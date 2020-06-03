#!/usr/python3
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

    def to_json(self):
        """to_json() - retrieves a dict repr of a Student instance """
            
        return self.__dict__
