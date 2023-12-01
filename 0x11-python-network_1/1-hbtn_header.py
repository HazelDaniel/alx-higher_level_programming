#!/usr/bin/python3
"""this module fetches from a url using the urllib package"""


if __name__ == "__main__":
    import urllib.request
    import sys
    url_link = "https://alx-intranet.hbtn.io/status"

    if len(sys.argv) < 2:
        sys.exit()

    req = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(req) as request:
        if 'X-Request-Id' not in request.headers:
            sys.exit()
        print(request.getheader('X-Request-Id'))
