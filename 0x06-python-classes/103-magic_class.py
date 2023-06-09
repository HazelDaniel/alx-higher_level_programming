#!/usr/bin/python3

""" A module that defines a class interpreted from bytecode and\
     initializes its fields """
import math


class MagicClass:
    """ an anonymous class interpreted from a bytecode """
    def __init__(self, radius=0):
        """ the constructor method of the MagicClass class """
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius
        return None

    def area(self):
        """ a public instance method for getting the area of a MagicClass """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """ a public instance method for getting the\
            circumference of a MagicClass """
        return 2 * math.pi * self.__radius
