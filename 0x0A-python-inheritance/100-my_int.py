#!/usr/bin/python3
"""a module that defines a class MyInt that inherits from int"""


class MyInt(int):
    """a class that inverts int operators == and !="""

    def __eq__(self, value):
        """a public instance method that overrides ==\
            operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """a public instance method that overrides != operator\
            with == behavior"""
        return self.real == value
