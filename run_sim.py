#!/usr/bin/env python3.6

# stdlib
import sys
import os
import pickle
import argparse
import inspect

# 3rd party
from datetime import datetime as dt
from IPython import embed

# local
import kobayashi as kob


def main():
    args = get_args()

    if args.ships or args.weapons:
        if args.ships:
            for name, member_type in inspect.getmembers(kob.ships):
                try:
                    if issubclass(member_type, kob.ships.Ship):
                        print(name)
                except:
                    pass
        if args.weapons:
            for name, member_type in inspect.getmembers(kob.weapons):
                try:
                    if issubclass(member_type, kob.weapons.Weapon):
                        print(name)
                except:
                    pass
    else:
        run_interactive(args.fleets, args.test_fleet)

def run_interactive(fleets, test_fleet):
    arena = kob.arena.Arena()

    if fleets is not None:
        imported_fleets = kob.fleets.get_fleet(fleets)
        for ships, center in imported_fleets:
            kob.generate.position_ships(arena, ships, center)

    if test_fleet:
        return

    tick = arena.tick
    show = arena.show
    list_ships = arena.list_ships
    tickn = arena.tickn
    save = lambda: save_arena(arena)


    def load():
        nonlocal arena  # this doesn't work, even though it should....
        # for some reason nonlocal arena is overwriting the higher scope version,
        # but when the function terminates the higher scope (old) version has not changed...
        arena = load_arena()
        return arena

    def help(obj=None):
        if obj is not None:
            return arena.help(obj)
        else:
            return {
                **arena.help(),
                'save': save,
                'load': load
            }

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

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--ships', action='store_true', default=False,
                        help=('List available ship classes'))
    parser.add_argument('-w', '--weapons', action='store_true', default=False,
                        help=('List available weapon classes'))
    parser.add_argument('-tf', '--test-fleet', action='store_true', default=False,
                        help=('Import fleet and quit'))
    parser.add_argument('-f', '--fleets', nargs='*', help='Fleets to import')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    sys.exit(main())
