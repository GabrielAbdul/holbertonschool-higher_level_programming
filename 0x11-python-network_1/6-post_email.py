#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)'''


if __name__ == '__main__':

    import requests
    from sys import argv

    print(requests.post(argv[1], data={'email': argv[2]}).text)
