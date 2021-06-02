#!/usr/bin/python3
""" number_of_lines """


def write_file(filename="", text=""):
    """ function that writes a string to a text file """

    with open(filename, 'w', encoding="utf-8") as writefile:
        return writefile.write(text)
