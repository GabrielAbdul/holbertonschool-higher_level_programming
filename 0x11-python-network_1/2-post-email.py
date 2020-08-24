#!/usr/bin/python3
'''ends a POST request to the passed URL with the email as a parameter
and displays the body of the response'''


if __name__ == '__main__':

    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]
    # application/x-www-form-urlencoded formatted headers into data
    data = urllib.parse.urlencode({'email': email})
    # data needs to be encoded to ascii
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        page = response.read().decode('utf8')
        print(page)
