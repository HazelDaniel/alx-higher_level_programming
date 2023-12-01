#!/usr/bin/python3
"""this module sends an POST http request to an endpoint
    without proper error handling"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 2:
        exit()

    req_url = sys.argv[1]
    res = requests.get(req_url)
    if (int(res.status_code) >= 400):
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
