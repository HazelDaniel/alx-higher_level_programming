#!/usr/bin/python3
""" This is a module for printing square with # """


def print_square(size):
    """a function that prints a square with # characters"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for _ in range(size):
        [print("#", end="") for _ in range(size)]
        print("")
