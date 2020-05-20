#!/usr/bin/python3
""" Singly linked list mod """


class Node:
    """ singly linked list """
    def __init__(self, data, next_node=None):
        """ private att
        Args:
             data - info in list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data """
        return self.__data

    @data.setter
    def data(self, value):
        """ set value in a node in a linked list """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ get next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ sets the next node """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

""" Does More Docstring go here, I really don't know """


class SinglyLinkedList:
    """ linked list """
    def __init__(self):
        """ head """
        self.__head = None

    def sorted_insert(self, value):
        """ node """
        Newn = Node(value, None)
        if (self.__head is None):
            self.__head = Newn
            return
        tmp = self.__head
        if tmp.data > Newn.data:
            Newn.next_node = tmp
            self.__head = Newn
            return
        while tmp.next_node is not None:
            tmp2 = tmp.next_node
            if tmp2.data < Newn.data:
                tmp = tmp.next_node
                continue
            else:
                tmp.next_node = Newn
                Newn.next_node = tmp2
                return
        if tmp.next_node is None:
            tmp.next_node = Newn
            return

    def __str__(self):
        """ str to print """
        new = ""
        nh = self.__head
        while nh is not None:
            new += (str(nh.data))
            nh = nh.next_node
            if nh is not None:
                new += ('\n')
        return new
