#!/usr/bin/python3
"""this module sends an http request to an endpoint
    with proper error handling"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error
    import sys
    url_link = "https://alx-intranet.hbtn.io/status"

    if len(sys.argv) < 2:
        sys.exit()

    req = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(req) as request:
        try:
            parsed = request.read()
            print(parsed.decode('utf-8'))
        except urllib.error.HTTPError as e:
            print(f"Error code: {e.code}")
