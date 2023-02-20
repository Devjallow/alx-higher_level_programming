#!/usr/bin/python3
"""Define a classs sqaure"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """
        Initialize a new square object

        Args:
            size(int): size of parameter.

        Raise:
            raise type error if parameter is not int
            raise value error if parameter is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of a square

        Return:
            area of a square
        """
        return self.__size ** 2
