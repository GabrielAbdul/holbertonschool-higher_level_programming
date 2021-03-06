#!/usr/bin/python3
"""Class Rectangle"""


from models.base import Base


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
        return self.__width

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
        return self.__height

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
        return self.__x

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
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """returns area of rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the rectangle instance with '#'"""
        if self.__height and self.__width == 0:
            print()
        else:
            for newlines in range(self.__y):
                print()
            for rows in range(self.__height):
                for space in range(self.__x):
                    print(' ', end='')
                for cols in range(self.__width):
                    print('#', end='')
                print()

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            try:
                self.id = args[0]
            except Exception:
                pass
            try:
                self.width = args[1]
            except Exception:
                pass
            try:
                self.height = args[2]
            except Exception:
                pass
            try:
                self.x = args[3]
            except Exception:
                pass
            try:
                self.y = args[4]
            except Exception:
                pass
        else:
            for keys in kwargs.keys():
                setattr(self, keys, kwargs[keys])

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        self_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return self_dict

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}\
".format(self.id, self.x, self.y, self.width, self.height)
