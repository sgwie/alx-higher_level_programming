def simple_delete(a_dictionary, key=""):
    for i in a_dictionary:
        if i == key:
            del a_dictionary[key]
            return a_dictionary
        else:
            return a_dictionary
