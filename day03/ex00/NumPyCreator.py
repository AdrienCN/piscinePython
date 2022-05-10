import numpy as np
import random


class NumPyCreator:

    def from_list(self, lst):
        np_arr = None
        try:
            if isinstance(lst, list):
                np_arr = np.array(lst)
            else:
                raise TypeError("arg must be a list")
        except Exception as msg:
            print("Error: from_list :\n", msg)
        return np_arr

    def from_tuple(self, tpl):
        np_arr = None
        try:
            if isinstance(tpl, tuple):
                np_arr = np.array(tpl)
            else:
                raise TypeError("arg must be a tuple")
        except Exception as msg:
            print("Error: from_tuple :\n", msg)
        return np_arr

    def from_iterable(self, itr):
        np_arr = None
        try:
            if hasattr(itr, "__iter__"):
                np_arr = np.array(list(itr))
            else:
                raise TypeError("arg must be an iterable")
        except Exception as msg:
            print("Error: from_iterable :\n", msg)
        return np_arr

    def from_shape(self, shape, value=0):
        np_arr = None
        try:
            if isinstance(shape, tuple):
                np_arr = np.full(shape, value)
            else:
                raise TypeError("shape must be a tuple")
        except Exception as msg:
            print("Error: from_shape :\n", msg)
        return np_arr

    def random(self, shape):
        np_arr = None
        try:
            if isinstance(shape, tuple):
                np_arr = np.random.random(shape)
            else:
                raise TypeError("arg must be a tuple")
        except Exception as msg:
            print("Error: from_random :\n", msg)
        return np_arr

    def identity(self, n):
        np_arr = None
        try:
            if isinstance(n, int):
                np_arr = np.identity(n)
            else:
                raise TypeError("arg must be an int")
        except Exception as msg:
            print("Error: from_identity :\n", msg)
        return np_arr
