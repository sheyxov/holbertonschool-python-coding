#!/usr/bin/python3
"""
This module defines a Square class with private size attribute,
getter and setter, and area computation.
"""

class Square:
    """
    Represents a square with private size attribute.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance with optional size.
        """
        self.size = size  # setter will validate

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
