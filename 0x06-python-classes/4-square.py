#!/usr/bin/python3
"""
This module defines a class Square based on 3-square.py

    Attributes:
        private instance attribute size

        property size() to retrieve size

        property setter size() to set it

        public instance method area()

"""


class Square:
    """ Class of square that has no size

    Attributes:
        __size (int): size of square

    """
    def __init__(self, size=0):

        """

        Initialization of square size

        Args:
            size (int): input square size

        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Method of class Square that computes are

        """

        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Method of class Square that retrieves square size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Method of class Sqaure that sets size

        Args:
            value: value to set size to
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
