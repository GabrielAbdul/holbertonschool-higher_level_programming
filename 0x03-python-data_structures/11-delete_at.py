#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if not my_list or not my_list[idx]:
        return my_list
    my_list[idx:idx + 1] = []
    return my_list
