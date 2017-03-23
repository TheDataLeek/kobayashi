import abc
import math
from ..util import dice


class Weapon(metaclass=abc.ABCMeta)

    # Weapon combat properties
    ammo = math.inf
    armor_pen = 0
    cloud = False
    clumsy = False
    flak = False
    weap_phase = 0

    # Weapon to ship compatibility properties
    # Ship class is defined as:
    # 0 - Fighter
    # 1 - Frigate
    # 2 - Cruiser
    # 3 - Capital
    # 4 - Super Capital
    # 5 - Bruxelles
    power = 1
    free_mass = 1
    hardpoints = 1
    min_class = 0
    notes = None

    @abc.abstractproperty
    def wdamage(self):
        pass

    @abc.abstractproperty
    def wrange(self):
        pass
