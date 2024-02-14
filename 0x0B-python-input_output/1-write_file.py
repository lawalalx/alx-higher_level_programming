#!/usr/bin/python3
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