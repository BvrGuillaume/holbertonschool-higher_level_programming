#!/usr/bin/env python3
import pickle

def display(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Is Student: {self.is_student}")


def serialize(self, filename: str):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
    except Exception as e:
        print(f"Serialization error: {e}")


@classmethod
def deserialize(cls, filename: str):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, pickle.PickleError, EOFError) as e:
        print(f"Deserialization error: {e}")
        return None
