#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    ep = requests.get(url)
    if ep.status_code >= 400:
        print("Error code: {}".format(ep.status_code))
    else:
        print(ep.text)
