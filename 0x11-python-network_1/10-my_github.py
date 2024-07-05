#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""

import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    perm = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    ep = requests.get("https://api.github.com/user", auth=perm)
    print(ep.json().get("id"))
