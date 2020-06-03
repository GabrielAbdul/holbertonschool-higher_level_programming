#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Function that returns True or False"""
    return isinstance(obj, a_class) and type(obj) != a_class
