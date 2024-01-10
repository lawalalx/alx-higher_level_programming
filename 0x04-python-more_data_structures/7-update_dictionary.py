#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary.keys():
        a_dictionary[key] = value
    a_dictionary.update({key: value})
    sorted_dict = dict(sorted(a_dictionary.items(), key=lambda x: x[0]))
    return (sorted_dict)
