#!/usr/bin/python3
"""the module for a function that Prints the name of a user """


def say_my_name(first_name, last_name=""):
    """a program to print name

    first_name: the firstname string
    last_name: the second string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
