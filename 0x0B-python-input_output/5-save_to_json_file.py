#!/usr/bin/python3
""" save_to_json_file """

import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file """

    with open(filename, mode="w", encoding="UTF-8") as saveFile:
        json.dump(my_obj, saveFile)
