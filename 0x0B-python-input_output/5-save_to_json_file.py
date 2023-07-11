#!/usr/bin/python3
"""a module that defines a function that writes an object\
    to a text file using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an object\
        to a text file using a JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return json.dump(my_obj, file)
