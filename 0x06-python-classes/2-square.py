#!/usr/bin/python3
""" Define a class square """


class Square:
    """ Represent a square """
    
    def __int__(self, size=0):
        """Initialize a new square
        
        Args:
            size (int): represent the size of a the sqaure
        """
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size