#!/usr/bin/python3
"""a module that defines a 'base' class"""

import json


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the constructor function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static method that serializes a dictionary list"""
        if (not list_dictionaries):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """a static method that decodes a json string"""
        if (not json_string):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method that saves a list of objects into a json file"""
        res_file = cls.__name__
        res_file += ".json"
        if not list_objs:
            with open(res_file, mode="w", encoding="utf-8") as file:
                return json.dump([], file)
        else:
            list_objs = [obj.to_dictionary() for obj in list_objs]
            with open(res_file, mode="w", encoding="utf-8") as file:
                json.dump(list_objs, file)

    @classmethod
    def create(cls, **dictionary):
        """a class method that creates a new instance from\
            a dictionary of attributes"""
        new_inst = cls(10, 10)
        new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """a class method that returns all instances from a json file"""
        res_file = cls.__name__ + ".json"
        with open(res_file, mode="r+", encoding="utf-8") as file:
            res = file.read()
            res_list = cls.from_json_string(res)
            res_list = [cls.create(**dct) for dct in res_list]
            return res_list
