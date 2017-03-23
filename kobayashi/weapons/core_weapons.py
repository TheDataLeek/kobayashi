from .base_weapon import Weapon
from ..util import dice


class MultifocalLaser(Weapon):

    armor_pen = 20
    power = 5

    @property
    def wdamage(self):
        return dice(1, 4)

class ReaperBattery(Weapon):

    clumsy = True
    power = 4

    @property
    def wdamage(self):
        return dice(3, 4)

class FractalImpactCharges(Weapon):

    armor_pen = 15
    ammo = 4
    power = 5

    @property
    def wdamage(self):
        return dice(2, 6)

class PolyspectralMESBeam(Weapon):

    armor_pen = 25
    weap_phase = 1
    power = 5

    @property
    def wdamage(self):
        return dice(2, 4)

class Sandthrower(Weapon):

    flak = True
    power = 3

    @property
    def wdamage(self):
        return dice(2, 4)

class FlakEmitterBattery (Weapon):

    armor_pen = 10
    flak = True
    power = 5
    free_mass = 3
    min_class = 1

    @property
    def wdamage(self):
        return dice(2, 6)

class TorpedoLauncher (Weapon):

     armor_pen = 20
     ammo = 4
     power = 10
     free_mass = 3
     min_class = 1

     @property
     def wdamage(self):
         return dice(3, 8)

class ChargedParticleCaster (Weapon):

    armor_pen = 15
    clumsy = True
    power = 10
    hardpoints = 2
    min_class = 1

    @property
    def wdamage(self):
        return dice(3, 6)

class PlasmaBeam (Weapon):

    armor_pen = 10
    power = 5
    free_mass = 2
    hardpoints = 2
    min_class = 1

    @property
    def wdamage(self):
        return dice(3, 6)

class MagSpikeArray (Weapon):

    flak = True
    weap_phase = 1
    ammo = 10
    power = 5
    free_mass = 2
    hardpoints = 2
    min_class = 1

    @property
    def wdamage(self):
        return dice(2, 6) + 2

class SpinalBeamCannon (Weapon):

    armor_pen = 15
    weap_phase = 1
    clumsy = True
    power = 10
    free_mass = 5
    hardpoints = 3
    min_class = 2

    @property
    def wdamage(self):
        return dice(3, 10)

class SmartCloud (Weapon):

    cloud = True
    clumsy = True
    power = 10
    free_mass = 5
    hardpoints = 2
    min_class = 2

    @property
    def wdamage(self):
        return dice(3, 10)

class Gravcannon (Weapon):

    armor_pen = 20
    power = 15
    free_mass = 4
    hardpoints = 3
    min_class = 2

    @property
    def wdamage(self):
        return dice(4, 6)

class SpikeInversionProjector (Weapon):

    armor_pen = 15
    weap_phase = 2
    power = 10
    free_mass = 3
    hardpoints = 3
    min_class = 2

    @property
    def wdamage(self):
        return dice(3, 8)

class VortexTunnelInductor (Weapon):

    armor_pen = 20
    weap_phase = 1
    clumsy = True
    power = 20
    free_mass = 10
    hardpoints = 4
    min_class = 3

    @property
    def wdamage(self):
        return dice(3, 20)

class MassCannon (Weapon):

    armor_pen = 20
    weap_phase = 3
    ammo = 4
    power = 10
    free_mass = 5
    hardpoints = 4
    min_class = 3

    @property
    def wdamage(self):
        return dice(2, 20)

class LightningChargeMantle (Weapon):

    armor_pen = 5
    cloud = True
    power = 15
    free_mass = 5
    hardpoints = 2
    min_class = 3

    @property
    def wdamage(self):
        return dice(1, 20)

class SingularityGun (Weapon):

    armor_pen = 20
    weap_phase = 6
    power = 25
    free_mass = 10
    hardpoints = 5
    min_class = 3

    @property
    def wdamage(self):
        return dice(5, 20)