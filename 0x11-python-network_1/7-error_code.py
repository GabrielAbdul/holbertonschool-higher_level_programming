#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)'''


if __name__ == '__main__':

    import requests
    from sys import argv

    try:
        response = requests.get(argv[1])
        if response.status_code >= 400:
            print('Error code: {:d}'.format(response.status_code))
    except:
        print(response.text)
