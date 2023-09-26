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
        Returns:
            None
        """

        self.__size = size

    def size(self):
        """
        Retrieves the size of the square

        Returns:
            int: The length of each side of the square
        """

        return self.__size

    def size(self, value):
        """
        Sets the size of the square

        Args:
            value (int): The length of each side of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

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
