#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """read_file()
        Args:
            filename - name of the file
    """
    with open(filename, "r", encoding='UTF-8') as file:
        print(file.read())
