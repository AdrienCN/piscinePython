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
