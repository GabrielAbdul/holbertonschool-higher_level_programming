#!/usr/bin/python3
''' Python script that takes in a URL
    sends a request'''


if __name__ == '__main__':
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
