from ..util import distance

import abc


class Ship(metaclass=abc.ABCMeta):
    def __init__(self, speed=10, team=None, level=None, coords=None):
        self.team = team
        self.AI_level = 0 if level is None else level
        self.coords = coords
        self.weapons = []
        self.speed = speed
        self.crew = {}

    def __int__(self):
        return self.coords[-1]

    def register_crewmember(self, person, role):
        self.crew[role] = person

    def threat_level(self, ship):
        return 1 / distance(self.coords, ship.coords)

    def attack(self, arena):
        close_ships, num_within_range = self.list_close_ships(arena)
        if num_within_range == 0:
            return False
        for s, d, w, inrange, threat in close_ships:
            if inrange:
                return True

    def list_close_ships(self, arena):
        """
        Returns a list of all ships sorted by threat level descending that are within range
        """
        ships = []
        for ship in arena.ships:
            d = distance(self.coords, ship.coords)
            for w in self.weapons:
                ships.append((ship, d, w, d < w.wrange, self.threat_level(ship)))
        return sorted(ships, key=lambda tup: -tup[-1]), sum([t[3] for t in ships])
