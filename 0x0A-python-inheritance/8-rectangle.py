#!/usr/bin/python3
"""a module that defines a rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a rectangle class that inherits from a 'BaseGeometry' class"""
    def __init__(self, width, height):
        """the constructor function"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
