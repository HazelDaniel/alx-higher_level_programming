#!/usr/bin/python3
"""a module that defines an empty class"""


class BaseGeometry:
    """an empty class called BaseGeometry"""

    def area(self):
        """It raise an exception for area not def"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a public instance method that validates the input"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
