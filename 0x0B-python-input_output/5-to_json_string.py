#!/usr/bin/python3
"""Function that returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """to_json_string
        Args:
            my_obj - obj to return string repr of
    """
    import json
    return json.dumps(my_obj)
