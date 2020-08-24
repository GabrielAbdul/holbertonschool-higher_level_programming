#!/usr/bin/python3
'''docstrings'''


if __name__ == '__main__':

    import requests
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])
    re = requests.get(url)
    for i in range(len(re.json()) - 11, len(re.json())):
        print('{}: {}'.format(re.json()[i]['sha'],
                              re.json()[i]['commit']['author']['name']))