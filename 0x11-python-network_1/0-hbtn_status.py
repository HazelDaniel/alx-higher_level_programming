#!/usr/bin/python3
"""this module fetches from a url using the urllib package"""

if __name__ == "__main__":
    import urllib.request

    url_link = "https://alx-intranet.hbtn.io/status"

    req = urllib.request.Request(url_link)

    with urllib.request.urlopen(req) as request:
        res_byte = request.read()
        res_utf = res_byte.decode('utf-8')
        print("Body response:")
        print(f"    - type: {type(res_byte)}")
        print(f"    - content: {res_byte}")
        print(f"    - utf8 content: {res_utf}")
