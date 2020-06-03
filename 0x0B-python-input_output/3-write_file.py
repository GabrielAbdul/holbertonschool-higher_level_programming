#!/usr/bin/python3
"""Function that writes text to a file and returns the # of chars written"""


def write_file(filename="", text=""):
    """write_file()
        Args:
            filename - name of file
            text - text to write to file
    """
    with open(filename, 'w') as file:
        return file.write(text)
