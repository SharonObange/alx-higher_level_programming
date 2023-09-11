#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        a1, a2 = tuple_a[:2]
    else:
        a1, a2 = (0, 0)
    if len(tuple_b) >= 2:
        b1, b2 = tuple_b[:2] 
    else:
        b1, b2 = (0, 0)
    
    result = (a1 + b1, a2 + b2)

    return result
