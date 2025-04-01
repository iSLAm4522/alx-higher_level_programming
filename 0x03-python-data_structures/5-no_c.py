#!/usr/bin/python3

def no_c(my_string):
    new_str = [ch for ch in my_string if ch != 'c' and ch != 'C']
    return "".join(new_str)
