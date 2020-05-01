#!/usr/bin/python3

if __name__ == "__main__":
    import sys

args = sys.argv
x = 1
arg_len = len(args)
if arg_len == 2:
    print("1 argument:")
elif arg_len == 1:
    print("0 arguments.")
elif arg_len > 2:
    print("{} arguments:".format(arg_len - 1))
for i in range(1, arg_len):
    if arg_len > 1:
        print("{}: {}".format(i, args[i]))
