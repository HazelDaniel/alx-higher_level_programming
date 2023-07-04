#!/usr/bin/python3
""" This about dividing the list of list of int and float by divisor """


def matrix_divided(matrix, div):
    """a function that divides through by matrix """
    if (not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(num, list) for num in matrix)
        or not all((isinstance(elem, int))
        or (isinstance(elem, float))
         for elem in [a for b in matrix for a in b])):
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")
    if not (all(len(a) == len(matrix[0]) for a in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if not ((isinstance(div, int)) or (isinstance(div, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return ([list(map((lambda x: round(x / div, 2)), row)) for row in matrix])
