from .base_weapon import Weapon, check_ammo
from ..util import dice


class ImplosionFieldProjector(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            to_hit_mod=10,
            armor_pen=25,
            weap_phase=2
        )
        self.__dict__ = {**self.__dict__, **kwargs}

    @property
    @check_ammo
    def wdamage(self):
        return dice(4, 20) + 2


class RandrodWarpLineGun(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            to_hit_mod=10,
            armor_pen=25
        )
        self.__dict__ = {**self.__dict__, **kwargs}

    @property
    @check_ammo
    def wdamage(self):
        return dice(2, 20) + 42
'''
class AntaeusSiegeMissiles(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
        to_hit_mod=,
        armor_pen=??
        )
        self.__dict__={**self.__dict__, **kwargs}
        @property
        @check_ammo
        def wdamage(self):
            return dice(???)
'''
