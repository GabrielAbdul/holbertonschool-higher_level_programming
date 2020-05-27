#!/usr/bin/python3


"""Class Rectangle that defines a rectangle based on 1-rectangle.py
Attributes:
    __width
    __height
    width(self) getter
    width(self, value) setter
    height(self) getter
    height(self, value) setter
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle

    Attributes:
        width (int): width of rect
        height (int): height of rect
    """
    def __init__(self, width=0, height=0):
        """
        init method of class rectangle to initialize new instances with values

        Args:
            width (int)
            height (int)
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        method of class rectangle to set width

        Args:
            value: integer to set width with
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value is < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        method of class rectangle to set height

        Args:
            value: integer to set height with
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value is < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        method of class rectangle to return area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        method of class rectangle to return perimeter
        """
        if self.__height is 0 or self.__width is 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))
