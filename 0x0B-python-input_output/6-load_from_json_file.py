#!/usr/bin/python3
"""a module that defines a function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """a function that creates an object from a JSON file"""
    with open(filename, mode="r+", encoding="utf-8") as file:
        return json.load(file)
