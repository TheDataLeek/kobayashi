import kobayashi as kob

import random


def generate(arena):
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
        team=2,
        crew_max=1600,
        spike=4
    )
    pilot = kob.generate.generate_pilot(ship.ship_class + random.randint(1, 5))
    ship.register_pilot(pilot)

    for i in range(249):
        gunner = kob.generate.generate_gunner(ship.ship_class + random.randint(1, 5))
        ship.register_gunner(gunner)

    ship.register_weapon(kob.weapons.ImplosionFieldProjector())
    ship.register_weapon(kob.weapons.RandrodWarpLineGun())
    #TODO SiegeMissiles

    ship.register_AI(1)
    ships.append(ship)

    for i in range(750):
        ship = kob.ships.Fighter(
            team=2,
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

    kob.generate.position_ships(arena, ships, (0, 0, 0))
