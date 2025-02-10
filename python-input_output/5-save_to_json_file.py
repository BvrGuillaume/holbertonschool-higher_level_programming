#!/usr/bin/python3
"""Module to save an object to a JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.
    
    Args:
        my_obj: The object to serialize.
        filename: The name of the file to save the JSON data."""
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(my_obj, f)
