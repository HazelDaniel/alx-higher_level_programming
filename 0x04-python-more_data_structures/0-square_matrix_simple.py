#!/usr/python3
# def square_matrix_simple(matrix=[]):
#     new_matrix = []
#     for row in matrix:
#         row_arr = list(map(lambda x: x ** 2, row))
#         new_matrix.append(row_arr)
#     if not matrix:
#         return None
#     return new_matrix


def square_matrix_simple(matrix=[]):
    if len(matrix) == 0 or matrix is None:
        return (None)
    new_matrix = []
    for each in matrix:
        new_matrix.append([x ** 2 for x in each])
    return (new_matrix)
