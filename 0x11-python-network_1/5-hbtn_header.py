#!/usr/bin/python3
"""this module sends an http request to an endpoint
    with proper error handling"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 2:
        exit()
    req_url = sys.argv[1]
    res = requests.get(req_url)
    if 'X-Request-Id' in res.headers.keys():
        print(res.headers['X-Request-Id'])
