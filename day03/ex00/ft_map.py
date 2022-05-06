import sys
import copy


def ft_map(func, iterable):
    try:
        iter(iterable)
    except TypeError:
        print("arg <iterable> is not an Iterator")
    for elem in iterable:
        yield func(elem)


def dummy(x):
    return x + "a"


foo = ("a", "b")
print("Mine : ", list(ft_map(dummy, foo)))
print("Official: ", list(map(dummy, foo)))
