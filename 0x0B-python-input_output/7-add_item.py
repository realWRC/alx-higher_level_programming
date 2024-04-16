#!/usr/bin/python3
"""
Program that adds all arguments to a Python list
and then save them to a JSON file.
"""

import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

savefile = "add_item.json"
data = []

if len(sys.argv) == 1:
    save_to_json_file(data, savefile)

if len(sys.argv) > 1:
    try:
        data = load_from_json_file(savefile)
    except Exception as e:
        print(e)
    for item in range(1, len(sys.argv)):
        data.append(sys.argv[item])
    save_to_json_file(data, savefile)
