#!/usr/bin/python3
"""this module sends an POST http request to an endpoint
    with proper error handling"""


if __name__ == "__main__":
    import requests
    import sys
    import json

    if len(sys.argv) < 2:
        exit()

    q_letter = sys.argv[1]
    headers = {"q": q_letter}
    res = requests.get("http://0.0.0.0:5000/search_user", headers=headers)
    try:
        json_res = res.json()
        if not json_res:
            print("No result")
    except json.decoder.JSONDecodeError:
        print("Not a valid json")
