#!/usr/bin/python3
"""Illustrates Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Read text from the file
    Search for string in text
    Add new string to text"""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(filename, 'w', encoding='utf-8') as file:
        for text in lines:
            file.write(text)

            if search_string in text:
                file.write(new_string + '\n')
