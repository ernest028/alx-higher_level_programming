#!/usr/bin/python3
"""
   This module contains matrix_divided, which divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """
    This function divides the elements of the input matrix
    All elements must be rounded off to 2 decimal places
    A new matrix must be returned

    Arguments:
      matrix: input matrix
      div: integer or float used in the division

    Return:
      new matrix with the resultant division

    Exceptions:
      TypeError: if matrix is not a list of integers or floats
      TypeError: if div is not an integer or a float
      ZeroError: if div is equal to 0
      TypeError: if each row of the matrix is not the same size

    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
