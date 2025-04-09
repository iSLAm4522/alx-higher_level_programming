#!/usr/bin/python3

"""
This module defines a singly linked list and a Node class for the list.
"""


class Node:
    """
    This class defines a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for the data attribute.
        """
        return self.__data

    @property
    def next_node(self):
        """
        Getter for the next_node attribute.
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list.
    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the list.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
