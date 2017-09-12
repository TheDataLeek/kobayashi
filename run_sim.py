#!/usr/bin/env python3.6

import sys
import os
from datetime import datetime as dt
import pickle
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
    help = arena.help
    save = lambda: save_arena(arena)

    def load():
        nonlocal arena  # this doesn't work, even though it should....
        # for some reason nonlocal arena is overwriting the higher scope version,
        # but when the function terminates the higher scope (old) version has not changed...
        arena = load_arena()
        return arena

    embed()


def save_arena(arena):
    if not os.path.isdir('saves'):
        os.mkdir('saves')

    with open(f'saves/gamestate_{dt.isoformat(dt.now())}.pkl', 'wb') as savefile:
        pickle.dump(arena, savefile, pickle.HIGHEST_PROTOCOL)


def load_arena():
    contents = [x for x in os.listdir('saves/')
                if (os.path.isfile(os.path.join('saves', x)) and x.startswith('gamestate'))]
    contents.sort(key=lambda f: os.path.getmtime(os.path.join('saves', f)))
    for i, f in enumerate(contents):
        print(f'({i + 1}) {f}')
    while True:
        choice = input(f'Please select a file to load (default {contents[-1]}) ')
        try:
            if choice == '':
                choice = 0
                break
            choice = int(choice)
            if choice < 1 or choice > len(contents):
                raise ValueError
            break
        except ValueError:
            print(f'Invalid input. Please enter a number between 1 and {len(contents)}')
    file_to_load = os.path.join('saves', contents[choice - 1])

    with open(file_to_load, 'rb') as savefile:
        arena = pickle.load(savefile)

    return arena


if __name__ == '__main__':
    sys.exit(main())
