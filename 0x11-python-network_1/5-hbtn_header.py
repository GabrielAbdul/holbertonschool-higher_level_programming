#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)'''


if __name__ == '__main__':

    import requests
    from sys import argv

    try:
        print(requests.get(argv[1]).headers['X-Request-Id'])
    except Exception:
        pass
