import sys
import string


def check_isnumber(*args):
    for i in args:
        if not isinstance(i, int) and not isinstance(i, float):
            return (0)
    return (1)


def check_list(arg_list):
    if not isinstance(arg_list, list):
        return (0)
    if len(arg_list) == 0:
        return (0)
    # check float for COL vector
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


class Vector:

    def __init__(self, arg_one):

        # RANGE constructor
        if isinstance(arg_one, tuple):
            range_start = arg_one[0]
            range_end = arg_one[1]
            if len(arg_one) > 2:
                raise ValueError("Range constructor len > 2")
            if not check_isnumber(range_start, range_end):
                raise ValueError("Range constructor param error")
            i = range_start
            self.shape = range_end - range_start
            self.values = []
            if not self.shape >= 0:
                raise ValueError("Init range must be >= 0")
            while i < range_end:
                self.values.append([float(i)])
                i += 1
        else:

            # DEFAULT constructor
            if isinstance(arg_one, list):
                arg_list = arg_one
                if not check_list(arg_list):
                    raise ValueError("List constructor must be"
                                     "floats and cannot be empty")
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
            if not check_isnumber(size):
                raise ValueError("Size constructor param error")
            if not size >= 0:
                raise ValueError("Size init must be >= 0")
            i = 0.0
            self.values = []
            while i < size:
                self.values.append([float(i)])
                i += 1.0
            self.shape = (size, 1)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Vector + ", type(other), " not available")
        if self.shape != other.shape:
            raise ValueError("Operands [+] Vector have NOT "
                             "the same dimension")
        # ROW add
        tmp = []
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                tmp.append(self.values[i] + other.values[i])
        # COL add
    else:
        for i in range(self.shape[0]):
            tmp.append([self.values[i][0] + other.values[i][0]])
        return Vector(tmp)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Vector - ", type(other), " not available")
        if self.shape != other.shape:
            raise ValueError("Operands [-] Vector have NOT "
                             "the same dimension")
        tmp = []
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                tmp.append(self.values[i] - other.values[i])
        else:
            for i in range(self.shape[0]):
                tmp.append([self.values[i][0] - other.values[i][0]])
        return Vector(tmp)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, other):
        if not check_isnumber(other):
            raise ValueError("Vector / ", type(other), " not available")
        if other == 0:
            raise ValueError("TrueDiv : division by 0 forbidden")
        tmp = []
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                tmp.append(self.values[i] / other)
        else:
            for i in range(self.shape[0]):
                tmp.append([self.values[i][0] / other])
        return Vector(tmp)

    def __rtruediv__(self, other):
        raise ValueError("A scalar cannot be divided by a Vector")

    def __mul__(self, other):
        if not check_isnumber(other):
            raise ValueError("Vector * ", type(other), " not available")
        tmp = []
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                tmp.append(self.values[i] * other)
        else:
            for i in range(self.shape[0]):
                tmp.append([self.values[i][0] * other])
        return Vector(tmp)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return f"Vector shape : row {self.shape[0]} - col {self.shape[1]} " + \
                "| Vector Values = {self.values}"

    def __repr__(self):
        return f"Vector(shape({self.shape}), values({self.values}))"

    def dot(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Vector DOT ", type(other), " not available")
        if self.shape != other.shape:
            raise ValueError("Operands [DOT] Vector have NOT "
                             "the same dimension")
        tmp = []
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                tmp.append(self.values[i] * other.values[i])
        else:
            for i in range(self.shape[0]):
                tmp.append([self.values[i][0] * other.values[i][0]])
        return Vector(tmp)

    def T(self):
        tmp = []
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                tmp.append([self.values[i]])
        else:
            for i in range(self.shape[0]):
                tmp.append(self.values[i][0])
        return Vector(tmp)
