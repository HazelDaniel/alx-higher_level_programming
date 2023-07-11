#!/usr/bin/python3
"""a module that defines a Python class-to-JSON function"""


def class_to_json(obj):
    """a Python class-to-JSON function"""
    return obj.__dict__
