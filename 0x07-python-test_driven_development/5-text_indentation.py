#!/usr/bin/python3
"""
   This module contains text_indentation which prints a text with 2
   new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints text with 2 new lines after these characters:
      '.', '?', ':'
    There should be no space at the beginning or end of the printed line

    Arguments:
      text: input text

    Return:
      formatted text

    Exceptions:
      TypeError: if text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1
