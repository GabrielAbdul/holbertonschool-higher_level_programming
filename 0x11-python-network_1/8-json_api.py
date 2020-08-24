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
        response = requests.post(url, data={'q': letter})
        json_obj = response.json()
        if not json_obj:
            print('Not a valid JSON')
        if json_obj is not {}:
            print("[{}] {}".format(response.json()['id'], response.json()['name']))
    except IndexError:
        response = requests.post(url, data={'q': ''})
        if response.json() == {}:
            print('No result')
