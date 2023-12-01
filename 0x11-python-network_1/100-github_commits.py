#!/usr/bin/python3
""" a module that lists the commits of a user's
    repo in the format => <sha>: <author name>"""

if __name__ == '__main__':
    import requests
    import sys
    url = "https://api.github.com/repos/{}/{}/commits".\
        format(sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
