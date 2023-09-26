#!/usr/bin/python3


""" This class defines a square """


class Square:
    """
    Attributes:
        __size (int): the length of each side.
                    : this attribute is private and should be an integer

    Methods:
        None
    """
    def __init__(self, size):
        """
        Initializes a new instance of Square with the given size

        Args:
            size (int): The length of the sides of the square

        Returns:
           None
        """
        self.__size = size
