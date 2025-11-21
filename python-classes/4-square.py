#!/usr/bin/python3
"""
Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """
    Represents a square with private size attribute.
    """
    def __init__(self, size=0):
        """
        Initialize a new Square instance with optional size.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the private size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the private size attribute.
        Validates that size is an integer >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the '#' character.
        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
