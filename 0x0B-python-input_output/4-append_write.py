#!/usr/bin/python3
"""Function that appends a string at  the end of a text file
and returns the number of characters added"""


def append_write(filename="", text=""):
    """append_write()
        Args:
            filename - name of the file
            text - text to append to the file
    """
    with open(filename, 'a', encoding="UTF-8") as file:
        return file.write(text)
