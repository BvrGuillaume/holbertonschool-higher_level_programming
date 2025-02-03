#!/usr/bin/python3
class MyList(list):
    """A subclass of list that adds a method to print the list in sorted order."""
    
    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        try:

            print(sorted(self))
        except TypeError:
            raise TypeError("unordonerable types: noneType() <int()")
