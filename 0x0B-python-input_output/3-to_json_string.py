#!/usr/bin/python3
""" This illustrates how to return the JSON rep of an object"""
import json


def to_json_string(my_obj):
    """ Return JSON rep"""
    return json.dumps(my_obj)
