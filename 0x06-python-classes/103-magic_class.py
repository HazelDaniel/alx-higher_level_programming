#!/usr/bin/python3
import math
""" A module that defines a class interpreted from bytecode and\
     initializes its fields """


class MagicClass:
    def __init__(self, radius=0):
        """ the constructor method of the MagicClass class """
        if (type(radius) is not int or type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius
        return None

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
