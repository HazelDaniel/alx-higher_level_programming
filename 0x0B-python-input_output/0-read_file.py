#!/usr/bin/python3
"""a module that defines a function that reads in a file's content"""


def read_file(filename=""):
    """a function that reads in a file's content"""
    with open(filename, mode="r", encoding="utf-8") as file:
        read_n = file.read()
        print(read_n, end="")
