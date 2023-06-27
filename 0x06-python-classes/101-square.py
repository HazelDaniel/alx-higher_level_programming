#!/usr/bin/python3
""" A module that defines a square class and initializes its fields """


class Square:
    """ a class that defines a square """
    def __init__(self, size=0, position=(0, 0)):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        if (not (type(position[0] == int) and type(position[1] == int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """ a getter method that returns the size of the current instance """
        return self.__size

    @property
    def position(self):
        """ a getter method that returns the position of the\
                current instance """
        return self.__position

    @size.setter
    def size(self, size=0):
        """ a setter method that returns the area of the square"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, position):
        """ a setter method that returns the position of the square"""
        if (not (type(position[0] == int) and type(position[1] == int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ a public instance method that returns the area of the square"""
        return self.size ** 2

    def my_print(self):
        """ a public instance method that prints the area\
                of the current instance """
        if (not self.size):
            print()
        else:
            pad = " " * self.position[0]
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print("{}".format(pad + ("#" * self.size)))

    def __str__(self):
        res = "\n" * self.position[1]
        pad = " " * self.position[0]
        for i in range(self.size):
            if i == self.size - 1:
                res += ("{}".format(pad + ("#" * self.size)))
            else:
                res += ("{}".format(pad + ("#" * self.size))) + "\n"
        return res
