#!/usr/bin/python3
"""a module wherein a rectangle class is defined"""


def rect_val_check(width=0, height=0):
    """an input validator for width and height parameters"""
    if (type(width) != int):
        raise TypeError("width is not an integer")
    if (width < 0):
        raise ValueError("width must be >= 0")
    if (type(height) != int):
        raise TypeError("height is not an integer")
    if (height < 0):
        raise ValueError("height must be >= 0")


class Rectangle:
    """a class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        rect_val_check(width, height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """a public getter method for the width field"""
        return self.__width

    @property
    def height(self):
        """a public getter method for the height field"""
        return self.__height

    @width.setter
    def width(self, value):
        """a public setter method for the width field"""
        rect_val_check(value, self.__height)
        self.__width = value

    @height.setter
    def height(self, value):
        """a public setter method for the height field"""
        rect_val_check(self.__width, value)
        self.__height = value
