#!/usr/bin/env python3.6


import sys
import kobayashi as kob


def main():
    arena = kob.arena.Arena(30, 30, layers=3)
    arena.register_ship((0, 2, 1), kob.generate_ship(kob.Fighter))
    arena.register_ship((10, 20, 2), kob.generate_ship(kob.Fighter))
    arena.register_ship((13, 21, 2), kob.generate_ship(kob.Fighter))
    arena.register_ship((18, 22, 2), kob.generate_ship(kob.Fighter))
    arena.register_ship((13, 23, 2), kob.generate_ship(kob.Fighter))
    arena.register_ship((15, 15, 0), kob.generate_ship(kob.Fighter))

    for _ in range(20):
        arena.tick()
        arena.show()






if __name__ == '__main__':
    sys.exit(main())
