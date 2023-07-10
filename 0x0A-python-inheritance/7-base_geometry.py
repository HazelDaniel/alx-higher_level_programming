#!/usr/bin/python3
"""a module that defines an empty class"""


class BaseGeometry:
    """an empty class called BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value < 0:
            raise ValueError("<value> must be greater than 0")
