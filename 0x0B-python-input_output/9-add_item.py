#!/usr/bin/python3
"""script that adds all args to a python list, and then
saves them into a file"""


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

from sys import argv

try:
        
