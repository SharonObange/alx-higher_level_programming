#!/usr/bin/python3
"""This illustrates loading from JSON string"""
import json


def from_json_string(my_str):
    """Return object represented by a JSON string"""
    my_object = json.loads(my_str)
    return my_object
