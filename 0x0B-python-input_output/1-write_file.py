#!/usr/bin/python3
"""a module that defines a function that writes to a file"""


def write_file(filename="", text=""):
    """a function that writes to a file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(str(text))
