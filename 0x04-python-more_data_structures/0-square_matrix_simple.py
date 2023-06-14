#!/usr/python3
def square_matrix_simple(matrix=[]):
    if (not matrix or not len(matrix)):
        return None
    return [[x ** 2 for x in row] for row in matrix]
