#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    num = 0
    for num in range(x):
        try:
            print(my_list[num], end="")
            num += 1
        except IndexError as err:
            break
    print()
    return num
