#!/usr/bin/python3
'''takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter'''


if __name__ == '__main__':

    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    try:
        letter = argv[1]
        if type(letter) is not int:
            print('No result')
            exit()
        re = requests.post(url, data={'q': letter})
        if re.json() is not {}:
            print("[{}] {}".format(re.json()['id'], re.json()['name']))
    except IndexError:
        re = requests.post(url, data={'q': ''})
        if re.json() == {}:
            print('No result')
