#!/usr/bin/python3
"""Function that writes an Object to a text file, using JSON repr"""


def save_to_json_file(my_obj, filename):
    """save_to_json_file
        Args:
            my_obj - obj to write
            filename - name of file to write obj to
    """
    with open(filename, "w") as file:
        import json
        json.dump(my_obj, file)
