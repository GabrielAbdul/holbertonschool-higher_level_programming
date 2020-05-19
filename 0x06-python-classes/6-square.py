#!/usr/bin/python3


class Square:
    """ Class of square that has no size

    Attributes:
        __size (int): size of square

    """
    def __init__(self, size=0, position=(0, 0)):
    
        """

        Initialization of square size

        Args:
            size (int): input square size
            position (tuple): input (x, y) position(s) of square

        """
    
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple:
            raise TypeError("position must be a tuple of two positive integers")
        else:
            self.__position = position
            
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

    @property    
    def position(self):
        """
        Method of class Square that retrieves square position
        """

        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Method of class Square that sets position

        Args:
            value: value to set position to
        """

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Method of class Square that prints the square with the # char
        """

        if self.__size == 0:
            print()
        else:
            for rows in range(self.__size):
                if self.__position[0] > 0:
                    for space in range(self.__position[0]):
                        print(' ')
                    for cols in range(self.__size):
                        if self.__position[1] > 0:
                            for nl in range(self.__position[1]):
                                print()
                    print('#', end='')
                print()
