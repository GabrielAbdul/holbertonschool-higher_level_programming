#!/usr/bin/python3
'''Technical interview preparation'''


def find_peak(list_of_integers):
    '''function that finds a peak in a list of unsorted integers'''
    if list_of_integers == []:
        return None
    back = len(list_of_integers) - 1
    for i in range(len(list_of_integers) - 1):
        if list_of_integers[i] == list_of_integers[back]:
            max_num = list_of_integers[i]
        max_num = list_of_integers[i] if list_of_integers[i] > list_of_integers[back] else list_of_integers[back]
        back = back - 1
    return max_num
