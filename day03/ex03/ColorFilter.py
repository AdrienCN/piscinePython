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
            and (filter != "w" and filter != "weight"
                 and filter != "mean" and filter != "m"):
            return None
        if (filter == "mean" or filter == "m"):
            r = 0.299
            g = 0.587
            b = 0.114
        else:
            if len(kwargs) != 3:
                return None
            lst = list(kwargs.values())
            if not all(isinstance(x, float) for x in lst):
                return None
            if sum(lst) != 1:
                return None
            r = lst[0]
            g = lst[1]
            b = lst[2]
        means = [r, g, b]
        gray_arr = np.tile(array[..., 0:3], 1)
        gray_arr = gray_arr[..., [0, 1, 2]] * means
        sum_arr = np.sum(gray_arr, 2)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                gray_arr[i, j, [0, 1, 2]] = [sum_arr[i, j],
                                             sum_arr[i, j],
                                             sum_arr[i, j]]
        return gray_arr


imp = ImageProcessor()
arr = imp.load("elon.png")
cf = ColorFilter()

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

# Gray
gray_arr = cf.to_grayscale(arr, "m")
imp.display(gray_arr)
imp.display(arr)

gray_arr = cf.to_grayscale(arr, "w", a=0.0, b=0.0, c=1.0)
imp.display(gray_arr)
imp.display(arr)

gray_arr = cf.to_grayscale(arr, "w", a=1.0, b=0.0, c=0.0)
imp.display(gray_arr)
imp.display(arr)
