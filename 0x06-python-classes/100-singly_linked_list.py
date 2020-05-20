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
        __data = data

    
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
            self.next_node = value
        else:
            raise TypeError("next_node must be a Node object")
            
    
class SinglyLinkedList:
    """
    Class SinglyLinkedList that defines a singly linked list
    """

    
    def __init__(self):
        """
        Init method of class SLL
        """
        self.__head = None
        self.__head.next_node = None

    def sorted_insert(self, value):
        """
        Method sorted_insert of class SLL that inserts a new node
        into the correct sorted position (increasing order)
        """

        node = Node(value)

        if (self.head is None):
            self.head = node

        tmp  = self.head

        while tmp.next_node:
            if tmp.__data < value:
                node = tmp.__data
            elif tmp.__data > value:
                tmp = tmp.next_node
            else:
                tmp.next_node = node
                node.next_node = tmp.next_node.next_node
            
