#!/usr/bin/python3


def read_file(filename=""):
    """
    This module reads a text file (UTF8) and prints the content

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
