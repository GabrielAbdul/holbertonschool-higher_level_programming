#!/usr/bin/python3


class Node:
    """
    Class Node defines a node of a singly linked list

    Attributes:
        data: data int
        next_ndoe: the next node
    """

    def __init__(self, data, next_node=None):
        """
        Init method of class Node

        Args:
            data: data
            next_node: the next node, set to None initially
        """
        __data = data(self, data)
        __next_node = None

    
    @property
    def data(self):
        """
        Method data of class Node to retrive data
        """
        return self.__data

    @property
    def __next_node(self):
        """
        Metod next_node of class Node to retrive next_node
        """
        return self.__next_node
        
    @data.setter
    def data(self, value):
        """
        Method data(self, value) of class Node to set data

        Args:
            value: value to set to data
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """
        Method of class Node to set the next node

        Args:
            value: next node
        """

        if isinstance(value, Node) or value == None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")
            
    
class SinglyLinkedList
    """
    Class SinglyLinkedList that defines a singly linked list
    """

    
    def __init__(self):
        """
        Init method of class SLL
        """
        self.__head = __head
        self.__head.__next_node = None

    def sorted_insert(self, value):
        """
        Method sorted_insert of class SLL that inserts a new node
        into the correct sorted position (increasing order)
        """

        Node *node = None
        flag, index = 0, 0

        node.__data = value

        if (!self.__head or self.__head):
            self.__head = node
        for(; node; node = node.__next_node):
            if node.__data < node.__next_node.__data:
                node

        
