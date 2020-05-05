#!/usr/bin/python3


def multiple_returns(sentence):
    my_list = [0, 0]
    if not sentence:
        fst_chr = None
    my_list[0] = len(sentence)
    my_list[1] = sentence[0]

    return tuple(my_list)
