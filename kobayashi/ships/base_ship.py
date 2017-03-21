from ..util import distance, FullCrewException

import abc
import random


class Ship(metaclass=abc.ABCMeta):
    def __init__(self, hp=10, speed=0, armor=0, crew_min=1, crew_max=1, armor_class=9, max_power=5, max_mass=2, max_hardpoints=1, ship_class=0, team=1, level=None, coords=None):
        self.team = team
        self.AI_level = 0 if level is None else level
        self.coords = coords
        self.weapons = []
        self.speed = speed
        self.crew = {}
        self.hp = hp
        self.armor = armor
        self.crew_min = crew_min
        self.crew_max = crew_max
        self.armor_class = armor_class
        self.max_power = max_power
        self.max_mass = max_mass
        self.max_hardpoints = max_hardpoints
        self.ship_class = ship_class

    def __int__(self):
        return self.team

    def remove(self, arena):
        arena.arena[self.coords] = None
        arena.ships.remove(self)

    def threat_level(self, ship):
        if ship.team == self.team:
            return 0
        return 1 / distance(self.coords, ship.coords)

    def attack(self, arena):
        close_ships, num_within_range = self.list_close_ships(arena)
        if num_within_range == 0:
            return False
        for s, d, w, inrange, threat in close_ships:
            if inrange and s.team != self.team:
                # fire at ship
                old = s.hp
                s.hp -= w.wdamage
                print(f'{s.team} ship damaged by {old - s.hp}')
                if s.hp <= 0:
                    print(f'{s.team} ship destroyed')
                    s.remove(arena)
                return True

    def move(self, arena, new_loc=None):
        if new_loc is not None:
            if distance(self.coords, new_loc) > self.speed:
                return False
            else:
                arena.arena[self.coords] = None
                self.coords = new_loc
                arena.arena[self.coords] = self
                return True

        arena.arena[self.coords] = None
        if self.AI_level == 0:
            self.coords = self.random_jitter(arena.arena.shape)
        arena.arena[self.coords] = self

    def random_jitter(self, shape):
        return tuple(min(max(_ + random.randint(-1, 1), 0), shape[i] - 1)
                            for i, _ in enumerate(self.coords))

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

    def tick(self, arena):
        self.move(arena)
        self.attack(arena)

    def register_crewmember(self, person, role):
        if role in self.crew:
            self.crew[role] = person
        else:
            if len(self.crew) < self.capacity:
                self.crew[role] = person
            else:
                raise FullCrewException(f'Capacity is at {self.capacity}.')

    @abc.abstractmethod
    def register_weapon(self, weapon):
        pass

    @abc.abstractproperty
    def capacity(self):
        pass
