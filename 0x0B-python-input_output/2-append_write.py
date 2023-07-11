#!/usr/bin/python3
"""a module that defines a function that appends to the end of a text file"""


def append_write(filename="", text=""):
    """a function that appends a text to the end of a file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
