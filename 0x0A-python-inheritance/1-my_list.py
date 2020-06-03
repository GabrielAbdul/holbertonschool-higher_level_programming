#!/usr/bin/python3
"""Class that ingerits from list"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
