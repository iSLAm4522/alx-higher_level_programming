#!/usr/bin/python3
def islower(c):
    if len(c) != 1:
        return False
    if 'z' >= c >= 'a':
        return True
    else:
        return False
