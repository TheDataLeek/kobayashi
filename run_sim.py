#!/usr/bin/env python3.6


import sys
import kobayashi as kob


def main():
    arena = kob.arena.Arena()
    kob.generate.generate_fleet(arena, size=10, team=1, center=(0, 0, 0))
    kob.generate.generate_fleet(arena, size=10, team=2, center=(100, 100, 100))

    commands = {
        'tick': arena.tick,
        'show': arena.show,
        'list': arena.list_ships,
    }

    while True:
        try:
            command = input('$--> ')

            if command.lower() == 'exit':
                break
            elif command.lower() in ['help', '?']:
                print(f'arena -> {type(arena)}')
                for k, v in commands.items():
                    print(f'{k} -> {v}')
            else:
                try:
                    commands[command]()
                except KeyError:
                    try:
                        results = eval(command)
                        if results is not None:
                            print(results)
                    except Exception as e:
                        print(e)

        except (EOFError, KeyboardInterrupt) as e:
            break





if __name__ == '__main__':
    sys.exit(main())
