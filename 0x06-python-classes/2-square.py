#!/usr/bin/python3
""" A module that defines a square class and initializes its fields """


class Square:
    """ a class that defines a square """
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
