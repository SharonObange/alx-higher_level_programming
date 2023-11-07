#!/usr/bin/python3
""" This module demonstrates writing a string to a text file"""


def write_file(filename="", text=""):
    """ This function writes text to a file
    Returns the number of characters writen"""

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            chars = file.write(text)
            return chars
    except Exception:
        return 0
