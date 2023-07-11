#!/usr/bin/python3
"""a module that defines a class Student"""


class Student:
    """a student class"""

    def __init__(self, first_name, last_name, age):
        """the constructor function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a public instance method to retrieve a dictionary\
            representation of the Student class"""
        return self.__dict__
