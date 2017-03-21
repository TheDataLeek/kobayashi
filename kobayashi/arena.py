from .ships import Fighter

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Arena(object):
    def __init__(self, m, n, layers=3):
        self.m = m
        self.n = n
        self.layers = layers
        self.arena = {}
        self.arena = np.empty((m, n, layers), dtype=object)
        self.ships = []
        self.framenum = 0

    def __str__(self):
        return str(self.arena)

    def register_ship(self, coords, shipinstance):
        shipinstance.coords = coords
        self.arena[coords] = shipinstance
        self.ships.append(shipinstance)

    def tick(self):
        self.framenum += 1
        for s in self.ships:
            s.tick(self)

    def show(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(np.linspace(-10, self.m + 10, 30), np.linspace(-10, self.n + 10, 30))
        ax.plot_wireframe(X, Y, 0, alpha=0.2)
        xs, ys, zs = np.nonzero(self.arena)
        colors = [self.arena[x, y, z].team for x, y, z in zip(xs, ys, zs)]
        ax.scatter(*np.nonzero(self.arena), c=colors)

        ax.set_xlim(-10, self.m + 10)
        ax.set_ylim(-10, self.n + 10)
        ax.set_zlim(0, self.layers + 1)

        # plt.savefig(f'./img/arena{self.framenum}.png')
