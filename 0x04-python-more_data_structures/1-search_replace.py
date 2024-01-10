#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for word in my_list:
        if word == search:
            word = replace
        new.append(word)
    return (new)
