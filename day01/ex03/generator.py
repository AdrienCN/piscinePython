import sys
import random
import copy


def check_input(text, option=None):
    error = 0
    if not isinstance(text, str):
        error = 1
    if option:
        if not isinstance(option, str):
            error = 1
        if not (option == "shuffle"
                or option == "ordered"
                or option == "unique"):
            error = 1
        return (error)


def generator(text, sep=" ", option=None):
    if check_input(text, option):
        print("ERROR")
        exit()

    word_list = text.split(sep)
    if option:
        if option == "shuffle":
            tmp = copy.deepcopy(word_list)
            randlist = random.sample(range(0, len(word_list)), len(word_list))
            j = 0
            for i in randlist:
                word_list[i] = tmp[j]
                j += 1
        elif option == "ordered":
            word_list.sort()
        else:
            word_list = list(dict.fromkeys(word_list))
    for i in word_list:
        yield i
