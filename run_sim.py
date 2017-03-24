#!/usr/bin/env python3.6


import sys
import kobayashi as kob


def main():
    arena = kob.arena.Arena()
    arena.register_ship((0, 2, 1), kob.generate.generate_ship(kob.ships.Fighter))
    arena.register_ship((10, 20, 2), kob.generate.generate_ship(kob.ships.Fighter))
    arena.register_ship((13, 21, 2), kob.generate.generate_ship(kob.ships.Fighter))
    arena.register_ship((18, 22, 2), kob.generate.generate_ship(kob.ships.Fighter))
    arena.register_ship((13, 23, 2), kob.generate.generate_ship(kob.ships.Fighter))
    arena.register_ship((15, 15, 0), kob.generate.generate_ship(kob.ships.Fighter))

    for _ in range(20):
        arena.tick()
        # arena.show()


    from player_fleet import phoenix

    phoenix()






if __name__ == '__main__':
    sys.exit(main())
