import numpy as np
import random


class NumPyCreator:

    def __init__(self):
        pass

    def from_list(self, lst):
        np_arr = None
        try:
            if isinstance(lst, list):
                np_arr = np.array(lst)
            else:
                raise TypeError("arg must be a list")
        except Exception as msg:
            pass
            # print("Error: from_list :\n", msg)
        return np_arr

    def from_tuple(self, tpl):
        np_arr = None
        try:
            if isinstance(tpl, tuple):
                np_arr = np.array(tpl)
            else:
                raise TypeError("arg must be a tuple")
        except Exception as msg:
            pass
            # print("Error: from_tuple :\n", msg)
        return np_arr

    def from_iterable(self, itr):
        np_arr = None
        try:
            if hasattr(itr, "__iter__"):
                np_arr = np.array(list(itr))
            else:
                raise TypeError("arg must be an iterable")
        except Exception as msg:
            pass
            # print("Error: from_iterable :\n", msg)
        return np_arr

    def from_shape(self, shape, value=0):
        np_arr = None
        try:
            if isinstance(shape, tuple):
                np_arr = np.full(shape, value)
            else:
                raise TypeError("shape must be a tuple")
        except Exception as msg:
            pass
            # print("Error: from_shape :\n", msg)
        return np_arr

    def random(self, shape):
        np_arr = None
        try:
            if isinstance(shape, tuple):
                np_arr = np.random.random(shape)
            else:
                raise TypeError("arg must be a tuple")
        except Exception as msg:
            pass
            # print("Error: from_random :\n", msg)
        return np_arr

    def identity(self, n):
        np_arr = None
        try:
            if isinstance(n, int):
                np_arr = np.identity(n)
            else:
                raise TypeError("arg must be an int")
        except Exception as msg:
            pass
            # print("Error: from_identity :\n", msg)
        return np_arr


npc = NumPyCreator()
print("Creating NumpyArray:")
print("From LIST:")
arr = npc.from_list([[], []])
print(arr)
arr = npc.from_list([[1, 2, 3], [6, 3, 4], [8, 5, 6]])
print(arr)

print("\nFrom TUPLE:")
arr = npc.from_tuple(("a", "b", "c"))
print(arr)

print("\nFrom ITERABLE:")
arr = npc.from_iterable(range(5))
print(arr)

print("\nFrom SHAPE:")
arr = npc.from_shape((0, 0))
print(arr)
arr = npc.from_shape((3, 5))
print(arr)

print("\nSize should be the same but value RANDOM:")
arr = npc.random((3, 5))
print("A:\n", arr)
arr = npc.random((3, 5))
print("B:\n", arr)
arr = npc.random((3, 5))
print("C:\n", arr)

print("\nIdentity:")
arr = npc.identity(4)
print(arr)

print("\nError check : None should appear 6 times")
print(npc.from_list("toto"))
print(npc.from_list([[1, 2, 3], [6, 3, 4], [8, 5, 6, 7]]))
print(npc.from_tuple(3.2))
print(npc.from_tuple(((1, 5, 8), (7, 5))))
print(npc.from_shape((-1, -1)))
print(npc.identity(-1))
