def ft_map(function_to_apply, iterable):
    try:
        iter(iterable)
        for elem in iterable:
            yield function_to_apply(elem)
    except TypeError as msg:
        print("Error : ft_map : ", msg)
        return None
