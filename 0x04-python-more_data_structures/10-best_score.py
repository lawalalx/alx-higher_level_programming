#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        max_score = max(a_dictionary.values())
        for key in a_dictionary.keys():
            if a_dictionary[key] == max_score:
                return (key)
    except:
        return (None)
