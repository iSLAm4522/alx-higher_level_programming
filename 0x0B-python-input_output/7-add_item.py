#!/usr/bin/python3
"""
    Script that adds all command line arguments to a Python list
    and saves them to a JSON file.
    This script loads existing items from a JSON file (if it exists),
    adds any command line arguments to the list, and saves the updated list
    back to the JSON file.
"""
import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = "add_item.json"
my_list = []

if os.path.exists(filename):
    my_list = load_from_json_file(filename)

if len(sys.argv) > 1:
    my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
