#!/usr/bin/python3

import math


"""This class calculates the are and circumference of a giveen radius"""


class MagicClass:
    """ Checks if radius is a number"""
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """Calculates the area based on the given radius"""
    def area(self):
        return self.radius ** 2 * math.pi

    """Claculates the circumference based ona given radius"""
    def circumference(self):
        return 2 * math.pi * self.radius
