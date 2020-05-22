#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    This module divides all elements of a matrix
    """

    type_err = 'matrix must be a matrix (list of lists) of integers/floats'
    num_elems = 0
    result_list = []

    if not matrix or type(matrix) is not list:
        raise TypeError(type_err)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    num_lists = len(matrix)
    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(type_err)
            num_elems += 1
    if num_elems % num_lists != 0:
        raise TypeError("Each row of the matrix must have the same size")

    # i gets assigned to matrix lists
    for i in matrix:
        result_list.append(list(map(lambda i: round((i / int(div)), 2), i)))

    return result_list
