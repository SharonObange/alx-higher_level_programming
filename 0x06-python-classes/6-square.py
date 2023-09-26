#!/usr/bin/python3


""" This class defines a square """


class Square:
    """
    Attributes:
        __size (int): private, an integer, length of each side

    Methods:
        None
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of Square with the given size

        Args:
            size (int, optional): length of the sides of the square
                                set to 0 by default
        Returns:
            None
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square

        Returns:
            int: The length of each side of the square
        """

        return self.__size

    @size.setter
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

    @property
    def position(self):
        """
        Retrieves the position of the square

        Returns:
            int: The length of each side of the square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the size of the square

        Args:
            value (int): The length of each side of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all (num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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

    def my_print(self):
        """prints the square with # in stdout"""
        if self.__size == 0:
            print()

        else:	
            for _ in range(self.__position[1]):
               print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
