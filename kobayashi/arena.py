from .ships import Fighter

import numpy as np
import matplotlib.pyplot as plt


class Arena(object):
    def __init__(self, m, n, layers=3):
        self.arena = np.empty((m, n, layers) if layers > 1 else (m, n), dtype=object)
        self.ships = []

    def __str__(self):
        return str(self.arena)

    def show(self):
        plt.figure()
        plt.imshow(self.arena)
        plt.show()

    def register_ship(self, coords, shipinstance):
        shipinstance.coords = coords
        self.arena[coords] = shipinstance
        self.ships.append(shipinstance)
