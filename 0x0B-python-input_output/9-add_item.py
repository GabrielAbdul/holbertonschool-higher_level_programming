#!/usr/bin/python3
"""script that adds all args to a python list, and then
saves them into a file"""


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

from sys import argv

try:
    arg_list = load_from_json_file('add_item.json')
    arg_list = list(arg_list)
except Exception:
    arg_list = []
    save_to_json_file(arg_list, 'add_item.json')

arg_list.append(argv[1:])

save_to_json_file(arg_list, 'add_item.json')
