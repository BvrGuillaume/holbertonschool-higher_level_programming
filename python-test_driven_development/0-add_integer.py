#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats, converting floats to integers.

    Args:
        a: The first number, must be an integer or a float.
        b: The second number, defaults to 98, must be an integer or a float.

    Returns:
        The addition of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
