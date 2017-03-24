from ..util import *

import abc
import random


class Ship(metaclass=abc.ABCMeta):
    def __init__(self, **kwargs):
        self.destroyed = False
        self.team = 1
        self.AI_level = 0
        self.coords = (0, 0, 0)
        self.weapons = []
        self.speed = 0
        self.crew = {}
        self.hp = 10
        self.armor = 0
        self.crew_min = 1
        self.crew_max = 1
        self.armor_class = 9
        self.max_power = 5
        self.max_mass = 2
        self.max_hardpoints = 1
        # Weapon to ship compatibility properties
        # Ship class is defined as:
        # 0 - Fighter
        # 1 - Frigate
        # 2 - Cruiser
        # 3 - Capital
        # 4 - Super Capital
        # 5 - Bruxelles
        self.ship_class = 0
        self.subordinates = []
        self.command_ship = None

        # overwrite with anything passed
        self.__dict__ = {**self.__dict__, **kwargs}

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
            dist = distance(self.coord, coords)
            directionVector = [(self.coord[i]-coords[i])/dist for i in range(len(coords))]
            travelVector = [math.floor(i*self.speed) for i in directionVector]
            self.move(arena, new_loc=travelVector)

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
        # TODO different level of AI
        elif self.command_ship is not None:
            arena[self.coords] = None
            if self.AI_level == 0:
                self.coords = self.random_jitter()
            arena[self.coords] = self

        for ship in self.subordinates:
            ship.move()

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
            if len(self.crew) <= self.crew_max:
                self.crew[role] = person
            else:
                raise FullCrewException(f'Capacity is at {self.capacity}.')

    @property
    def current_free_mass(self):
        return self.max_mass - sum(w.free_mass for w in self.weapons)

    @property
    def current_free_power(self):
        return self.max_power - sum(w.power for w in self.weapons)

    @property
    def current_free_hardpoints(self):
        return self.max_hardpoints - sum(w.hardpoints for w in self.weapons)

    def register_weapon(self, weapon):
        new_mass = self.current_free_mass + weapon.free_mass
        new_power = self.current_free_power + weapon.power
        new_hardpoints = self.current_free_hardpoints + weapon.hardpoints
        if ((new_mass <= self.max_mass) and
            (new_power <= self.max_power) and
            (new_hardpoints <= self.max_hardpoints)):
            self.weapons.append(weapon)
        else:
            raise NotEnoughSpacePowerMass(
                    'Refusing to add weapon '
                    f'({new_mass}/{self.max_mass})m '
                    f'({new_power}/{self.max_power})p '
                    f'({new_hardpoints}/{self.max_hardpoints})h')
