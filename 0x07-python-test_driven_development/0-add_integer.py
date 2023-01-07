#!/usr/bin/python3
def add_integer(a, b=98):
    """adds two integers
    Args:
       a: 1st argument
       b: 2nd argument
    Return:
       a+b
    Raises:
       TypeError: If either argument is not of type int or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
