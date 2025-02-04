#!/usr/bin/python3
"""Module to create class"""
BaseGeometry = __import__('9-rectangle').BaseGeometry


class Square(BaseGeometry):
    """class representing a square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the aera of the square"""
        return self.__size ** 2
    
    def __str__(self):
        """return a string representation of the square"""
        return f"[Sqaure] {self.__size}/{self.__size}"
