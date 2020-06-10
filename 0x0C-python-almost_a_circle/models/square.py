#!/usr/bin/python3
"""Class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from class Rectangle
        Attributes:
            size - size
            x - x
            y - y
        Methods:
            __init__() - Class constructor
"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Size getter"""
        return self.__width

    @size.setter
    def size(self, size):
        """Size setter"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = size
            self.__height = size
            self.__size = size

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            try:
                self.id = args[0]
            except Exception:
                pass
            try:
                self.size = args[1]
            except Exception:
                pass
            try:
                self.x = args[2]
            except Exception:
                pass
            try:
                self.y = args[3]
            except Exception:
                pass
        else:
            for keys in kwargs.keys():
                setattr(self, keys, kwargs[keys])

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        self_dict = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return self_dict

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return "Square ({}) {}/{} - {}\
".format(self.id, self.x, self.y, self.width)
