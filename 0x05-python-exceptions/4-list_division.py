#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    res = 0
    new_list = []
    for num in range(list_length):
        try:
            res = my_list_1[num] / my_list_2[num]
        except ZeroDivisionError:
            res = 0
            print("division by zero")
        except IndexError:
            res = 0
            print("out of range")
        except (TypeError, ValueError):
            res = 0
            print("wrong type")
        finally:
            new_list.append(res)
    return new_list
