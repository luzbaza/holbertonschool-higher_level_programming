#!/usr/bin/python3
""" read_file """


def read_file(filename=""):
    """ function that reads a text file """

    with open(filename, encoding="utf-8") as readfile:
        print(readfile.read(), end="")
