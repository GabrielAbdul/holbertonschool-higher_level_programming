#!/usr/bin/python3
'''takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter'''


if __name__ == '__main__':

    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    try:
        letter = argv[1]
    except IndexError:
        print("No result")
        quit()
    re = requests.post(url, data={'q': letter})
    try:
        json_obj = re.json()
        if json_obj is not {}:
            print("[{}] {}".format(re.json()['id'], re.json()['name']))
        else:
            print("No Result")
    except Exception:
        print("Not a valid JSON")
