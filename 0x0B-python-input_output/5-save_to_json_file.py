#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
=======
"""
    Write a function that writes an Object to a text file, using a JSON representation
"""
def save_to_json_file(my_obj, filename):
    """
        Write a function that writes an Object to a text file, using a JSON representation
    """
    import json
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
>>>>>>> b62a6153a1679c0ad6e12dd0efd00766bf7557a2
