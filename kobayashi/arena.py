from .ships import Fighter

import sys
import os
from tqdm import tqdm
import inspect
import numpy as np

try:
    import matplotlib
    # matplotlib.rcParams['backend'] = "Qt5Agg"
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
except ImportError as e:
    print(f'Visualization unavailable: {e}')


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

    def help(self, object=None):
        if object is not None:
            return {k: type(v) for k, v in inspect.getmembers(object) if not k.startswith('_')}
        return {k: type(v) for k, v in inspect.getmembers(self) if not k.startswith('_')}

    def update_fleet_attr(self, team, key, value):
        for ship in self.ships:
            if ((ship.team == team) and (not ship.destroyed)):
                ship.key = value

    def send_fleet_command(self, team, command, args, kwargs):
        for ship in self.ships:
            if ((ship.team == team) and (not ship.destroyed) and (ship.ticked is False)):
                getattr(ship, command)(*args, **kwargs)

    def get_fleet(self, team):
        return [s for s in self.ships if s.team == team]

    def num_ships_left(self):
        shipcount = {}
        for ship in self.ships:
            if not ship.destroyed:
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
            print(f'{ship.name}({ship.team} {ship.__class__.__name__}) @ {ship.coords}. {ship.hp}hp')

    def tick(self):
        self.framenum += 1
        for ship in self.ships:
            if ship.destroyed is False:
                ship.tick(self)
        self.show(save=True)

    def tickn(self, n):
        for _ in tqdm(range(n)):
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
        ax.scatter(*np.array(points).T, c=colors, alpha=0.5, s=sizes, cmap=plt.get_cmap('tab10'))

        # ax.set_xlim(-1, 30)
        # ax.set_ylim(-1, 30)
        # ax.set_zlim(0, 30)

        # plt.axis('off')

        if save:
            if not os.path.isdir('img'):
                os.mkdir('img')
            plt.savefig(f'img/arena{self.framenum}.png')
        else:
            plt.show()

        return None
