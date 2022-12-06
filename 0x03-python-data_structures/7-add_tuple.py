#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    size1 = len(tuple_a)
    size2 = len(tuple_b)
    if size1 == 1:
        tuple_a = tuple_a[0], 0
    if size2 == 1:
        tuple_b = tuple_b[0], 0
    if size1 == 0:
        tuple_a = 0, 0
    if size2 == 0:
        tuple_b = 0, 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
