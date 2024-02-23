#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
=======
"""Read a file"""
def read_file(filename=""):
    """Read a file"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
    file.close()
>>>>>>> b62a6153a1679c0ad6e12dd0efd00766bf7557a2
