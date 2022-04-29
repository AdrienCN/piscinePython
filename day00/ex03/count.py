import sys
import string


def text_analyser(*args):
    """Return upper case, lower case and
    punctuation and spaces count from a text"""
    if len(args) > 1:
        print("ERROR")
        return

    text = ""
    if len(args) == 0:
        text = input("Enter your own text:\n")
    else:
        text = args[0]

    low = 0
    up = 0
    pun = 0
    space = 0
    for i in text:
        if i.isspace():
            space += 1
        elif i.islower():
            low += 1
        elif i.isupper():
            up += 1
        elif i in string.punctuation:
            pun += 1
    sum = low + up + pun + space
    print("This text contains ", str(len(text)), "characters of which:")
    print("-Uppercases: ", up)
    print("-Lowercases: ", low)
    print("-Spaces: ", space)
    print("-Punctuation: ", pun)
