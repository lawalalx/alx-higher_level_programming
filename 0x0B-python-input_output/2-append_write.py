#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
=======
"""Append to a file"""
def append_write(filename="", text=""):
    """
    Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
    return sum(len(word) for word in text)
>>>>>>> b62a6153a1679c0ad6e12dd0efd00766bf7557a2
