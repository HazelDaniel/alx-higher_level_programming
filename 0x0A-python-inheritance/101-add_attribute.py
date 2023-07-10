#!/usr/bin/python3
"""a module that defines a function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """a method to add a new attribute to an object if possible """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
