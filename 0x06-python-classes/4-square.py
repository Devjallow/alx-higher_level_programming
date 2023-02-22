#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represent a class square"""
    def __init__(self, size=0):
        """
        Initializing a square

        Arg:
            size(int): size of the integer
        Raise:
            raise TypeError if value is not int
            raise ValueError if value is less than zero
        """
        self.__size = size

    @property
    def size(self):
        """object setter retrive the value of square
        object setter:
                to set the value of size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("value must be integer")
        elif value < 0:
            raise ValueError("value must be >=0")
        else:
            self.__size = value

    def area(self):
        """ Return the square area of a square """
        return self.__size ** 2
