import abc
import math
from ..util import dice
from ..exceptions import OutOfAmmo

import wrapt


@wrapt.decorator
def check_ammo(wrapped, instance, args, kwargs):
    cls = args[0]
    if cls.ammo > 0:
        cls.ammo -= 1
        return wrapped(*args, **kwargs)
    else:
        raise OutOfAmmo


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
        self.wrange = 1

        self.to_hit_mod = 0

        self.extra_dmg = 0

        self.__dict__ = {**self.__dict__, **kwargs}

    @abc.abstractproperty
    def wdamage(self):
        pass
