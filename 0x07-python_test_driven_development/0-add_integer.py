#!/usr/bin/python3
""" Defines a function for integer addition """


def add_integer(a, b=98):
    """prints the integer addition of two numbers """
    if (not (isinstance(a, int) or isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not (isinstance(b, int) or isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
