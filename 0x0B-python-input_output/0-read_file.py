#!/usr/bin/python3
"""Read a file"""
def read_file(filename=""):
    """Read a file"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")