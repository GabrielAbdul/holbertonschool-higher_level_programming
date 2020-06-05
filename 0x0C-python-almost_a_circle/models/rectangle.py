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
            self.width = width
            self.height = height
            self.x = x
            self.y = y
            super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Height getter"""
        return self.height

    @height.setter
    def height(self, height):
        """Height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def x(self):
        """x property"""
        return self.x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """y property"""
        return self.y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
