#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for item in set_1:
        if item not in set_2:
            new_set.append(item)
    for item in set_2:
        if item not in set_1:
            new_set.append(item)

    return new_set
