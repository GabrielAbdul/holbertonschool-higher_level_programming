#!/usr/bin/python3
"""Class MyInt that inherits from int"""


class MyInt(int):
    """class MyInt"""
    def __eq__(self, other):
        """Method that gets called when compared with =="""
        return not int(self)
    def __ne__(self, other):
        """Method that gets called when compared with !="""
        return int(self) == int(self)
