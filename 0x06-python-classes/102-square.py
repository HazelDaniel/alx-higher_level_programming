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

    @property
    def size(self):
        """ a getter method that returns the size of the current instance """
        return self.__size

    @size.setter
    def size(self, size=0):
        """ a setter method that returns the area of the square"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ a public instance method that returns the area of the square"""
        return self.size ** 2

    def __eq__(self, other):
        """ a private instance method that returns the a boolean resulting\
            from scalar comparison of an instance with another instance (=)"""
        return isinstance(other, Square) and self.size == other.size

    def __gt__(self, other):
        """ a private instance method that returns the a boolean resulting\
            from scalar comparison of an instance with another instance (>)"""
        return isinstance(other, Square) and self.size > other.size

    def __lt__(self, other):
        """ a private instance method that returns the a boolean resulting\
            from scalar comparison of an instance with another instance (<)"""
        return isinstance(other, Square) and self.size < other.size

    def __le__(self, other):
        """ a private instance method that returns the a boolean resulting\
            from scalar comparison of an instance with another instance (<=)"""
        return isinstance(other, Square) and self.size <= other.size

    def __ge__(self, other):
        """ a private instance method that returns the a boolean resulting\
            from scalar comparison of an instance with another instance (>=)"""
        return isinstance(other, Square) and self.size >= other.size
