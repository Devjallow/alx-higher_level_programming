#!/usr/bin/python3
""" Define a class square """


class Square:
    """ Represent a square """
    def __int__(self, size=0):
        """Initialize a new square"""

        if type(size) != int:
            raise TypeError("value must be integer")
        if size < 0:
            raise ValueError("value must >= 0")
        self.__size = size
