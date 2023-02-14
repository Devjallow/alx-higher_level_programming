#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """
        Initialize a new square object

        Args:
            size(int): size of the square.

        Raise:
            raise type error if parameter is not int
            raise value error if parameter is < 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
