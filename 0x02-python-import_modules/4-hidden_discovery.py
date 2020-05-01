#!/usr/bin/python3


if __name__ == '__main__':
    import hidden_4
    import sys

name_list = dir(hidden_4)
for i in range(len(name_list)):
    if name_list[i][0] != '_' and name_list[i][1] != '_':
        print(name_list[i])
