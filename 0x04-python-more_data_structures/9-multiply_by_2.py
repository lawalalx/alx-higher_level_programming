#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    values = [value*2 for value in a_dictionary.values()]
    return (dict(zip(a_dictionary.keys(), values)))
