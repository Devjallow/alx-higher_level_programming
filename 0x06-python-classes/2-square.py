#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent a square

    Args:
        size(int) : the size of the square
    """
    def __init__(self, size):
        if type(size) != int:
            raise TypeError("value must be an interger")
        if size < 0:
            raise TypeError("value must be >=0")
        self.__size = size
