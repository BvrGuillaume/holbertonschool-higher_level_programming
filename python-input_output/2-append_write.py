#!/usr/bin/python3
"""append write fonction"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
