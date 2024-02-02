#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_str = ""
    punct = [".","?",":"]
    for char in text:
        current_str+=char
        if char in punct:
            print(current_str.strip())
            print()
            current_str=""
    if current_str:
        print(current_str)
