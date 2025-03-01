#!/usr/bin/python3
"""append write fonction"""


def append_write(filename="", text=""):
    """Appends a string to a text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
