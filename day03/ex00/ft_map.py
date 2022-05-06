import sys
from functools import reduce 

def ft_map(function_to_apply, iterable):
    try:
        iter(iterable)
        for elem in iterable:
            yield function_to_apply(elem)
    except TypeError as msg:
        print("Error : ft_map : ", msg)
        return None

def ft_filter(function_to_apply, iterable):
    try:
        iter(iterable)
        for elem in iterable:
            if function_to_apply is None:
                if elem != False:
                    yield elem
            elif function_to_apply(elem):
                yield elem
    except TypeError as msg:
        print("Error : ft_filter : ",msg)
        return None

def ft_reduce(function_to_apply, iterable):
    try:
        iter(iterable)
        if len(iterable) == 0:
            return None
        value = iterable[0]
        for index in range(1, len(iterable)):
            value = function_to_apply(value, iterable[index])
        return value
    except TypeError as msg:
        print("Error: ft_reduce : ", msg)
        return None

def map_test(x):
    return x + 2

def filter_test(x):
    return  x % 2 == 0

def reduce_test(a, b):
    return a + b

foo = (1, 2, 3, 4, 5)
bar = (1, 2, 3, 4, 5)
# baz = ["S", "A", "L", "U", "T"]
# baz = ("S")

print("foo : ", foo, " | next(iter(foo))", next(iter(foo)))

try:
    print("\t\t***MAP***")
    print("Mine : ", list(ft_map(map_test, foo)))
    print("Official: ", list(map(map_test, foo)))
    

    print("\n\t\t***FILTER***")
    print("Mine : ",    list(ft_filter(filter_test, foo)))
    print("Official: ", list(filter(filter_test, foo)))
    
    print("\t\t***REDUCE***")
    print("Mine : ",    list(ft_reduce(reduce_test, baz)))
    print("Official : ",    list(reduce(reduce_test, baz)))
except TypeError as msg:
    print(msg)
