import sys
import random
import copy


def check_input(text, sep, option):
    if not isinstance(text, str)\
        or not isinstance(sep, str)\
            or not isinstance(option, str):
        return -1
    if len(sep) == 0:
        return -1
    if option:
        if (option != "shuffle"
            and option != "ordered"
                and option != "unique"):
            return -1
    return (0)


def generator(text, sep=" ", option=None):
    if check_input(text, sep, option):
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
