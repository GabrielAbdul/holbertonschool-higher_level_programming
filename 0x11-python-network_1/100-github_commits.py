#!/usr/bin/python3
'''docstrings'''


if __name__ == '__main__':

    import requests
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    r = requests.get(url)
    for i in r.json()[:10]:
        print('{}: {}'.format(i['sha'],
                              i['commit']['author']['name']))
