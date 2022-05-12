from ImageProcessor import ImageProcessor
from matplotlib import pyplot
import numpy as np

class ColorFilter:

    def __init__(self):
        pass

    def invert(self, array):
        if not isinstance(array, np.ndarray):
            return None
        invert_arr = 1 - array[:, :, :3]
        return invert_arr

    def to_blue(self, array):
        if not isinstance(array, np.ndarray):
            return None
        blue_arr = np.zeros(array.shape)
        blue_arr[..., 2:4] = array[..., 2:4]
        return blue_arr

    def to_green(self, array):
        if not isinstance(array, np.ndarray):
            return None
        green_arr = array[...]
        green_arr = [0, 1, 0, 1] * green_arr[..., :4]
        return green_arr

    def to_red(self, array):
        if not isinstance(array, np.ndarray):
            return None
        green = self.to_green(array)
        blue = self.to_blue(array)
        red_arr = array[...]
        red_arr[..., 1:2] -= green[..., 1:2]
        red_arr[..., 2:3] -= blue[..., 2:3]
        return red_arr

    def to_grayscale(self, array, filter, **kwargs):
        gray_arr = None
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(filter, str)\
            and (filter != "w" and filter != "weight"\
            and filter != "mean" and filter != "m"):
            return None
        if (filter == "mean" or filter == "m"):
            gray_arr = array[...]
            gray_arr[..., 0:3] = (gray_arr[..., 0:1] * 0.299\
                                  + gray_arr[..., 1:2] * 0.587\
                                  + gray_arr[..., 2:3] * 0.114)\
                                  / 3
            return gray_arr
        else:
            if len(kwargs) != 3 :
                return None
            lst = list(kwargs.values())
            print("List : ", lst)
            if not all(isinstance(x, float) for x in lst):
                return None
            print(sum(lst))
            if sum(lst) != 1:
                print("sum is not 1")
                return None
            gray_arr = array[...]
            gray_arr[..., 0:3] = (gray_arr[..., 0:1] * lst[0]\
                                  + gray_arr[..., 1:2] * lst[1]\
                                  + gray_arr[..., 2:3] * lst[2])\
                                  / 3

            return gray_arr

imp = ImageProcessor()
arr = imp.load("elon.png")
cf = ColorFilter()

# Original Img
#pyplot.imshow(arr)
#pyplot.show()

# Inverted Img
"""
invert_arr = cf.invert(arr)
pyplot.imshow(blue_arr)
pyplot.show()
"""

# Blue Filter
"""
blue_arr = cf.to_blue(arr)
pyplot.imshow(blue_arr)
pyplot.show()
"""

# Green Filter
"""
green_arr = cf.to_green(arr)
pyplot.imshow(green_arr)
pyplot.show()
"""

# Red Filter
"""
red_arr = cf.to_red(arr)
pyplot.imshow(red_arr)
pyplot.show()
"""
# Gray
"""
gray_arr = cf.to_grayscale(arr, "m", a=0.299, b=0.587, c=0.114)
pyplot.imshow(gray_arr)
pyplot.show()
"""

gray_arr = cf.to_grayscale(arr, "w", a=0.4, b=0.6, c=0.0)
pyplot.imshow(gray_arr)
pyplot.show()

