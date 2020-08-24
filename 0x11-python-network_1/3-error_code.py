#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)'''


if __name__ == '__main__':

    import urllib.request
    import urllib.parse
    import sys

    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf8')
            print(html)
    except Exception as e:
        # e = HTTP Error 401: UNAUTHORIZED
        e = str(e)
        e = e.rsplit(' ')[2].replace(':', ' ')
        print('Error code: {}'.format(e))
