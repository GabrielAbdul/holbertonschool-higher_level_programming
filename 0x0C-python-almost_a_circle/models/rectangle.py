#!/usr/bin/python3
"""2. First Rectangle """


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
    def width_setter(self, width):
        """Width setter"""
        if type(width) is not int:
            raise TypeError("width must be an int")
        else:
            self.__width = width

    @property
    def height(self):
        """Height getter"""
        return self.height

   @height.setter
    def height_setter(self, height):
        """Width setter"""
        if type(height) is not int:
            raise TypeError("width must be an int")
	elif height <= 0:
            raise
        else:
            self.__width = width


