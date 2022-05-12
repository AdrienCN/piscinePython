from ImageProcessor import ImageProcessor
from matplotlib import pyplot
import numpy as np

class ColorFilter:

    def __init__(self):
        pass

    def invert(self, array):
        if not isinstance(array, np.ndarray):
            return None
        return 1 - array[:, :, :3]

    def to_blue(self, array):
        if not isinstance(array, np.ndarray):
            return None
        blue_arr = np.zeros((array.shape[0], array.shape[1], 3))
        blue_arr[..., 2:3] = array[..., 2:3]
        return blue_arr

    def to_green(self, array):
        if not isinstance(array, np.ndarray):
            return None
        return [0, 1, 0] * array[..., :3]

    def to_red(self, array):
        if not isinstance(array, np.ndarray):
            return None
        green = self.to_green(array)
        blue = self.to_blue(array)
        return array[..., 0:3] - (green[..., 0:3] + blue[..., 0:3])

    def to_grayscale(self, array, filter, **kwargs):
        gray_arr = None
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(filter, str)\
            and (filter != "w" and filter != "weight"\
            and filter != "mean" and filter != "m"):
            return None
        if (filter == "mean" or filter == "m"):
           
            test = np.sum([2, 3, 4])
            print("Test: ", test)
            gray_arr = np.tile(array[..., 0:3], 1)
            gray_arr[:, :, 0:1] = np.sum([0.299 * array[..., 0:1],\
                                  0.587 * array[..., 1:2],\
                                  0.114 * array[..., 2:3]])

            gray_arr[:, :, 1:2] = np.sum([0.299 * array[..., 0:1],\
                                  0.587 * array[..., 1:2],\
                                  0.114 * array[..., 2:3]])

            gray_arr[:, :, 2:3] = np.sum([0.299 * array[..., 0:1],\
                                  0.587 * array[..., 1:2],\
                                  0.114 * array[..., 2:3]])

            return gray_arr
        else:
            if len(kwargs) != 3 :
                return None
            lst = list(kwargs.values())
            if not all(isinstance(x, float) for x in lst):
                return None
            if sum(lst) != 1:
                return None
            gray_arr = np.tile(array[..., 0:3], 1)
            gray_arr[..., 0:1] = gray_arr[..., 0:1] * lst[0]
            gray_arr[..., 1:2] = gray_arr[..., 1:2] * lst[1]
            gray_arr[..., 2:3] = gray_arr[..., 2:3] * lst[2]
            return gray_arr

imp = ImageProcessor()
arr = imp.load("elon.png")
cf = ColorFilter()

"""
# Original Img
imp.display(arr)

# Inverted Img

invert_arr = cf.invert(arr)
imp.display(invert_arr)
imp.display(arr)


# Blue Filter
blue_arr = cf.to_blue(arr)
imp.display(blue_arr)
imp.display(arr)

# Green Filter
green_arr = cf.to_green(arr)
imp.display(green_arr)
imp.display(arr)

# Red Filter
red_arr = cf.to_red(arr)
imp.display(red_arr)
imp.display(arr)
"""
# Gray
gray_arr = cf.to_grayscale(arr, "m")
imp.display(gray_arr)
imp.display(arr)
"""
gray_arr = cf.to_grayscale(arr, "w", a=0.0, b=0.0, c=1.0)
imp.display(gray_arr)
imp.display(arr)

gray_arr = cf.to_grayscale(arr, "w", a=1.0, b=0.0, c=0.0)
imp.display(gray_arr)
imp.display(arr)
"""
