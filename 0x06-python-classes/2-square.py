#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent a square

    Args:
        size(int) : the size of the square
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >=0")
        self.__size = size
