import random

import pytest

from .. import ships
from .. import generate
from .. import weapons


@pytest.fixture
def default_ship():
    return ships.Ship()

def test_init(default_ship):
    assert default_ship.AC == 10
    assert default_ship.ticked == False

def test_int_repr(default_ship):
    assert int(default_ship) == default_ship.team

@pytest.fixture
def fighter():
    ship = ships.Fighter(
        hp=16,
        crew_max=6,
        speed=6,
        armor=8,
        AC=3,
        spike=1
    )
    ship.register_pilot(generate.generate_pilot(random.randint(1, 5)))
    ship.register_gunner(generate.generate_gunner(random.randint(1, 5)))
    ship.register_gunner(generate.generate_gunner(random.randint(1, 5)))
    ship.register_weapon(weapons.FractalImpactCharges())

    ship.register_AI(1)
    return ship

def test_crew_size(fighter):
    assert fighter.crew_size == 3

def test_ai(fighter):
    assert fighter.AI.__class__.__name__ == 'Level1'

def test_best_gunner(fighter):
    for gunner in fighter.gunners:
        assert fighter.best_gunner.skillmod >= gunner.skillmod
