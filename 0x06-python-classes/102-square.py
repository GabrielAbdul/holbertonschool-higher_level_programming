#!/usr/bin/python3
"""
class Square defines a square based on 4-square.py
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

    def __lt__(self, other):
        """
        Method of class Square that enables < comparison
        """
        return self.size < other.size

    def __le__(self, other):
        """
        Method of class Square that enables < comparison
        """
        return self.size <= other.size

    def __eq__(self, other):
        """
        Method  of class Square that enables < comparison
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        Method of class Square that enables < comparison
        """
        return not self.size == other.size

    def __gt__(self, other):
        """
        Method of class Square that enables < comparison
        """
        return self.size > other.size

    def __ge__(self, other):
        """
        Method of class Square that enables < comparison
        """
        return self.size >= other.size
