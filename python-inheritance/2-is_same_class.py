#!/usr/bin/python
"""function that checks if the obj
 is an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class,
      otherwise False.
    """
    return type(obj) is a_class
