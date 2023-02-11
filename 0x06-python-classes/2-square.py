#!/usr/bin/python3
""" Define a class square """


class Square:
    """ Represent a square """
    def __int__(self, size=0):
        """Initialze a new square

        Args:
            size(int): size of the new square
        """
            
        if type(size) != int:
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
