#!/usr/bin/python3
"""a module that defines an empty class"""


class BaseGeometry:
    """an empty class called BaseGeometry"""
    def area(self):
        """a public instance method that computes the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a public instance method that validates the input"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value < 0:
            raise ValueError("<value> must be greater than 0")
