#!/usr/bin/python3
"""a module that defines a class Student"""


class Student:
    """a Student class"""

    def __init__(self, first_name, last_name, age):
        """the constructor function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a public instance method that retrieves a dictionary representation\
            of the Student If attrs is a list of strings,\
            represents only those attributes included in the list """
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
