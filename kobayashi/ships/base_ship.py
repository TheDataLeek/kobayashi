from ..util import distance, dice, all_neighbor_points
from ..exceptions import *
from .ship_ai import Level1

import abc
import random
import math
import string
import itertools
import heapq


class Ship(metaclass=abc.ABCMeta):
    def __init__(self, *args, **kwargs):
        self.player_ship = False
        self.name = ''.join(random.choice(string.ascii_lowercase)
                            for _ in range(10))
        self.destroyed = False
        self.team = 1
        self.AI = None
        self.coords = (0, 0, 0)
        self.weapons = []
        self.speed = 0
        self.pilot = None
        self.gunners = []
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
        self.AC = 10
        self.spike = 1
        self.phase = 0

        # overwrite with anything passed
        self.__dict__ = {**self.__dict__, **kwargs}

    def __int__(self):
        return self.team

    def __str__(self):
        return str(self.__dict__)

    @property
    def crew_size(self):
        return len(self.gunners) + (1 if self.pilot is not None else 0)

    def register_AI(self, level):
        if level == 0:
            self.AI = None
        if level == 1:
            self.AI = Level1(self)

    def remove(self, arena):
        arena[self.coords] = None
        self.destroyed = True

    def threat_level(self, ship):
        if ship.team == self.team:
            return 0
        return 1 / distance(self.coords, ship.coords)

    @property
    def best_gunner(self):
        best_gunners = sorted(self.gunners, key=lambda g: -g.skillmod)
        if len(best_gunners) == 0:
            return None
        return best_gunners[0]

    def attack(self, arena):
        for weapon in self.weapons:
            close_ships = self.list_ships(arena, d=weapon.wrange)
            for ship, d, t in close_ships:
                self.attack_ship(weapon, ship, arena)
                break

    def attack_ship(self, weapon, ship, arena):
        gunner = self.best_gunner
        if gunner is None:
            return
        phase_check = (self.phase == ship.phase) or (dice(1, 6) > (self.phase - ship.phase))
        to_hit_check = (dice(1, 20) + gunner.skillmod + weapon.to_hit_mod + ship.AC - ship.pilot.skillmod > 20)
        if phase_check and to_hit_check:
            DR_dmg = min(0, ship.armor - weapon.wdamage)
            if DR_dmg < 0:
                print(f'{self.name} attacked {ship.name} for {-DR_dmg}')
                ship.hp += DR_dmg
                if ship.hp <= 0:
                    print(f'{ship.name} was destroyed')
                    ship.remove(arena)


    def move_towards(self, arena, coords):
        if distance(self.coords, coords) <= self.speed:
            self._move(arena, coords)
        else:
            # TODO make sure we move close to full distance as possible
            # This method currently cuts > 1 full move on average
            d = distance(self.coords, coords)
            new_loc = tuple(self.coords[i] + int(self.speed *
                                ((coords[i] - self.coords[i]) / d))
                            for i in range(len(coords)))
            self._move(arena, new_loc)

    def move(self, arena, new_loc=None):
        self.phase = random.randint(0, self.spike)
        # If given directions, try to move there
        if new_loc is not None:
            if distance(self.coords, new_loc) > self.speed:
                raise NotEnoughSpeed(f'Not enough speed for {self.name}. {distance(self.coords, new_loc)} > {self.speed}')
            else:
                self._move(arena, new_loc)
        # Otherwise use AI
        elif self.command_ship is None and self.AI is not None:
            self.AI.move(arena)

        for ship in self.subordinates:
            ship.move()

    def _move(self, arena, loc):
        """ Not guaranteed to move full speed!! """
        if loc in arena.arena:  # check for collision
            pqueue = []
            visited = [loc]

            neighbors = all_neighbor_points(loc)

            for n in neighbors:
                heapq.heappush(pqueue, (-distance(self.coords, n), n))

            while True:
                try:
                    d, new_loc = heapq.heappop(pqueue)
                except IndexError:
                    loc = self.coords
                    break

                if new_loc in arena.arena:
                    visited.append(new_loc)
                    new_loc_neighbors = [t for t in all_neighbor_points(new_loc)
                                         if t not in visited]
                    for n in new_loc_neighbors:
                        heapq.heappush(pqueue, (-distance(self.coords, n), n))
                else:
                    loc = new_loc
                    break

        if arena[loc] is not None:
            raise ArenaCoordinateOccupied(f'Refusing to move {self.name}. {loc} occupied')
        print(f'{self.name} moved {self.coords} -> {loc}')
        arena[self.coords] = None
        self.coords = loc
        arena[self.coords] = self

    def random_jitter(self):
        return tuple(_ + random.randint(-1, 1)
                     for i, _ in enumerate(self.coords))

    def within_range(self, ship):
        for w in self.weapons:
            if distance(self.coords, ship.coords) <= w.wrange:
                return True
        return False

    def list_ships(self, arena, d=math.inf):
        ships = []
        for coord, ship in arena.arena.items():
            if ((ship.ship_class >= self.ship_class) and  #only target >= ship classes
                    (ship.team != self.team)):
                new_d = distance(self.coords, ship.coords)
                if new_d <= d:
                    ships.append((ship, new_d, self.threat_level(ship)))
        ships = sorted(ships, key=lambda tup: (tup[0].ship_class, -tup[-1]))
        return ships

    def tick(self, arena):
        if self.player_ship is not True:
            self.move(arena)
            try:
                self.attack(arena)
            except NoTargetsAvailable:
                pass

    def register_pilot(self, person):
        if self.crew_size < self.crew_max:
            self.pilot = person
        else:
            raise FullCrewException(f'{self.name} capacity is max')

    def register_gunner(self, person):
        if self.crew_size < self.crew_max:
            self.gunners.append(person)
        else:
            raise FullCrewException(f'{self.name} capacity is max')

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
        new_mass = self.current_free_mass - weapon.free_mass
        new_power = self.current_free_power - weapon.power
        new_hardpoints = self.current_free_hardpoints - weapon.hardpoints
        if ((new_mass >= 0) and
            (new_power >= 0) and
            (new_hardpoints >= 0)):
            self.weapons.append(weapon)
        else:
            raise NotEnoughSpacePowerMass(
                    f'Refusing to add weapon to {self.name} '
                    f'({new_mass}/{self.max_mass})m '
                    f'({new_power}/{self.max_power})p '
                    f'({new_hardpoints}/{self.max_hardpoints})h')
