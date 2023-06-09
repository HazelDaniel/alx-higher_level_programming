#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if (not matrix) or matrix is None:
        return None
    tmp_print = [row[i] for row in matrix for i in range(len(row))]
    for i in range(len(tmp_print)):
        arr_len = len(matrix[0])
        if (i + 1) % (arr_len) == 0:
            print("{}".format(tmp_print[i]), end="\n")
        else:
            print("{}".format(tmp_print[i]), end=" ")
