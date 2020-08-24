#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)'''


if __name__ == '__main__':

    import requests

    response = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print(' - type: {}'.format(type(response.text)))
    print(' - content: {}'.format(response.text))
