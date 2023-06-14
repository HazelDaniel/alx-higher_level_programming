#!/usr/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        row_arr = list(map(lambda x: x ** 2, row))
        new_matrix.append(row_arr)
    if not matrix:
        return None
    return new_matrix
