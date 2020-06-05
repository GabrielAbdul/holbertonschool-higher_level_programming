#!/usr/bin/python3
"""1. Base Class """


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
