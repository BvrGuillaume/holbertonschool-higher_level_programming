#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.
    :param data: Dictionary to serialize
    :param filename: Output JSON file name
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """
    Load data from a JSON file and deserialize it into a Python dictionary.
    :param filename: Input JSON file name
    :return: Deserialized dictionary
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)
