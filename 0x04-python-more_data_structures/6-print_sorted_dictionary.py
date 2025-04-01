#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list = sorted(a_dictionary.keys())
    for item in list:
        print("{:s}: {}".format(item, a_dictionary[item]))
