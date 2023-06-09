#!/usr/bin/python3
"""a module wherein a rectangle class is defined"""
rect_val_check = __import__("1-rectangle").rect_val_check


def rect_check(rect_1, rect_2):
    """an input validator for two rectangle instances"""
    if (not rect_1 or not rect_2):
        return None
    if (not isinstance(rect_1, Rectangle)):
        raise TypeError("rect_1 must be an instance of Rectangle")
    if (not isinstance(rect_2, Rectangle)):
        raise TypeError("rect_2 must be an instance of Rectangle")


class Rectangle:
    """a class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        rect_val_check(width, height)
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """a static method that does a scalar comparison of two rectangle\
            classes based on their areas"""
        rect_check(rect_1, rect_2)
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        return rect_2

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

    def __str__(self):
        """a special method that returns the string representation\
            of the rectangle class"""
        ret_str = ""

        if (self.area == 0):
            return ret_str

        for h in range(self.height):
            for _ in range(self.width):
                ret_str += str(self.print_symbol)
            if h != self.height - 1:
                ret_str += "\n"
        return ret_str

    def __repr__(self):
        """a special method that returns the exact string representation\
            that can be used to construct the object itself"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """a special method that serves as a destructor for the current\
            instance of the rectangle object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
