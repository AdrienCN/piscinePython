def ft_filter(function_to_apply, iterable):
    try:
        iter(iterable)
        for elem in iterable:
            if function_to_apply(elem):
                yield elem
    except TypeError as msg:
        print("Error : ft_filter : ", msg)
        return None
