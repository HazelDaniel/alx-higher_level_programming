#!/usr/bin/python3
"""a module that defines a class Student"""


class Student:
    """a student class"""

    def __init__(self, first_name, last_name, age):
        """the constructor function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a public instance method that sets a dictionary representation\
            of the Student class based on some conditions """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """a public instance method that replaces all\
            attributes of the Student"""
        for k, v in json.items():
            setattr(self, k, v)
