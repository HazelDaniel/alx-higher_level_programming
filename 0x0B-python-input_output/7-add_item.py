#!/usr/bin/python3
"""a module that defines a function that adds all command\
    line arguments to a pyton list and writes them to a file"""
import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    list = []
    for arg in sys.argv[1:]:
        list.append(arg)
    save_to_json_file(list, "add_item.json")
