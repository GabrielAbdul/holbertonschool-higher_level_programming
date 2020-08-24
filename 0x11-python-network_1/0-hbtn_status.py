#!/usr/bin/python3
'''Python script that fetches https://intranet.hbtn.io/status'''


if __name__ == '__main__':

    import urllib.request
    from urllib.parse import unquote

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print('Body response:')
        print(' - type: {}'.format(type(content)))
        print(' - content: {}'.format(content))
        print(' - utf8 content: {}'.format(content.decode('utf8')))
