#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    list_keys = sorted(a_dictionary)

    for i in range(len(list_keys)):

        print("{}: {}".format(list_keys[i], a_dictionary[list_keys[i]]))
