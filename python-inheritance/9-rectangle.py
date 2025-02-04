#!/usr/bin/python3
"""Module to create class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height
    def __str__(self):
        """Return a string of the rectangle"""
        return f"[Rectagle] {self.__width}/{self.__height}"
