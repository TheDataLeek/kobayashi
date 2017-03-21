from .base_weapon import Weapon
from ..util import dice


class PhotonBeam(Weapon):
    @property
    def wdamage(self):
        return dice(2, 6)

    @property
    def wrange(self):
        return 5


class PhotonCannon(Weapon):
    @property
    def wdamage(self):
        return dice(10, 10)

    @property
    def wrange(self):
        return 2
