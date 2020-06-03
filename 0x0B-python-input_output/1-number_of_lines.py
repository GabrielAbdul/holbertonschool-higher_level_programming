#!/usr/bin/python3
"""Function that returns the number of lines in a text file"""


def number_of_lines(filename=""):
    """number_of_lines()
        Args:
            filename - name of file
    """
    line_num = 0
    with open(filename) as file:
        for lines in file:
            line_num += 1
    return line_num
