#!/usr/bin/python3

""" This is a Rectangle class """


class Rectangle:
    def __init__(self, width=0, height=0):
        """ This is a method to define width and height """

        self.width = width
        self.height = height


    @property
    def width(self):
        """" This method gets the width attribute """

        return self.__width


    @width.setter
    def width(self, value):
        """" This method sets the width to a new value """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value


    @property
    def height(self):
        """ This method gets the height attribute """
        return self.__height


    @height.setter
    def height(self, value):
        """ This method sets the height to a new value """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
