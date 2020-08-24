#!/usr/bin/python3
'''script that takes your Github credentials (username and password)
and uses the Github API to display your id'''


if __name__ == '__main__':

    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    try:
        print(response.json()['id'])
    except KeyError:
        print("None")
