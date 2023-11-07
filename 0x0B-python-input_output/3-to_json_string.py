#!/usr/bin/python3
import json
""" This illustrates how to return the JSON rep of an object"""


def to_json_string(my_obj):
    """ Return JSON rep"""
    return json.dumps(my_obj)
