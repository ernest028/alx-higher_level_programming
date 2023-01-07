#!/usr/bin/python3
"""
    This module contains say_my_name function which outputs a
    formatted string with the user's name
"""


def say_my_name(first_name, last_name=""):
    """
    This function returns a formatted string with the user's name

    Arguments:
      first_name: first name to be accesses
      last_name: last name to be accessed

    Return:
      formatted string

    Exceptions:
      TypeError: if either of the inputs is not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
