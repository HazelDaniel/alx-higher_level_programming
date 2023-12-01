#!/usr/bin/python3
"""this module sends an http request to an endpoint
    with proper error handling"""


if __name__ == "__main__":
    import requests

    req_url = "https://alx-intranet.hbtn.io/status"

    req = requests.get(req_url)
    print(f"Body response:")
    print(f"    - type: {type(req.text)}")
    print(f"    - content: {req.text}")
