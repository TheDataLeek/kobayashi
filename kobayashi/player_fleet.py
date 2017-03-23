from kobayashi.ships import Cruiser
from kobayashi.ships import
from kobayashi.weapons import *

def phoenix():
    ship = Cruiser()
    ship.register_weapon(SpinalBeamCannon())
    ship.register_weapon(FlakEmitterBattery())
    ship.register_weapon(ChargedParticleCaster())
    ship.register_weapon(Gravcannon())
