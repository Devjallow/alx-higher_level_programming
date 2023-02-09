#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    values = list(a_dictionary.items())
    values.sort()
    for k, v in values:
        print("{}: {}".format(k, v))
