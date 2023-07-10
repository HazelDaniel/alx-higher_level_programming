#!/usr/bin/python3
"""a module that defines a square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class that defines a square"""
    def __init__(self, size):
        """the constructor function"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
