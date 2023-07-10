#!/usr/bin/python3
"""a module wherein a function that checks for instances is defined"""


def is_same_class(obj, a_class):
    """a function that checks if a class is the same\
            class as an existing class"""
    return (isinstance(obj, a_class) and obj.__class__ is a_class)
