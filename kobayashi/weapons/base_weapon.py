import abc
import math
from ..util import dice


class Weapon(metaclass=abc.ABCMeta):
    def __init__(self, **kwargs):
        # Weapon combat properties
        self.ammo = math.inf
        self.armor_pen = 0
        self.cloud = False
        self.clumsy = False
        self.flak = False
        self.weap_phase = 0

        # Weapon to ship compatibility properties
        # Ship class is defined as:
        # 0 - Fighter
        # 1 - Frigate
        # 2 - Cruiser
        # 3 - Capital
        # 4 - Super Capital
        # 5 - Bruxelles
        self.power = 1
        self.free_mass = 1
        self.hardpoints = 1
        self.min_class = 0
        self.notes = None
        self.wrange = 10

        self.__dict__ = {**self.__dict__, **kwargs}

    @abc.abstractproperty
    def wdamage(self):
        pass
