#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    new_matrix = list(map(list, matrix))

    lists = 0

    for i in new_matrix:

        new_matrix[lists] = list(map(lambda x: x ** 2, new_matrix[lists]))
        lists += 1
    return new_matrix
