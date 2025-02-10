#!/usr/bin/python3
"""Module to create a class"""


def write_file(filename="", text=""):
    """write a string and return the nb of character written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
