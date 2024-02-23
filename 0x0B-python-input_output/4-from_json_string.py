#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
=======
"""
    Write a function that returns an object (Python data structure) represented by a JSON string
"""
def from_json_string(my_str):
    """
        Write a function that returns an object (Python data structure) represented by a JSON string
    """
    import json
    return json.loads(my_str)
>>>>>>> b62a6153a1679c0ad6e12dd0efd00766bf7557a2
