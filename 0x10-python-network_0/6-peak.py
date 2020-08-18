#!/usr/bin/python3
'''Technical interview preparation'''


def find_peak(list_of_integers):
    '''function that finds a peak in a list of unsorted integers'''
    if list_of_integers == []:
        return None
    b = len(list_of_integers) - 1
    for f in range(len(list_of_integers) - 1):
        if list_of_integers[f] == list_of_integers[b]:
            max_num = list_of_integers[f]
        max_num = list_of_integers[f] if\
            list_of_integers[f] > list_of_integers[b] else list_of_integers[b]
        b = b - 1
    return max_num
