#!/usr/bin/python3
"""Module to create class"""
class BaseGeometry:

    """A base class for geometry operations."""
    def area(self):
        """
        Raises an exception indicating that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates if a value is a positive integer

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer
            ValueError: If value to be validated
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))



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
