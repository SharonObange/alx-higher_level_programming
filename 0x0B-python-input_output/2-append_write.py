#!/usr/bin/python3
"""THis demonstrates how to append a string to a file"""


def append_write(filename="", text=""):
    """Append string to file
    Return number of characters added"""

    try:
        with open(filename, 'a', encoding='utf-8')as file:
            chars = file.write(text)
            return chars
    except Exception:
        return 0
