#!/usr/bin/python3
""" Define a square """


class Square:
    """ Represent a square """
    def __init__(self, size=0):
        """
        Initilizing a square

        Args:
            size(int): size of a square.
        Raise:
            raise a typeerro if value is not integer
            raise valueerror if value is  less than zero
        """
        self.__size = size

    @property
    def size(self):
        """get/setter getting and setting the value"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("value most be integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ return area of a square """
        return self.__size ** 2

    def my_print(self):
        """ print square """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
