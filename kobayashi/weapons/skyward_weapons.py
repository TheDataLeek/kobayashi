import math
from .base_weapon import Weapon
from ..util import dice

class BrakerGunArray (Weapon):
    notes = ('This weapon is intended for use on planet-side installations. The range is too short to use in ship to ' \
            'ship combat but can target and redirect projectiles back into space. This array can handle a large number ' \
            'of incoming projectiles at once and as such, can be used to defend against almost any short duration ' \
            'orbital bombardment. This can protect an entire hemisphere if need be.')

class JitterBeamProjector (Weapon):

     armor_pen = 15
     weap_phase = 3
     power = 15
     free_mass = 5
     hardpoints = 2
     min_class = 2

     @property
     def wdamage(self):
         return dice(3, 8)

class PhotonicSiegeCannon (Weapon):

    armor_pen = 20
    power = 40
    free_mass = 20
    hardpoints = 10
    min_class = 2
    notes = 'This weapon can only be used against stationary targets'

    @property
    def wdamage(self):
        return dice(6, 10)

class SunshineField (Weapon):

    armor_pen = 10
    weap_phase = 2
    cloud = True
    power = 15
    free_mass = 10
    hardpoints = 2
    min_class = 2

    @property
    def wdamage(self):
        return dice(2, 6)

class UmbrellaBarrageSystem (Weapon):

    ammo = 2
    power = 20
    free_mass = 10
    hardpoints = 4
    min_class = 2
    notes = ('This weapon is designed to hit large numbers of small ships - such as Cargo Lighters or Drop Pods. A '
             'single attack roll is made against each craft. When fired against mass drops, like those from a'
             'Thunderhead grav pod system, a single shot will destroy 1d4 x 15% of all of the pods or lighters '
             'attempting to land that round.'

    @property
    def wdamage(self):
        return dice(1, 4)

class DevourerLauncher (Weapon):

    ammo = 5
    armor_pen = 10
    power = 10
    free_mass = 5
    hardpoints = 3
    notes = ('On a hit, the affected ship takes 1d10 + 5 damage at the beginning of each round. This damage continues ' \
            'until the ship mounting the Launcher is destroyed or disengages from combat. Armor and AP apply as normal. ' \
            'For example, after 3 successful hits the target takes 3d10 + 15 damage at the beginning of the round.')