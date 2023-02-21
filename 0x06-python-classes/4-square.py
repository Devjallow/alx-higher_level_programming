#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represent a class square"""
    def __init__(self, size=0):
        """
        Initialize a square object
        Arg:
            size(int) first parameter 
        Raise:
            raise typeerror if value is not int
            raise value error if value is less than 0
        """
    @property
    def size(self):
        """object setter retrive the value of square
        object setter:
                to set the value of size.
        """
        return self.__size = size

    @size.sitter
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
