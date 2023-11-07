#!/usr/bin/python3
"""
    This module contains a function to read a text file
"""


def read_file(filename=""):
    """
    This function reads a text file and prints the contents

    Args:
        filename

    Returns:
        none
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        pass
