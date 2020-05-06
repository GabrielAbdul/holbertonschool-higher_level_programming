#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    nums, nums_a, nums_b = [0, 0], [0, 0], [0, 0]

    if not tuple_a and not tuple_b:
        return None
    if len(tuple_a) == 1:
        tuple_a = tuple_a + (0,)
    elif len(tuple_b) == 1:
        tuple_b = tuple_b + (0,)
    if len(tuple_b) < 1:
        tuple_b = tuple_b + (0, 0)
    elif len(tuple_a) < 1:
        tuple_a = tuple_a + (0, 0)
    for i in range(0, 2):
        nums_a[i] = tuple_a[i]
        nums_b[i] = tuple_b[i]
    add_one = nums_a[0] + nums_b[0]
    add_two = nums_a[1] + nums_b[1]
    result = (add_one, add_two)
    return result
