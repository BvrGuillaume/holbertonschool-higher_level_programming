#!/usr/bin/python3
"""module to create a student class"""


class Student:
    # Initialization of the Student class with attributes
    #  first_name, last_name, and age
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    # Method that returns the dictionary representation of the Student instance
    def to_json(self):
        return self.__dict__
