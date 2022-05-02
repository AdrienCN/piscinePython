import sys
import string

def check_isnumber(*args):
    for i in args:
        if not isinstance(i, int) \
            and not isinstance(i, float):
            return (0)
    return (1)


class  Vector:

    def __init__(self, arg_one, arg_two=None):
        if arg_one and arg_two:
            assert check_isnumber(arg_one, arg_two), "Range constructor param error"
            range_start = arg_one
            range_end = arg_two
            i = range_start
            self.shape = range_end - range_start
            self.values = []
            assert self.shape >= 0, "Init range must be >= 0"
            while i < range_end:
                self.values.append([float(i)])
                i += 1
        else:
            #Vector constructor (Row or Col)
            if isinstance(arg_one, list):
                arg_list = arg_one
                self.shape = len(arg_list)
                self.values = arg_list
            else:
               size = arg_one
               assert check_isnumber(size), "Size constructor param error"
               assert size >= 0, "Size init must be >= 0" 
               i = 0.0
               self.shape = size
               self.values = []
               while i < size:
                   self.values.append([i])
                   i += 1.0

foo = Vector(7)
bar = Vector([[1],[3]])
print("foo values : ", foo.values, " | shape : ", foo.shape)
print("bar values : ", bar.values, " | shape : ", bar.shape)


