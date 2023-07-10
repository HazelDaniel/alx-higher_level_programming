#!/usr/bin/python3
"""a class that defines both BaseGeometry and Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """a class that defines a square"""
    def __init__(self, size):
        """the constructor function"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculate the area"""
        return (self.__size * self.__size)

    def __str__(self):
        """return the str value of the Square class"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
