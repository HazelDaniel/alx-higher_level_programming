#!/usr/python3
def complex_delete(a_dictionary, value):
    if not value:
        return
    match_keys = []
    for k in a_dictionary.keys():
        mch = a_dictionary.get(k, None)
        if (mch and mch == value):
            match_keys.append(k)
    for k in match_keys:
        del a_dictionary[k]
    return a_dictionary
