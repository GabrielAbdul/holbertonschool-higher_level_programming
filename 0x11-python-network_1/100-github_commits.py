#!/usr/bin/python3
'''docstrings'''


if __name__ == '__main__':

    import requests
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    re = requests.get(url)
    try:
        for i in range(0, 10):
            print('{}: {}'.format(re.json()[i]['sha'],
                                  re.json()[i]['commit']['author'].get('name')))
