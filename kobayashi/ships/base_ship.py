from ..util import distance, dice
from ..exceptions import *
from .ship_ai import Level1

import abc
import random
import math
import string


class Ship(metaclass=abc.ABCMeta):
    def __init__(self, **kwargs):
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

        # overwrite with anything passed
        self.__dict__ = {**self.__dict__, **kwargs}

    def __int__(self):
        return self.team

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

    def attack(self, arena):
        close_ships, num_within_range = self.list_close_ships(arena)
        if num_within_range == 0:
            raise NoTargetsAvailable(f'{self.name} has no targets')
        if len(close_ships) > 0:
            ship, distance, weapon, threat = close_ships[0]
            ship.hp -= weapon.wdamage
            if ship.hp <= 0:
                ship.remove(arena)

    def move_towards(self, arena, coords):
        if distance(self.coords, coords) <= self.speed:
            self._move(arena, coords)
        else:
            d = distance(self.coords, coords)
            new_loc = tuple(self.coords[i] + int(self.speed *
                                ((coords[i] - self.coords[i]) / d))
                            for i in range(len(coords)))
            self._move(arena, new_loc)

    def move(self, arena, new_loc=None):
        # If given directions, try to move there
        if new_loc is not None:
            for coord in arena:
                if coord == new_loc: #This means a collision will occur since there is already a shipinstance at the new location
                    i = 0
                    reductionFactor = 1
                    pos = 0
                    collisionFlag = 0
                    while(collisionFlag != 1):
                        if reductionFactor > self.speed:
                            collisionFlag = 1 #Setting this is not required since we are breaking out of the loop but I have it here anyway for clarity
                            print("CANNOT MOVE!")
                            new_loc = self.loc #cannot move so the shipinstance will remain at same position
                            break
                        for pos in range(0,7):
                            collisionFlag = 1
                            if pos == 0:
                                x = tuple(reductionFactor * i for i in (1,0,0))
                            elif pos == 1:
                                x = tuple(reductionFactor*i for i in (0,1,0))
                            elif pos == 2:
                                x = tuple(reductionFactor*i for i in (0,0,1))
                            elif pos == 3:
                                x = tuple(reductionFactor*i for i in (1,1,0))
                            elif pos == 4:
                                x = tuple(reductionFactor*i for i in (1,0,1))
                            elif pos == 5:
                                x = tuple(reductionFactor*i for i in (0,1,1))
                            elif pos == 6:
                                x = tuple(reductionFactor*i for i in (1,1,1))
                            tempLoc = tuple(map(operator.sub, new_loc, x))
                            if(distance(new_loc, tempLoc) > self.speed):
                                collisionFlag == 1
                                print("Cannot move!")
                                break
                            for coord in listofCoords:
                                print("Entering comparison loop")
                                if tempLoc == coord:
                                    collisionFlag = 0
                                    print("Collision detected at {}".format(tempLoc))
                                    break #if collision was detected, no point in comparion against other coordinates.
                            if(collisionFlag):
                                print("No Collision Detected at {}".format(tempLoc))
                                new_loc = tempLoc #Since no collision was detected at this location, we can move this shipinstance here instead.
                                break #If no collision was detected, again no need to shift x and check other points.
                        reductionFactor += 1
            arena[self.coords] = None
            self.coords = new_loc
            arena[self.coords] = self
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
        if arena[loc] is not None:
            raise ArenaCoordinateOccupied(f'Refusing to move {self.name}. {loc} occupied')
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

    def list_ships(self, arena):
        ships = []
        for coord, ship in arena.arena.items():
            if ((ship.ship_class >= self.ship_class) and  #only target >= ship classes
                    (ship.team != self.team)):
                d = distance(self.coords, ship.coords)
                ships.append((ship, d, self.threat_level(ship)))
        ships = sorted(ships, key=lambda tup: (tup[0].ship_class, -tup[-1]))
        return ships

    def list_close_ships(self, arena):
        """
        Returns a list of all ships sorted by threat level descending that are within range
        """
        ships = []
        for coord, ship in arena.arena.items():
            if ((ship.ship_class >= self.ship_class) and  #only target >= ship classes
                    (ship.team != self.team)):
                d = distance(self.coords, ship.coords)
                for w in self.weapons:
                    if d < w.wrange:
                        ships.append((ship, d, w, self.threat_level(ship)))
        ships = sorted(ships, key=lambda tup: (tup[0].ship_class, -tup[-1]))
        num_within_range = len(ships)
        return ships, num_within_range

    def tick(self, arena):
        self.move(arena)
        try:
            self.attack(arena)
        except NoTargetsAvailable:
            pass

    def register_pilot(self, person):
        if self.crew_size < self.crew_max:
            self.pilot = person
        else:
            raise FullCrewException(f'{self.name} capacity is at {self.capacity}.')

    def register_gunner(self, person):
        if self.crew_size < self.crew_max:
            self.gunners.append(person)
        else:
            raise FullCrewException(f'{self.name} capacity is at {self.capacity}.')

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
                    'Refusing to add weapon to {self.name} '
                    f'({new_mass}/{self.max_mass})m '
                    f'({new_power}/{self.max_power})p '
                    f'({new_hardpoints}/{self.max_hardpoints})h')
