#!/usr/bin/python3


def multiple_returns(sentence):
    my_list = [0, 0]
    if not sentence:
        fst_chr = None
    elif sentence:
        fst_chr = sentence[0]
    my_list[0] = len(sentence)
    my_list[1] = fst_chr

    return tuple(my_list)
