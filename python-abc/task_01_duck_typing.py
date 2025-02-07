#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

#abstract class Shape



class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate & return the aera of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate & return the perimeter of the shape"""
        pass
#Circle class inherit from Shape


class Circle(Shape):
    def __init__(self, radius): # radius est le rayon du cercle en FR
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2
    #calcule l'air du cercle avec la formule πr où r est le rayon du cercle
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    #Rectangle class inherit from Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
#Shape_info function duck typing


def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


# Testing the classes and the shape_info function
if __name__ == "__main__":
    # Create a Circle with a radius of 5
    circle = Circle(5)
    print("Circle Info:")
    shape_info(circle)

    print("\nRectangle Info:")
    # Create a Rectangle with a width of 3 and height of 4
    rectangle = Rectangle(3, 4)
    shape_info(rectangle)
