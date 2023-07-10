#!/usr/bin/python3
"""a module that defines a list subclass"""


class MyList(list):
    """a list class that extends from the list base object"""

    def __init__(self):
        """the constructor function"""
        list.__init__(self)

    def print_sorted(self):
        """a function that prints the list in a sorted order"""
        print(sorted(self))
