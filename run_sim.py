#!/usr/bin/env python3.6


import sys
import kobayashi as kob


def main():
    arena = kob.arena.Arena()
    arena.register_ship((0, 0, 0), kob.generate.generate_ship(kob.ships.Fighter))
    arena.register_ship((100, 100, 100), kob.generate.generate_ship(kob.ships.Fighter))

    commands = {
        'tick': arena.tick,
        'savetick': arena.show,
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
                        try:
                            results = eval(command)
                            if results is not None:
                                print(results)
                        except SyntaxError:
                            print('Syntax Error')
                    except NameError:
                        print("Command not found")

        except (EOFError, KeyboardInterrupt) as e:
            break





if __name__ == '__main__':
    sys.exit(main())
