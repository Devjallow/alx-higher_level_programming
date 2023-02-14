#!/usr/bin/python3
"""Define a classs sqaure"""


class Square:
    def __init__(self, size):
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
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(size):
        """Return the area of size"""

        return self.__size ** 2
