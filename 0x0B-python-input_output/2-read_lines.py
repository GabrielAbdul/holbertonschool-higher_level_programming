#!/usr/bin/python3
"""Function that reads n lines of a text file UTF8 and prints it to stdout"""


def read_lines(filename="", nb_lines=0):
    """read_lines()
        Args:
            filename - name of the file
            nb_lines - limiter of lines to read from the file
    """
    line_num = 0
    with open(filename, encoding='UTF-8') as file:
        if nb_lines <= 0:
            print(file.read(), end='')
        for lines in file:
            print(lines, end='')
            line_num += 1
            if line_num == nb_lines:
                break
