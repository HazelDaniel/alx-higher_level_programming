#!/usr/bin/python3
"""this module posts an input email to an input endpoint
    using the urllib package"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error
    import sys
    url_link = "https://alx-intranet.hbtn.io/status"

    if len(sys.argv) < 3:
        sys.exit()

    data = {}
    data["email"] = sys.argv[2]
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as request:
        try:
            parsed = request.read()
            print(parsed.decode('utf-8'))
        except urllib.error.URLError:
            print(Exception)
