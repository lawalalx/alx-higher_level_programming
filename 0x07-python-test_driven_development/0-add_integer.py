#!/usr/bin/python3
def add_integer(a, b=98):
    """
        A function that adds two number a, and b
    """
    # Check if a is int or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    # Check if b is int or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    # Convert a and b to integers if they are floats
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return("{:d}".format((int(a) + int(b))))
