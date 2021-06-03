#!/usr/bin/python3
""" append_write """


def append_write(filename="", text=""):
    """ unction that appends a string at the end of a text file """

    with open(filename, mode="a", encoding="utf-8") as appendFile:
        appendFile.write(text)
        return len(text)
