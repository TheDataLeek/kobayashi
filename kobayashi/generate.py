from .crew import Pilot, Gunner
from .weapons import MultifocalLaser
from .util import dice

from .ships import Fighter, Carrier, Battleship, Cruiser, Frigate

import random


def generate_fleet(arena, size=10, center=(0,0,0), team=1):
    """
    Basic theory is that regardless of size of fleet, perc of ships stays same.
    """
    num_capital = int(size * 0.05)
    num_cruiser = int(size * 0.1)
    num_frigate = int(size * 0.1)
    num_fighters = int(size * 0.75)

    ships = []
    for _ in range(num_capital):
        ship = generate_ship(random.choice([Carrier, Battleship]), team)
        ships.append(ship)

    for _ in range(num_cruiser):
        ship = generate_ship(Cruiser, team)
        ships.append(ship)

    for _ in range(num_frigate):
        ship = generate_ship(Frigate, team)
        ships.append(ship)

    for _ in range(num_fighters):
        ship = generate_ship(Fighter, team)
        ships.append(ship)

    position_ships(arena, ships, center)


def position_ships(arena, ships, center):
    for ship in ships:
        coord = center
        while True:
            if arena[coord] is None:
                break
            else:
                coord = tuple(c + random.randint(-1, 1)
                              for c in coord)
        ship.coords = coord
        arena[coord] = ship
        arena.ships.append(ship)


def generate_ship(shiptype, team):
    # New ship instance
    ship = shiptype()
    # Set crew
    pilot = generate_pilot(ship.ship_class + random.randint(1, 3))
    ship.register_pilot(pilot)
    for i in range(ship.crew_max - 1):
        gunner = generate_gunner(ship.ship_class + random.randint(1, 3))
        ship.register_gunner(gunner)
    # Set team
    ship.team = team
    # Get weapons
    ship.register_weapon(MultifocalLaser())
    # Register AI level
    ship.register_AI(1)

    return ship


def generate_crew(count):
    pilot = generate_pilot()
    if count == 1:
        return


def generate_pilot(level):
    dx_mod = random.randint(-2, 2)
    skill_level = min(random.randint(0, 10), int(level / 2))
    return Pilot(level, dx_mod + skill_level)

def generate_gunner(level):
    dx_mod = random.randint(-2, 2)
    skill_level = min(random.randint(0, 10), int(level / 2))
    ab = random.randint(0, 5)  # TODO
    return Gunner(level, dx_mod + skill_level + ab)
