#!/usr/bin/python3
"""
    Write a function that returns the JSON representation of an object (string)
"""
def to_json_string(my_obj):
    """
        Write a function that returns the JSON representation of an object (string)
    """
    import json
    return json.dumps(my_obj)