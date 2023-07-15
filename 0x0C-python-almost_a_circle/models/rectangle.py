#!/usr/bin/python3
"""a module that defines a rectangle class"""

from . import base
Base = base.Base


def validate_prop(name, value):
    match name:
        case "width" | "height" as dimension:
            if (type(value) != int):
                raise TypeError("{} must be an integer".format(dimension))
            if (value <= 0):
                raise ValueError("{} must be > 0".format(dimension))
        case "x" | "y" as point:
            if (type(value) != int):
                raise TypeError("{} must be an integer".format(point))
            if (value < 0):
                raise ValueError("{} must be >= 0".format(point))


class Rectangle(Base):
    """a class that defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """the constructor function"""
        super().__init__(id)
        validate_prop("width", width)
        self.__width = width
        validate_prop("height", height)
        self.__height = height
        validate_prop("x", x)
        self.__x = x
        validate_prop("y", y)
        self.__y = y

    def area(self):
        """returns the area of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints the visual representation of the Rectangle class"""
        pad_x = " " * self.x
        pad_y = "\n" * self.y
        print(pad_y, end="")
        for hgt in range(self.height):
            print(pad_x, end="")
            for wdt in range(self.width):
                print("#", end="")
            print()

    @property
    def width(self):
        """a public instance attribute for accessing the width"""
        return self.__width

    @property
    def height(self):
        """a public instance attribute for accessing the height"""
        return self.__height

    @property
    def x(self):
        """a public instance attribute for accessing the x attribute"""
        return self.__x

    @property
    def y(self):
        """a public instance attribute for accessing the y attribute"""
        return self.__y

    @width.setter
    def width(self, w):
        """a setter method for the public instance attribute 'width'"""
        validate_prop("width", w)
        self.__width = w

    @height.setter
    def height(self, h):
        """a setter method for the public instance attribute 'height'"""
        validate_prop("height", h)
        self.__height = h

    @x.setter
    def x(self, val):
        """a setter method for the public instance attribute 'x'"""
        validate_prop("x", val)
        self.__x = val

    @y.setter
    def y(self, val):
        """a setter method for the public instance attribute 'y'"""
        validate_prop("y", val)
        self.__y = val

    def __str__(self):
        """returns the string representation of an instance"""
        f_string = "[Rectangle] ({}) {}/{} - {}/{}"
        return f_string.format(self.id, self.x, self.y,
                               self.width, self.height)
