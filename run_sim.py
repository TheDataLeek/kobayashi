#!/usr/bin/env python3.6

import sys
from IPython import embed

import kobayashi as kob

import player_fleet
import enemy_fleet


def main():
    arena = kob.arena.Arena()

    player_fleet.generate(arena)
    enemy_fleet.generate(arena)

    tick = arena.tick
    show = arena.show
    list_ships = arena.list_ships
    tickn = arena.tickn
    save = lambda: arena.show(save=True)
    help = arena.help

    embed()




if __name__ == '__main__':
    sys.exit(main())
