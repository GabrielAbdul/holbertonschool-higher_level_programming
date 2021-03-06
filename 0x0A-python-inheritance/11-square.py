#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """Defines a Class BaseGeometry based on 5-base_geomtry.py

    Methods: area()
             integer_validator()

    """
    def area(self):
        """Method that raises an exception when area() is called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Description: Method that validates value

        Args:   name - a string
                value - int to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from class BaseGeometry

        Attributes: width - width
                    height - height
    """
    def __init__(self, width, height):
        """init method
            Args: width - width
                  height - height
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that returns area"""
        return (self.__width * self.__height)

    def __str__(self):
        """Method that prints string representation of obj"""
        return "[Rectangle] %r/%r" % (self.__width, self.__height)

class Square(Rectangle, BaseGeometry):
    """Class Square that inherits from class Rectangle

        Attributes: size - size
    """
    def __init__(self, size):
        """init method"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__width, self.__height)

    def area(self):
        """Method that returns area"""
        return self.__size * self.__size

