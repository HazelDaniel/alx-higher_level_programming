#!/usr/bin/python3
"""a module that defines a function that returns an object\
        represented by a json string"""
import json


def from_json_string(my_str):
    """a function that returns an object represented by a json string"""
    return json.loads(my_str)
