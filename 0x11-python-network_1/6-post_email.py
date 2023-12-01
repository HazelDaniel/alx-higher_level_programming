#!/usr/bin/python3
"""this module sends an http request to an endpoint
    with proper error handling"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 3:
        exit()

    headers = {"email": sys.argv[2]}
    req_url = sys.argv[1]
    res = requests.get(req_url, headers=headers)
    print(res.text)
