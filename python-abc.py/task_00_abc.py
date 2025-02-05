#!/usr/bin/env python3
"""Module to create class"""

from abc import ABC, abstractmethod

"""Animal class"""


class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass

"""A class representing a soubclass of animal"""
class Dog(Animal):
    def sound(self):
        return "Bark"

"""A class representing a soubclass of animal"""
class Cat(Animal):
    def sound(self):
        return "Meow"
