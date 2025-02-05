#!/usr/bin/env python3
"""Module to create class"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal class"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """A class representing a soubclass of animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """A class representing a soubclass of animal"""
    def sound(self):
        return "Meow"
