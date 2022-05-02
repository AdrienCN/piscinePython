import sys
import string

def check_isnumber(*args):
    for i in args:
        if not isinstance(i, int) \
            and not isinstance(i, float):
            return (0)
    return (1)
def check_list(arg_list):
    if not isinstance(arg_list, list):
        return (0)
    #check float for COL vector
    if isinstance(arg_list[0], list):
        for sublist in arg_list:
            for elem in sublist:
                if not isinstance(elem, float):
                    return (0)
    else:
        for elem in arg_list:
            if not isinstance(elem, float):
                return (0)
    return (1)

class  Vector:

    def __init__(self, arg_one, arg_two=None):
        
        # RANGE constructor
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

            # DEFAULT constructor
            if isinstance(arg_one, list):
                arg_list = arg_one
                assert check_list(arg_list), "List constructor must be floats and cannot be empty" 
                self.values = arg_list
                # Liste de Liste : COL
                if isinstance(arg_list[0], list):
                    self.shape = (len(arg_list), 1)
                # List  : ROW
                else:
                    self.shape = (1, len(arg_list))

            # SIZE constructor
            else:
               size = arg_one
               assert check_isnumber(size), "Size constructor param error"
               assert size >= 0, "Size init must be >= 0" 
               i = 0.0
               self.values = []
               while i < size:
                   self.values.append([i])
                   i += 1.0
               self.shape = (size, 1)

foo = Vector(3)
bar = Vector([3.0, 2.0])
print("COL values : ", foo.values, " | shape : ", foo.shape)
print("ROW values : ", bar.values, " | shape : ", bar.shape)


