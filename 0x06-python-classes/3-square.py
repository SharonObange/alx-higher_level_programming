#!/usr/bin/python3


""" This class defines a square """


class Square:
    """
    Attributes:
        __size (int): private, an integer, length of each side

    Methods:
        None
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of Square with the given size

        Args:
            size (int, optional): length of the sides of the square
                                set to 0 by default

        Raises:
            TypeError: If size is not an integer
            ValueError: if size is less than 0

        Returns:
            None
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Initializes a new instance of Square by calculating its area

        Args:
            None

        Returns:
            The current Square area
        """
        area = self.__size * self.__size

        return area
