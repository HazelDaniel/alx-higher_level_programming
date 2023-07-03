#!/usr/bin/python3
"""a module wherein a rectangle class is defined"""
rect_val_check = __import__("1-rectangle").rect_val_check


class Rectangle:
    """a class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        rect_val_check(width, height)
        self.__width = width
        self.__height = height

    def area(self):
        """a public instance method that returns the area\
            of the rectangle class"""
        return self.width * self.height

    def perimeter(self):
        """a public instance method that returns the perimeter\
            of the rectangle class"""
        if (self.width == 0 or self.height == 0):
            return 0
        return 2 * (self.width + self.height)

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
