#!/usr/bin/python3

""" A module that defines a Node class and a SinglyLinkedList class """


class Node:
    """ a class that defines a Node """
    def __init__(self, data, next_node=None):
        if (type(data) != int):
            raise TypeError("data must be an integer")
        self.__data = data
        if (not (isinstance(next_node, Node) or next_node is None)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, data):
        if (type(data) != int):
            raise TypeError("data must be an integer")
        self.__data = data

    @next_node.setter
    def next_node(self, next_node):
        if (not (isinstance(next_node, Node) or next_node is None)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """definition of Singly Linked List"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """a public instance method inserts a node in sorted linked list """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            curr = self.__head
            while (curr.next_node is not None
                   and curr.next_node.data < value):
                curr = curr.next_node
            new.next_node = curr.next_node
            curr.next_node = new

    def __str__(self):
        value = []
        curr = self.__head
        while curr is not None:
            value.append(str(curr.data))
            curr = curr.next_node
        return ('\n'.join(value))
