#!/usr/bin/python3
"""2. First Rectangle """


class Base:
    """Class Base
        Attributes:
            __nb_objects = # of instances meant to be id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """init method
            Args:
                id - obj id
        """
        self.__nb_objects
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id


class Rectangle(Base):
    """Class Rectangle that ingerits from Base
        Attributes:
            width - width
            height - height
            x - x
            y - y
        Methods:
            __init__() - Class constructor
    """
    def __init__(self, width, height, x=0, y=0, id=None):
            """Class constructor
                Args:
                    width - width
                    height - height
                    x - x
                    y - y
            """
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y
            super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.width

    @width.setter
    def width_setter(self, width):
        """Width setter"""
        if type(width) is not int:
            raise TypeError("width must be an int")
        elif width <= 0:
            raise ValueError("width must be greater than  0")
        else:
            self.__width = width

    @property
    def height(self):
        """Height getter"""
        return self.height

    @height.setter
    def height_setter(self, height):
        """Height setter"""
        if type(height) is not int:
            raise TypeError("height must be an int")
        elif height <= 0:
            raise ValueError("height must be greater than 0")
        else:
            self.__height = height

    @property
    def x(self):
        """x property"""
        return self.x

    @x.setter
    def x_setter(self):
        self.__x = x

    @property
    def y(self):
        """y property"""
        return self.y

    @y.setter
    def y_setter(self):
        self.__y = y
