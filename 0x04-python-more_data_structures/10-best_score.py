#!/usr/bin/python3

def best_score(a_dictionary):
    if (not a_dictionary):
        return None
    maximum = 0
    best_key = None
    for x, _ in (a_dictionary.items()):
        if (a_dictionary[x] > maximum):
            maximum = a_dictionary[x]
            best_key = x
    return best_key
