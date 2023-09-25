#!/usr/bin/python3
def safe_print_integer(value):
    try:
        integer = "{:d}".format(value)
        print(integer)
        return True

    except ValueError:
        return False

    finally:
        print()
