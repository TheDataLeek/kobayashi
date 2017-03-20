#!/usr/bin/env python3.6


import sys
import kobayashi as kob


def main():
    arena = kob.arena.Arena(3, 3, layers=1)
    arena.register_ship((0, 0), kob.generate_ship(kob.Fighter))

    print(arena)





if __name__ == '__main__':
    sys.exit(main())
