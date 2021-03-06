import random

import kobayashi as kob


# player fleet
def generate_player_fleet(arena):
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
        ship = kob.ships.Battleship(
            team=1,
            hp=170,
            armor=28,
            AC=-2,
            allies=[2, 4],
            speed=3
        )
        ship.register_weapon(kob.weapons.SingularityGun(wrange=16))
        ship.register_weapon(kob.weapons.SingularityGun(wrange=16))
        ship.register_weapon(kob.weapons.LightningChargeMantle(wrange=16))
        ship.register_weapon(kob.weapons.SpikeInversionProjector(wrange=16))

        ship.register_pilot(kob.generate.generate_pilot(random.randint(1, 5)))
        for i in range(10):
            ship.register_gunner(kob.generate.generate_gunner(random.randint(1, 5)))

        ship.player_ship = True
        ship.register_AI(1)

        ships.append(ship)

    # position them
    kob.generate.position_ships(arena, ships, (10, 10, 0))

    ships = []

    """
    Fleet 5: Valkyrie (Frigate)
    Hit points 20, Crew 10/10 Speed: 10 Armor: 10 AC 0
    Mag Spike Array+5/2d6+5 Flak, Phase 1, Ammo 10
    Grav Eddy Displacer Hardened Polyceramic Overlay
    """
    ship = kob.ships.Frigate(
        team=5,
        hp=20,
        speed=10,
        armor=15,
        AC=0,
        spike=3
    )

    ship.register_pilot(kob.generate.generate_pilot(5))
    for i in range(10):
        ship.register_gunner(kob.generate.generate_gunner(5))
    ship.register_weapon(kob.weapons.MagSpikeArray(
        to_hit_mod=5,
        extra_dmg=5,
        flak=True,
        phase=1,
        ammo=10,
        wrange=2
    ))

    ship.destroyed = True

    ship.player_ship = True

    ship.register_AI(1)

    ships.append(ship)

    kob.generate.position_ships(arena, ships, (100, 100, 100))

    ships = []

    # BORG CUBE
    """
    Borg Cube
    Hitpoints 30 Shields 100 Crew: 100/200 Speed: 1 Armor: 15 AC 0
    Gravcannon (+4 to hit/4d6+1, AP 20), Spike Inversion Projector x2 (+4 to hit/3d8+1, AP 15, Phase 2), Sunshine Field
    (+4 to hit/2d6+1, AP 10, Cloud, Phase 2), Umbrella Barrage System (+4 to hit/Special)
    Armor: Regenerating Shield (10) Adapting Shield(Hits by same weapon lose 1 damage), Hardened Polyceramic Overlay
    """
    ship = kob.ships.Battleship(
        hp=130,
        shields=100,
        speed=1,
        armor=23,
        AC=0,
        team=2,
        allies=[1, 4]
    )

    ship.register_pilot(kob.generate.generate_pilot(3))
    for _ in range(10):
        ship.register_gunner(kob.generate.generate_gunner(3))
    ship.register_weapon(kob.weapons.SunshineField(
        to_hit_mod=4,
        extra_dmg=1,
        armor_pen=10,
        cloud=True,
        wrange=8,
        phase=2
    ))
    ship.register_weapon(kob.weapons.Gravcannon(
        to_hit_mod=4,
        extra_dmg=1,
        wrange=8,
        armor_pen=20
    ))
    ship.register_weapon(kob.weapons.SpikeInversionProjector(
        to_hit_mod=4,
        extra_dmg=1,
        wrange=8,
        armor_pen=15,
        phase=2
    ))
    ship.register_weapon(kob.weapons.SpikeInversionProjector(
        to_hit_mod=4,
        extra_dmg=1,
        armor_pen=15,
        wrange=8,
        phase=2
    ))

    ship.register_AI(1)

    ships.append(ship)

    # Borg Cruisers
    for i in range(4):
        ship = kob.ships.Cruiser(
            hp=70,
            crew_max=200,
            speed=2,
            armor=18,
            AC=6,
            team=2,
            allies=[1, 4],
            spike=3,
        )
        ship.register_pilot(kob.generate.generate_pilot(random.randint(1, 5)))
        for _ in range(10):
            ship.register_gunner(kob.generate.generate_gunner(random.randint(1, 5)))

        ship.register_weapon(kob.weapons.Gravcannon(wrange=8))
        ship.register_weapon(kob.weapons.Gravcannon(wrange=8))
        ship.register_weapon(kob.weapons.SmartCloud(wrange=8))
        ship.register_weapon(kob.weapons.PlasmaBeam(wrange=8))

        ship.register_AI(1)

        ships.append(ship)

    # Borg Frigates
    """
    2x Reproach-class Hunter-Killer frigate
    Hit Points: 45 Crew: 3/60 Speed: 2 Armor: 13 AC: 4
     Torpedo Launchers * 2 (+8 to hit/3d8+3, AP 20, Ammo 4), Plasma Beam (+8 to hit/3d6+3, AP 10)
     Hardened Polyceramic Overlay, Augmented Plating
    Fittings Spike Drive-3
    """
    for i in range(2):
        ship = kob.ships.Frigate(
            team=2,
            allies=[1, 4],
            hp=45,
            speed=2,
            armor=18,
            AC=4,
            spike=3,
            max_power=40
        )
        ship.register_pilot(kob.generate.generate_pilot(3))
        for _ in range(10):
            ship.register_gunner(kob.generate.generate_gunner(3))
        ship.register_weapon(kob.weapons.PlasmaBeam(
            to_hit_mod=8,
            extra_dmg=3,
            wrange=2,
            armor_pen=10
        ))
        ship.register_weapon(kob.weapons.TorpedoLauncher(
            to_hit_mod=8,
            wrange=2,
            extra_dmg=3,
            armor_pen=20,
            ammo=4
        ))
        ship.register_weapon(kob.weapons.TorpedoLauncher(
            to_hit_mod=8,
            extra_dmg=3,
            wrange=2,
            armor_pen=20,
            ammo=4
        ))

        ship.register_AI(1)

        ships.append(ship)


    # Borg fighters
    for i in range(130):
        ship = kob.ships.Fighter(
            hp=16,
            crew_max=6,
            speed=6,
            armor=8,
            AC=3,
            team=2,
            allies=[1,4],
            spike=1
        )
        ship.register_pilot(kob.generate.generate_pilot(random.randint(1, 5)))
        ship.register_gunner(kob.generate.generate_gunner(random.randint(1, 5)))
        ship.register_weapon(kob.weapons.FractalImpactCharges())

        ship.register_AI(1)

        ships.append(ship)

    # Captain Bomber
    ship = kob.ships.Fighter(
        hp=25,
        crew_max=2,
        speed=10,
        armor=15,
        AC=-3,
        spike=6,
        team=2,
        allies=[1, 4],
        max_power=15,
        max_hardpoints=10,
        max_mass=10
    )
    ship.register_pilot(kob.generate.generate_pilot(10))
    ship.register_gunner(kob.generate.generate_gunner(10))

    ship.register_weapon(kob.weapons.FractalImpactCharges())
    ship.register_weapon(kob.weapons.FractalImpactCharges())
    ship.register_weapon(kob.weapons.FractalImpactCharges())

    ship.register_AI(1)

    ships.append(ship)

    kob.generate.position_ships(arena, ships, (0, 0, 0))

    ships = []

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
        ship = kob.ships.Cruiser(
            team=4,
            hp=80,
            armor=20+5,
            AC=3,
            spike=6,
            speed=1,
            crew_max=1000,
            allies=[2,1],
            max_hardpoints=100,
            max_power=100,
            max_mass=100
        )
        ship.register_pilot(kob.generate.generate_pilot(random.randint(1,5)))
        for i in range(20):
            ship.register_gunner(kob.generate.generate_gunner(random.randint(1, 5)))

        ship.register_weapon(kob.weapons.Gravcannon(wrange=16))
        ship.register_weapon(kob.weapons.MassCannon(wrange=16))
        ship.register_weapon(kob.weapons.MassCannon(wrange=16))
        ship.register_weapon(kob.weapons.SpikeInversionProjector(wrange=16))
        ship.register_weapon(kob.weapons.SpikeInversionProjector(wrange=16))
        ship.register_weapon(kob.weapons.SunshineField(wrange=16))
        ship.register_weapon(kob.weapons.UmbrellaBarrageSystem(wrange=16))

        ship.register_AI(1)

        ships.append(ship)

    #Neo Mandate Shantadurga Crusers
    for i in range(6):
        ship = kob.ships.Cruiser(
        team=4,
        hp=80,
        armor=15+5,
        AC=7,
        spike=4,
        speed=1,
        crew_max=20,
        max_hardpoints=100,
        max_power=100,
        max_mass=100,
        allies=[2,1]
        )
        ship.register_pilot(kob.generate.generate_pilot(random.randint(1,5)))
        for i in range(10):
            ship.register_gunner(kob.generate.generate_gunner(random.randint(1, 5)))

        ship.register_weapon(kob.weapons.Gravcannon(wrange=8))
        ship.register_weapon(kob.weapons.SpikeInversionProjector(wrange=8))
        ship.register_weapon(kob.weapons.SpikeInversionProjector(wrange=8))
        ship.register_weapon(kob.weapons.SpikeInversionProjector(wrange=8))
        ship.register_weapon(kob.weapons.SmartCloud(wrange=8))

        ship.register_AI(1)
        ships.append(ship)

    #Neo Mandate Shantadurga Frigates
    for i in range(12):
        ship = kob.ships.Frigate(
        team=4,
        hp=60,
        armor=5,
        AC=9,
        spike=3,
        speed=6,
        crew_max=200,
            max_hardpoints=100,
            max_power=100,
            max_mass=100,
        allies=[2,1]
        )
        ship.register_pilot(kob.generate.generate_pilot(random.randint(1,5)))
        for i in range(10):
            ship.register_gunner(kob.generate.generate_gunner(random.randint(1, 5)))

        ship.register_weapon(kob.weapons.JitterBeamProjector(wrange=2))
        ship.register_weapon(kob.weapons.PlasmaBeam(wrange=2))
        ship.register_AI(1)
        ships.append(ship)


    #Neo Mandate Shantadurga Fighters
    for i in range(48):
        ship = kob.ships.Fighter(
        team=4,
        hp=25,
        armor=5,
        AC=6,
        spike=2,
        speed=4,
        crew_max=200,
            max_hardpoints=100,
            max_power=100,
            max_mass=100,
        allies=[2,1]
        )
        ship.register_pilot(kob.generate.generate_pilot(random.randint(1,5)))
        for i in range(10):
            ship.register_gunner(kob.generate.generate_gunner(random.randint(1, 5)))

        ship.register_weapon(kob.weapons.PlasmaBeam())

        ship.register_AI(1)
        ships.append(ship)

    # position them
    kob.generate.position_ships(arena, ships, (20, 20, 0))


def generate_enemy_fleet(arena):
    """
    Fleet 3: Veng
    1x Veng Super Cruiser
     Hit Points: 120 Crew: 250/1,600 Speed: 3 Armor: 25 AC: 4
    Implosion Field Projector (+10 to hit/4d20+2(Forces fighters to save vs death), AP 25, Phase 2), “Ramrod” Warp-line Gun (+10 to hit/2d20+42, AP 25),
    “Antaeus” Siege Missiles (Special, can hit things that take cover behind planets)
    Hardened Polyceramic Overlay
    Spike Drive-4,
    750 Veng Fighter Bombers
    Hit Points: 10 Crew 1/1 Speed: 4 Armor:6 AC 3
    2x Plasma Beams (+6 to hit/3d6+1, AP 10)
    Hardened Polyceramic Overlay
    Spike 3
    """
    # kob.generate.generate_fleet(arena, size=10, team=1, center=(0, 0, 0))
    # kob.generate.generate_fleet(arena, size=10, team=2, center=(0, 0, 100))
    # kob.generate.generate_fleet(arena, size=10, team=3, center=(100, 0, 0))

    ships = []

    ship = kob.ships.Cruiser(
        hp=120,
        speed=3,
        armor=25+5, #5 armor because of reduced AP of attacking weapons due to polyceramic overlay.
        AC=4,
        team=3,
        crew_max=1600,
        spike=4
    )
    pilot = kob.generate.generate_pilot(ship.ship_class + random.randint(1, 5))
    ship.register_pilot(pilot)

    for i in range(249):
        gunner = kob.generate.generate_gunner(ship.ship_class + random.randint(1, 5))
        ship.register_gunner(gunner)

    ship.register_weapon(kob.weapons.ImplosionFieldProjector(wrange=8))
    ship.register_weapon(kob.weapons.RandrodWarpLineGun(wrange=8))
    #TODO SiegeMissiles

    ship.register_AI(1)
    ships.append(ship)

    for i in range(750):
        ship = kob.ships.Fighter(
            team=3,
            hp=10,
            speed=4,
            armor=6,
            AC=3,
            spike=3,
            crew_max=2,
            max_power=10,
            max_hardpoints=10,
            max_mass=10
        )
        ship.register_pilot(kob.generate.generate_pilot(random.randint(1, 5)))
        ship.register_gunner(kob.generate.generate_gunner(random.randint(1, 5)))
        ship.register_weapon(kob.weapons.PlasmaBeam())
        ship.register_weapon(kob.weapons.PlasmaBeam())

        ship.register_AI(1)
        ships.append(ship)

    kob.generate.position_ships(arena, ships, (10, 10, 50))
