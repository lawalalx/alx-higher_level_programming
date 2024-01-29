#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or not any(isinstance(sublist, list) for sublist in matrix):
        raise Exception("matrix must be a matrix (list of lists) of integers/floats")
    if not len(set([len(arr) for arr in matrix])) == 1:
        raise Exception("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise Exception("div must be a number")
    if div < 0:
        raise ZeroDivisionError("division by zero")

    nw = [[round((arr / div), 2) for arr in m] for m in matrix]
    return (nw)
