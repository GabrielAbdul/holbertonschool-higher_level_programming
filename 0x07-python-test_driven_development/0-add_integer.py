#!/usr/bin/python3
"""
Module that adds 2 integers
"""


def add_integer(a, b=98):
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b
