#!/usr/bin/python3
"""1. Base Class """


import json


class Base:
    """Class Base
        Attributes:
            __nb_objects = # of instances meant to be id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """init method
            Args:
                id - obj id
        """
        self.__nb_objects
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representatin of list_dictionaries
            Args:
                list_dictionaries - list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation to a file
            Args:
                cls - class name
                list_objs - list of instances that inherit from Base
        """
        list_dicts = []
        for instances in list_objs:
            list_dicts.append(instances.to_dictionary())
        json_dicts = Base.to_json_string(list_dicts)
        try:
            with open("{}.json".format(cls.__name__), 'a') as jason:
                jason.write(json_dicts)
        except FileNotFoundError:
            with open("{}.json".format(cls.__name__), 'x') as jason:
                jason.write(json_dicts)
