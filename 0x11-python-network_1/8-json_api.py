#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":
    character = "" if len(sys.argv) == 1 else sys.argv[1]
    pack = {"q": character}
    ep = requests.post("http://0.0.0.0:5000/search_user", data=pack)
    try:
        response = ep.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
