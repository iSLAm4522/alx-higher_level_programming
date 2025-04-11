#!/usr/bin/python3

"""
Module 5-text_indentation
Contains function text_indentation that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
    ., ? and :

    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delimiters = ".?:"
    line = ""

    for char in text:
        if char == '\n':
            if line.strip():
                print(line.strip())
            line = ""
        else:
            line += char
            if char in delimiters:
                parts = line.split(char)
                if len(parts) > 1:
                    print(parts[0].strip() + char)
                else:
                    print(line.strip())
                print()
                line = ""
    if line.strip():
        print(line.strip())
