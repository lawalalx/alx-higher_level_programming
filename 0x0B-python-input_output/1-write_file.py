#!/usr/bin/python3
"""Write a file"""
def write_file(filename="", text=""):
    """
        Write a function that writes a string to a text file (UTF8) and returns the number of characters written
    """
    count = 0
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
    file.close()
    for word in text:
        for character in word:
            count += 1
    return (count)