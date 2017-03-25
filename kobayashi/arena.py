from .ships import Fighter

import os
import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = "Qt5Agg"
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
        if isinstance(key, list):
            key = tuple(key)
        return self.arena.get(key)

    def __setitem__(self, key, value):
        if isinstance(key, list):
            key = tuple(key)
        if value is None:
            self.arena.pop(key)
        else:
            self.arena[key] = value

    def num_ships_left(self):
        shipcount = {}
        for ship in self.ships:
            try:
                shipcount[ship.team] += 1
            except KeyError:
                shipcount[ship.team] = 1
        return shipcount

    def ship_by_name(self, key):
        for ship in self.ships:
            if ship.name == key:
                return ship
        return None

    def register_ship(self, coords, shipinstance):
        shipinstance.coords = coords
        self.arena[coords] = shipinstance
        self.ships.append(shipinstance)

    def list_ships(self):
        for ship in self.ships:
            print(ship.team, ship.coords)

    def tick(self):
        self.framenum += 1
        for ship in self.ships:
            if ship.destroyed is False:
                ship.tick(self)

    def tickn(self, n):
        for _ in range(n):
            self.tick()

    def show(self, save=False):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')

        points = []
        colors = []
        sizes = []
        for ship in self.ships:
            if not ship.destroyed:
                points.append(ship.coords)
                colors.append(ship.team)
                sizes.append((ship.ship_class + 1) * 100)
        ax.scatter(*np.array(points).T, c=colors, alpha=0.5, s=sizes)

        # ax.set_xlim(-1, 30)
        # ax.set_ylim(-1, 30)
        # ax.set_zlim(0, 30)

        if save:
            plt.savefig(f'./img/arena{self.framenum}.png')
        else:
            plt.show()

        return None
