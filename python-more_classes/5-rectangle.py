#!/usr/bin/python3
"""Module to create class
This module defines an empty class called Rectangle.
"""


class Rectangle:
    """ an empty rectangle, we will define it later too
    """

    def __init__(self, width=0, height=0):
        """initialize the rectangle with width and height at 0"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """change the size of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ change the height of the rectangle with the value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.height})"
    
    def __del__(self):
        print("Bye rectangle...")
