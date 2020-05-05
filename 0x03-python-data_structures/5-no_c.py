#!/usr/bin/python3


def no_c(my_string):
    unwanted = ['c', 'C']
    my_string = ''.join(i for i in my_string if i not in unwanted)
    return my_string
