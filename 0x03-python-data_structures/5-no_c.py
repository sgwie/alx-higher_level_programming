#!/usr/bin/python3
def no_c(my_string):
    mydict = {67: None, 99: None}
    new_string = (my_string.translate(mydict))
    return new_string
