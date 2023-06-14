#!/usr/python3
# def square_matrix_simple(matrix=[]):
#     return [[x ** 2 for x in row] for row in matrix]

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        row_arr = list()
        for col in row:
            row_arr.append(col ** 2)
        if row_arr:
            new_matrix.append(row_arr)
    if not matrix:
        return None
    return new_matrix
