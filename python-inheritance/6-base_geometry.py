#!/usr/bin/python3
"""Module to create class
"""


class BaseGeometry:

    """A base class for geometry operations."""
    def area(self):
        """
        Raises an exception indicating that the method is not implemented.
        """
        raise Exception("area() is not implemented")
