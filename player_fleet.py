import random

from kobayashi.ships import *
from kobayashi.weapons import *
from kobayashi.crew import *
from kobayashi.generate import *


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
            AC=-1,
            allies=[2,4]
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
            team=2,
            allies=[1,4],
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
            team=2,
            allies=[1,4],
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
        team=2,
        allies=[1,4],
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

    """
    Fleet 4: Neo Mandate
    3x Arx Capital ships
    Hit Points: 120 Crew: 100/1000 Speed: 2 Armor: 20 AC: 3
    Gravcannon (+5 to hit/4d6+2, AP 20), Mass Cannon x3 (+5 to hit/2d20+2, AP 20, Phase 3), Spike Inversion Projectors x2 (+5 to hit/3d8+2, AP 15, Phase 2), Sunshine Field (+5 to hit/2d6+2, AP 10, Cloud, Phase 2), Umbrella Barrage
    System (+5 to hit/Special)
    Hardened Polyceramic Overlay
    Spike 6
    6x Shantadurga Cruisers
    Hit Points: 80 Crew: 50/300 Speed: 1 Armor: 15 AC: 7
     Spike Inversion Projector x3 (+4 to hit/3d8+1, AP 15, Phase 2), Gravcannon (+4 to hit/4d6+1, AP 20), Smart Cloud
    (+4 to hit/3d10+1, Cloud, Clumsy)
    Hardened Polyceramic Overlay
    Spike 4
    12x Model Twelve - Frigate
    Hit Points: 60 Crew: 20/200 Speed: 6 Armor: 5 AC: 9
    Jitter Beam Projector (+3 to hit/3d8+1, AP 15, Phase 3), Plasma Beam (+3 to hit/3d6+1, AP 10)
    Spike 3
    48x
    Hit Points: 25 Crew: 5/20 Speed: 4 Armor: 5 AC: 6
     Plasma Beam (+3/3d6+1, AP 10)
    Spike 2
    """
    #Capital Ships for Neo Mandate.
    for i in range(3):
        ship = Cruiser(
            team=4,
            hp=80,
            armor=20+5,
            AC=3,
            spike=6,
            speed=1,
            crew_max=1000,
            allies=[2,1]
        )
        ship.register_pilot(generate_pilot(random.randint(1,5)))
        for i in range(20):
            ship.register_gunner(generate_gunner(random.randint(1, 5)))

        ship.register_weapon(Gravcannon())
        ship.register_weapon(MassCannon())
        ship.register_weapon(MassCannon())
        ship.register_weapon(SpikeInversionProjector())
        ship.register_weapon(SpikeInversionProjector())
        ship.register_weapon(SunshineField())
        ship.register_weapon(UmbrellaBarrageSystem())

        ships.append(ships)

    #Neo Mandate Shantadurga Crusers
    for i in range(6):
        ship = Cruiser(
        team=4,
        hp=80,
        armor=15+5,
        AC=7,
        spike=4,
        speed=1,
        crew_max=20,
        allies=[2,1]
        )
        ship.register_pilot(generate_pilot(random.randint(1,5)))
        for i in range(10):
            ship.register_gunner(generate_gunner(random.randint(1, 5)))

        ship.register_weapon(Gravcannon())
        ship.register_weapon(SpikeInversionProjector())
        ship.register_weapon(SpikeInversionProjector())
        ship.register_weapon(SpikeInversionProjector())
        ship.register_weapon(SmartCloud())

    #Neo Mandate Shantadurga Frigates
    for i in range(12):
        ship = Frigate(
        team=4,
        hp=60,
        armor=5,
        AC=9,
        spike=3,
        speed=6,
        crew_max=200,
        allies=[2,1]
        )
        ship.register_pilot(generate_pilot(random.randint(1,5)))
        for i in range(10):
            ship.register_gunner(generate_gunner(random.randint(1, 5)))

        ship.register_weapon(JitterBeamProjector())
        ship.register_weapon(PlasmaBeam())


    #Neo Mandate Shantadurga Fighters
    for i in range(25):
        ship = Fighter(
        team=4,
        hp=25,
        armor=5,
        AC=6,
        spike=2,
        speed=4,
        crew_max=200,
        allies=[2,1]
        )
        ship.register_pilot(generate_pilot(random.randint(1,5)))
        for i in range(10):
            ship.register_gunner(generate_gunner(random.randint(1, 5)))

        ship.register_weapon(PlasmaBeam())

    # position them
    position_ships(arena, ships, (0, 0, 25))
