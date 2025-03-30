#!/usr/bin/python3
def uppercase(str):
    for char in str:
        result = "".join(chr(ord(char) - 32) if 'a' <= char <= 'z' else char)
        print("{:s}".format(result), end="")
    print()
