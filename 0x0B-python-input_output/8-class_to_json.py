#!usr/bin/python3
"""This converts a class to JSON"""


def class_to_json(obj):
    """Returns dict descr for JSON serialization of an object"""
    if not hasattr(obj, '__dict__'):
        return None

    obj_dict = obj.__dict__
    serial_dict = []

    for key, value in obj_dict.items():
        if isintamce(value, (list, dict, str, int, bool)):
            serial_dict[key] = value

    return serial_dict
