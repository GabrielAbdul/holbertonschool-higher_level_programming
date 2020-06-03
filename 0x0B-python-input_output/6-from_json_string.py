#!/usr/bin/python3
"""Function that returns an object represented by a JSON string"""


def from_json_string(my_str):
    """form_json_string
        Args:
            my_str - str to return as obj
    """
    import json
    return json.loads(my_str)
