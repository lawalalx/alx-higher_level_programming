#!/usr/bin/python3
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