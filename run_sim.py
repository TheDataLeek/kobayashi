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

    embed()

    # while True:
    #     try:
    #         command = input('$--> ')

    #         if command.lower() == 'exit':
    #             break
    #         elif command.lower() in ['help', '?']:
    #             print(f'arena -> {type(arena)}')
    #             for k, v in commands.items():
    #                 print(f'{k} -> {v}')
    #         else:
    #             try:
    #                 commands[command]()
    #             except KeyError:
    #                 try:
    #                     results = eval(command)
    #                     if results is not None:
    #                         print(results)
    #                 except Exception as e:
    #                     print(e)

    #     except (EOFError, KeyboardInterrupt) as e:
    #         break





if __name__ == '__main__':
    sys.exit(main())
