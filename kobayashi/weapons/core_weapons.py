from .base_weapon import Weapon, check_ammo
from ..util import dice


class MultifocalLaser(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=20,
            power=5
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(1, 4)


class ReaperBattery(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            clumsy=True,
            power=4
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(3, 4)


class FractalImpactCharges(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=15,
            ammo=4,
            power=5,
            to_hit_mod=11
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(2, 6) + 3


class PolyspectralMESBeam(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=25,
            weap_phase=1,
            power=5
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(2, 4)


class Sandthrower(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            flak=True,
            power=3
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(2, 4)


class FlakEmitterBattery(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=10,
            flak=True,
            power=5,
            free_mass=3,
            min_class=1
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(2, 6)


class TorpedoLauncher(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=20,
            ammo=4,
            power=10,
            free_mass=3,
            min_class=1
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(3, 8)


class ChargedParticleCaster(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=15,
            clumsy=True,
            power=10,
            hardpoints=2,
            min_class=1
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(3, 6)


class PlasmaBeam(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=10,
            power=5,
            free_mass=2,
            hardpoints=2,
            to_hit_mod=8,
            min_class=1
        )
        self.__dict__ = {**self.__dict__, **kwargs}

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(3, 6) + 3


class MagSpikeArray(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            flak=True,
            weap_phase=1,
            ammo=10,
            power=5,
            free_mass=2,
            hardpoints=2,
            min_class=1
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(2, 6) + 2


class SpinalBeamCannon(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=15,
            weap_phase=1,
            clumsy=True,
            power=10,
            free_mass=5,
            hardpoints=3,
            min_class=2
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(3, 10)


class SmartCloud(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            cloud=True,
            clumsy=True,
            power=10,
            free_mass=5,
            hardpoints=2,
            min_class=2,
            to_hit_mod=8
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(3, 10) + 3


class Gravcannon(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=20,
            power=15,
            free_mass=4,
            hardpoints=3,
            min_class=2,
            to_hit_mod=8
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(4, 6) + 3


class SpikeInversionProjector(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=15,
            weap_phase=2,
            power=10,
            free_mass=3,
            hardpoints=3,
            min_class=2,
            to_hit_mod=1
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(3, 8) + 3


class VortexTunnelInductor(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=20,
            weap_phase=1,
            clumsy=True,
            power=20,
            free_mass=10,
            hardpoints=4,
            min_class=3
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(3, 20)


class MassCannon(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=20,
            weap_phase=3,
            ammo=4,
            power=10,
            free_mass=5,
            hardpoints=4,
            min_class=3
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(2, 20)


class LightningChargeMantle(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=5,
            cloud=True,
            power=15,
            free_mass=5,
            hardpoints=2,
            min_class=3,
            to_hit_mod=5
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(1, 20) + 3


class SingularityGun(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(
            armor_pen=20,
            weap_phase=6,
            power=25,
            free_mass=10,
            hardpoints=5,
            min_class=3,
            to_hit_mod=5
        )

    @property
    @check_ammo
    def wdamage(self, *args, **kwargs):
        return dice(5, 20) + 3
