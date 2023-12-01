#!/usr/bin/python3
""" a module that takes github credentials (username and password)
    from the command line and uses the Github API to display user id """

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    r = requests.get(url,
                     auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
