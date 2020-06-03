#!/usr/bin/python3
class BaseGeometry:
    """Defines a Class BaseGeometry based on 5-base_geomtry.py

    Methods: area()

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
