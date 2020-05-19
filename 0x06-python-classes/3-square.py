#!/usr/bin/python3
"""
This module defines a class Square

    Attribues:
        private class attribute size

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
