#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle based on 2-rectangle.py

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
        number_of_instances: keeps track of how many obj instances there are
    """
    number_of_instances = 0
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
            self.width = width
            self.height = height
        Rectangle.number_of_instances += 1

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
        elif value < 0:
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
        elif value < 0:
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
        return ((self.__height * 2 ) + (self.__width * 2))


    def __str__(self):
        """
        method of class rectangle to print out rect in #s
        """
        str_rep = ''
        if self.__width is 0 or self.__height is 0:
            return ''
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    str_rep += '#'
                str_rep += '\n'
            print(str_rep)
            return str_rep
    def __repr__(self):
        """
        method of class rectangle to return a string representation of rect
        """
        return "Rectangle(%r, %r)" % (self.width, self.height)
    def __del__(self):
        """
        method of class rectangle to delete an instance and print a message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1        
