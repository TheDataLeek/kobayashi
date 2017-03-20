import numpy as np
import matplotlib.pyplot as plt


class Arena(object):
    def __init__(self, m, n, layers=3):
        self.arena = np.empty((m, n, layers), dtype=object)

    def __str__(self):
        return str(self.arena)

    def show(self):
        plt.figure()
        plt.imshow(self.arena)
        plt.show()
