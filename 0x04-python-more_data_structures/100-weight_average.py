#!/usr/bin/python3


def weight_average(my_list=[]):

    if not my_list:
        return 0

    # multiplies individual tuples together
    for tuples in my_list:
        elements = list(map(lambda x: x[0] * x[1], my_list))

    dividend = 0
    for tuples in my_list:
        dividend += tuples[1]

    divisor = 0
    for elem in elements:
        divisor += elem

    result = divisor / dividend

    return result
