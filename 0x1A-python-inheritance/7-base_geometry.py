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
