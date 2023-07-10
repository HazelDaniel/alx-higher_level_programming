#!/usr/bin/python3
""" a module wherein a function that checks if a\
        class inherited from another class"""


def inherits_from(obj, a_class):
    """a function that determines if a function \
           inherited from another class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
