#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
=======
"""
    Write a function that creates an Object from a "JSON file"
"""
def load_from_json_file(filename):
    """
        Write a function that creates an Object from a "JSON file"
    """
    import json
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
>>>>>>> b62a6153a1679c0ad6e12dd0efd00766bf7557a2
