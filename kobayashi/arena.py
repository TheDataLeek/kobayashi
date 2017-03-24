from .ships import Fighter

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Arena(object):
    def __init__(self):
        self.arena = {}
        self.framenum = 0
        self.ships = []

    def __str__(self):
        return str(self.arena)

    def __getitem__(self, key):
        return self.arena.get(key)

    def __setitem__(self, key, value):
        if value is None:
            self.arena.pop(key)
        else:
            self.arena[key] = value

    def register_ship(self, coords, shipinstance):
        shipinstance.coords = coords
        self.arena[coords] = shipinstance
        self.ships.append(shipinstance)

    def tick(self):
        self.framenum += 1
        for ship in self.ships:
            if ship.destroyed is False:
                ship.tick(self)

    def show(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(np.linspace(-1, 30, 30), np.linspace(-1, 30, 30))
        ax.plot_wireframe(X, Y, 0, alpha=0.2)

        points = []
        colors = []
        for ship in self.ships:
            if not ship.destroyed:
                points.append(ship.coords)
                colors.append(ship.team)
        ax.scatter(*np.array(points).T, c=colors)

        ax.set_xlim(-1, 30)
        ax.set_ylim(-1, 30)
        ax.set_zlim(0, 30)

        plt.savefig(f'./img/arena{self.framenum}.png')
