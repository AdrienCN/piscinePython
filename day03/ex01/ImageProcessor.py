from matplotlib import image
from matplotlib import pyplot
import numpy as np


class ImageProcessor:
    def __init__(self):
        pass

    def load(self, path):
        try:
            img = image.imread(path)
            print("Loading image of dimension {} x {}"
                  .format(img.shape[0], img.shape[1]))
            arr = np.array(img)
        except Exception as msg:
            print("Error Load :\n", msg)
            return None
        return arr

    def display(self, array):
        try:
            pyplot.imshow(array)
            pyplot.show()
        except Exception as msg:
            print("Error Display :\n", msg)
        return
