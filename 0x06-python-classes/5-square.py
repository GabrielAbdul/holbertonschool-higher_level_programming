#!/usr/bin/python3


class Square:
    """ Class of square that has no size

    Attributes:
        __size (int): size of square

    """
    def __init__(self, size=0):
    
        """

        Initialization of square size

        Args:
            size (int): input square size

        """
    
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            
    def area(self):
        """
        Method of class Square that computes are

        """

        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Method of class Square that retrieves square size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Method of class Sqaure that sets size

        Args:
            value: value to set size to 
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Method of class Square that prints the square with the # char
        """

        if self.__size == 0:
            print()
        else:
            for rows in range(self.__size):
                for cols in range(self.__size):
                    print('#', end='')
                print()
