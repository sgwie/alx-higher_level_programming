#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    new = (my_list[size::-1])
    print("{:d}".format(new))
