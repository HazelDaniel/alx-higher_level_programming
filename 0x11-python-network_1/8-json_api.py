#!/usr/bin/python3
"""this module sends an POST http request to an endpoint
    with proper error handling"""


if __name__ == "__main__":
    import requests
    import sys
    import json

    q_letter = ""
    if len(sys.argv) > 1:
        q_letter = sys.argv[1]
    headers = {"q": q_letter}
    res = requests.get("http://0.0.0.0:5000/search_user", headers=headers)
    json_res = {}
    bool_res = 0
    try:
        json_res = res.json()
        if not json_res:
            print("No result")
            bool_res = 1
        else:
            print(f"[{json_res['id']}] {json_res['name']}")
    except json.decoder.JSONDecodeError:
        if not bool_res:
            print("Not a valid JSON")
