#!/usr/bin/python3

if __name__ == '__main__':
    import sys

x = 0
int(x)
for i in range(1, len(sys.argv)):
        x += int(sys.argv[i])
print("{}".format(x))
