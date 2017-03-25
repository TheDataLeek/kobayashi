import random

from kobayashi.ships import *
from kobayashi.weapons import *
from kobayashi.crew import *
from kobayashi.generate import *


def phoenix():
    ship = Cruiser()
    ship.register_weapon(SpinalBeamCannon())
    ship.register_weapon(FlakEmitterBattery())
    ship.register_weapon(ChargedParticleCaster())
    ship.register_weapon(Gravcannon())


def generate(arena):
    """
    Fleet 1: Yours
    2x Monstrance-class Battleship
    Hit Points: 170 Crew: 100/2,000 Speed: 0 Armor: 23 AC: -1
    Singularity Gun * 2 (+7?/+5? to hit/5d20+3, AP 20, Phase 6), Lighting Charge Mantle (+5? to hit/1d20+3, AP 5, Cloud),
    Spike Inversion Projector (+1? to hit/3d8+3, AP 15, Phase 2)
     Augmented Plating, Hardened Polyceramic Overlay, Ablative Hull Compartments
    Fleet 2: Roberts
    1x Borg Cube (Lemme do tomorrow)
    3x Hasta-class cruiser
    Hit Points: 70 Crew: 50/200 Speed: 2 Armor: 18 AC: 6
    Gravcannon * 2 (+8 to hit/4d6+3, AP 20), Smart Cloud (+8 to hit/3d10+3, Clumsy, Cloud), Plasma Beam (+8 to
    hit/3d6+3, AP 10)
    Hardened Polyceramic Overlay, Grav Eddy Displacer
    Fittings Spike Drive-5
    2x Reproach-class Hunter-Killer frigate
    Hit Points: 45 Crew: 3/60 Speed: 2 Armor: 13 AC: 4
     Torpedo Launchers * 2 (+8 to hit/3d8+3, AP 20, Ammo 4), Plasma Beam (+8 to hit/3d6+3, AP 10)
     Hardened Polyceramic Overlay, Augmented Plating
    Fittings Spike Drive-3
    130x Furor-class fighter-Bomber
     Hit Points: 16 Crew: 1/6 Speed: 6 Armor: 8 AC: 3
    Fractal Impact Charge * 2 (+5 to hit/2d6+3, AP 15, Ammo 4)
    Spike 1
    1 Pirate  Captains Bomber
    Hit Points: 25. Crew: 1/1 Speed: 10 Armor: 15 AC: -3
    Fractal Impact Charge * 3 (+11 to hit/2d6+3, AP 15, Ammo 4)
    Spike 6(edited)
    """

    ships = []

    # Phoenix Ships
    for i in range(2):
        ship = Battleship(
            team=1,
            hp=170,
            armor=23,
            AC=-1
        )
        ship.register_weapon(SingularityGun())
        ship.register_weapon(SingularityGun())
        ship.register_weapon(LightningChargeMantle())
        ship.register_weapon(SpikeInversionProjector())

        ship.register_pilot(generate_pilot(random.randint(1, 5)))
        for i in range(10):
            ship.register_gunner(generate_gunner(random.randint(1, 5)))

        ship.register_AI(1)

        ships.append(ship)

    # BORG CUBE
    # TODO

    # Borg Cruisers
    for i in range(3):
        ship = Cruiser(
            hp=70,
            crew_max=200,
            speed=2,
            armor=18,
            AC=6,
            spike=3
        )
        ship.register_pilot(generate_pilot(random.randint(1, 5)))
        for _ in range(10):
            ship.register_gunner(generate_gunner(random.randint(1, 5)))

        ship.register_weapon(Gravcannon())
        ship.register_weapon(Gravcannon())
        ship.register_weapon(SmartCloud())
        ship.register_weapon(PlasmaBeam())

    # Borg fighters
    for i in range(130):
        ship = Fighter(
            hp=16,
            crew_max=6,
            speed=6,
            armor=8,
            AC=3,
            spike=1
        )
        ship.register_pilot(generate_pilot(random.randint(1, 5)))
        ship.register_gunner(generate_gunner(random.randint(1, 5)))
        ship.register_weapon(FractalImpactCharges())

        ship.register_AI(1)

        ships.append(ship)

    # Captain Bomber
    ship = Fighter(
        hp=25,
        crew_max=2,
        speed=10,
        armor=15,
        AC=-3,
        spike=6,
        max_power=15,
        max_hardpoints=10,
        max_mass=10
    )
    ship.register_pilot(generate_pilot(10))
    ship.register_gunner(generate_gunner(10))

    ship.register_weapon(FractalImpactCharges())
    ship.register_weapon(FractalImpactCharges())
    ship.register_weapon(FractalImpactCharges())

    ships.append(ship)


    # position them
    position_ships(arena, ships, (0, 0, 25))

