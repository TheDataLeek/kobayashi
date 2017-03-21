from ..util import distance, FullCrewException, NoTargetsAvailable, NotEnoughSpeed

import abc
import random


class Ship(metaclass=abc.ABCMeta):
    def __init__(self, hp=10, speed=10, team=1, level=None, coords=None):
        self.team = team
        self.AI_level = 0 if level is None else level
        self.coords = coords
        self.weapons = []
        self.speed = speed
        self.crew = {}
        self.hp = hp
        self.destroyed = False

    def __int__(self):
        return self.team

    def remove(self, arena):
        arena[self.coords] = None
        self.destroyed = True

    def threat_level(self, ship):
        if ship.team == self.team:
            return 0
        return 1 / distance(self.coords, ship.coords)

    def attack(self, arena):
        close_ships, num_within_range = self.list_close_ships(arena)
        if num_within_range == 0:
            raise NoTargetsAvailable
        for s, d, w, inrange, threat in close_ships:
            if inrange and s.team != self.team:
                s.hp -= w.wdamage
                if s.hp <= 0:
                    s.remove(arena)

    def move_towards(self, arena, coords):
        if distance(self.coords, coords) <= self.speed:
            self.move(arena, new_loc=coords)
        else:
            # TODO: move speed along line
            pass

    def move(self, arena, new_loc=None):
        # If given directions, try to move there
        if new_loc is not None:
            if distance(self.coords, new_loc) > self.speed:
                raise NotEnoughSpeed(f'{distance(self.coords, new_loc)} > {self.speed}')
            else:
                arena[self.coords] = None
                self.coords = new_loc
                arena[self.coords] = self
        # Otherwise use AI
        else:
            arena[self.coords] = None
            if self.AI_level == 0:
                self.coords = self.random_jitter()
            arena[self.coords] = self

    def random_jitter(self):
        return tuple(_ + random.randint(-1, 1)
                     for i, _ in enumerate(self.coords))

    def list_close_ships(self, arena):
        """
        Returns a list of all ships sorted by threat level descending that are within range
        """
        ships = []
        for coord, ship in arena.arena.items():
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

    def register_weapon(self, weapon):
        self.weapons.append(weapon)

    @abc.abstractproperty
    def capacity(self):
        pass
