#!/usr/bin/python3
"""Function that creates an Object from a "JSON file"""


def load_from_json_file(filename):
    """load_from_json_file()
        Args:
            filename - name of the file
    """
    with open(filename) as file:
        import json
        return json.load(file)
