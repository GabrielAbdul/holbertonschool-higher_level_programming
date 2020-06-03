#!/usr/bin/python3
class BaseGeometry:
    """Defines a class BaseGeometry based on 5-base_geometry.py

        Methods: area
    """
    def area(self):
        """Method that raises an exception when area() is called"""
        raise Exception("area() is not implemented")
