#!/usr/bin/python3
"""Module to create class"""


def read_file(filename=""):
    """Reads a text file and prints the content."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
