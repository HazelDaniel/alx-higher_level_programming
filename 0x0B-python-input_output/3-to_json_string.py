#!/usr/bin/python3
"""a module that defines a function that returns the json\
    representation of an object"""
import json


def to_json_string(my_obj):
    """a function that retuns the json representation of an object"""
    return json.dumps((my_obj))
