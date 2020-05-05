#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if not my_list:
        return None
    if idx < 0 or idx > len(my_list):
        return (my_list)
    new_list = my_list[:]
    for i in range(0, len(new_list)):
        if idx == 0:
            new_list[idx] = element
        if i == idx:
            new_list[idx] = element
    return new_list
