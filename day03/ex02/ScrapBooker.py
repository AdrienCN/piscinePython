import copy
import numpy as np


def crop_var_check(array, dim, position):
    if isinstance(array, np.ndarray)\
        and isinstance(dim, tuple)\
        and isinstance(position, tuple)\
        and all(isinstance(x, int) for x in dim)\
        and all(isinstance(x, int) for x in position)\
        and all(x >= 0 for x in dim)\
        and all(x >= 0 for x in position)\
        and position[0] <= array.shape[0]\
        and position[1] <= array.shape[1]\
        and array.shape[0] - position[0] <= dim[0]\
            and array.shape[1] - position[1] <= dim[1]:
        print("Review crop error check1")
        return 1
    return 0


def thin_var_check(array, n, axis):
    if isinstance(array, np.ndarray)\
        and isinstance(n, int)\
        and n > 0\
        and isinstance(axis, int)\
            and axis >= 0:
        # Vertical case
        if axis == 0:
            if n < array.shape[1]:
                return 1
        else:
            if n < array.shape[0]:
                return 1
    return 0


def juxtapose_var_check(array, n, axis):
    if isinstance(array, np.ndarray)\
        and isinstance(n, int)\
        and isinstance(axis, int)\
        and n > 0\
            and (axis == 0 or axis == 1):
        return 1
    return 0


class ScrapBooker:

    def __init__(self):
        pass

    def crop(self, array, dim, position=(0, 0)):
        if crop_var_check(array, dim, position):
            cropped_arr = array[position[0]:dim[0], position[1]:dim[1]]
            return cropped_arr
        return None

    def thin(self, array, n, axis):
        if thin_var_check(array, n, axis):
            thin = None
            if axis == 0:
                thin = np.delete(array, list(range(n - 1,
                                 array.shape[1], n)), 1)
            else:
                thin = np.delete(array, list(range(n - 1,
                                 array.shape[0], n)), 0)
            return thin
        return None

    def juxtapose(self, array, n, axis):
        if juxtapose_var_check(array, n, axis):
            jux_arr = array
            for i in range(n - 1):
                jux_arr = np.concatenate((jux_arr, array), axis)
            return jux_arr
        return None

    def mosaic(self, array, dim):
        if isinstance(array, np.ndarray)\
            and isinstance(dim, tuple)\
            and all(isinstance(x, int) for x in dim)\
            and len(dim) == 2\
                and (dim[0] >= 0 and dim[1] >= 0):
            mosaic_arr = self.juxtapose(array, dim[0], 0)
            mosaic_arr = self.juxtapose(mosaic_arr, dim[1], 1)
            return mosaic_arr
        return None


sb = ScrapBooker()

# CROP
arr = np.arange(0, 25).reshape(5, 5)
sb.crop(arr, (3, 1), (1, 0))

# THIN
arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
sb.thin(arr3, 3, 1)

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
sb.thin(arr2, 3, 0)

# JUXTAPOSE
arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sb.juxtapose(arr4, 0, 0)

sb.mosaic(arr4, (2, 3))

print("ERROR CHECK NOTHING SHOULD APPEAR")
not_numpy_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sb.crop(not_numpy_arr, (1, 2))
sb.juxtapose(arr4, -2, 0)
sb.mosaic(arr4, (1, 2, 3))
