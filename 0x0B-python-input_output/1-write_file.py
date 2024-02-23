#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
=======
"""Write a file"""
def write_file(filename="", text=""):
    """
        Write a function that writes a string to a text file (UTF8) and returns the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
    file.close()
    count = sum(len(word) for word in text)
    return (count)
>>>>>>> b62a6153a1679c0ad6e12dd0efd00766bf7557a2
