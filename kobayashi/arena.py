from .ships import Fighter

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Arena(object):
    def __init__(self, m, n, layers=3):
        self.m = m
        self.n = n
        self.layers = layers
        self.arena = np.empty((m, n, layers), dtype=object)
        self.ships = []

    def __str__(self):
        return str(self.arena)

    def show(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        xs = np.arange(0, self.m)
        ys = np.arange(0, self.n)
        X, Y = np.meshgrid(np.linspace(-10, self.m + 10, 30), np.linspace(-10, self.n + 10, 30))
        ax.plot_wireframe(X, Y, 0, alpha=0.2)
        for i in range(self.m):
            for j in range(self.n):
                for k in range(self.layers):
                    if self.arena[i, j, k] is not None:
                        ax.scatter(xs[i], ys[j], int(self.arena[i, j, k]))
                        ax.plot([xs[i], xs[i]],
                                [ys[j], ys[j]],
                                [int(self.arena[i, j, k]), 0],
                                c='red', alpha=0.2)
        plt.savefig('arena.png')

    def register_ship(self, coords, shipinstance):
        shipinstance.coords = coords
        self.arena[coords] = shipinstance
        self.ships.append(shipinstance)
