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
        blue_arr = np.zeros(array.shape)
        return blue_arr

    def to_green(self, array):
        pass

    def to_red(self, array):
        pass

    def to_grayscale(self, array):
        pass


imp = ImageProcessor()
arr = imp.load("elon.png")
pyplot.imshow(arr)
pyplot.show()
print(arr.shape)
cf = ColorFilter()
print(arr)
invert_arr = cf.invert(arr)
#blue_arr = cf.to_blue(arr)
#print(blue_arr)
pyplot.imshow(invert_arr)
pyplot.show()
