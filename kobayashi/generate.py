from .crew import Pilot
from .weapons import MultifocalLaser
from .util import dice

import random


def generate_fleet(size=10):
    pass


def generate_ship(shiptype):
    ship = shiptype()
    ship.register_crewmember(generate_pilot(), 'pilot')
    ship.team = random.randint(1, 3)
    ship.register_weapon(MultifocalLaser())
    ship.register_AI(1)
    return ship


def generate_crew(count):
    pilot = generate_pilot()
    if count == 1:
        return


def generate_pilot():
    attributes = [dice(4, 6, droplowcount=1) for _ in range(6)]
    level = random.randint(1, 5)
    return Pilot('expert', level, attributes)
