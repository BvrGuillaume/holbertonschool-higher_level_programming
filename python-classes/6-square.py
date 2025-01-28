#!/usr/bin/python3
'''Module to create a class'''


class Square:
    """A class that defines a square with size and position."""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Initialize the square with a private size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size
    
    def my_print(self):
        if self.size == 0:
            print()
            return
        
        # Print spaces (new lines) based on position[1]
            for _ in range(self.__position[1]):
                print()

           # Print the square with space indentation for position[0]
           #  
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
