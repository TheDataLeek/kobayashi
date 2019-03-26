# stdlib
import os
import json
import inspect
import importlib

from typing import List, Union

# local
from . import ships
from .exceptions import InvalidJSON


def get_fleet(location: Union[str, list]) -> List[ships.Ship]:
    if isinstance(location, list):
        combined = []
        for x in location:
            results = get_fleet(x)
            combined += results
        return combined
    else:
        if os.path.isdir(location):
            ships = []
            for root, dirs, files in os.walk(location):
                for file in files:
                    fleet = parse_file(os.path.join(root, file))
                    if fleet is not None:
                        ships.append(fleet)
        elif os.path.isfile(location):
            ships = parse_file(location)
        return ships


def parse_file(path):
    if path.endswith('.json'):
        return parse_json_file(path)
    elif path.endswith('.py'):
        return parse_python_file(path)

def parse_python_file(path):
    # module_name = ".".join(os.path.basename(path).split('.')[:-1])
    # importlib.import_module(path, f'fleets')
    print(inspect.getmembers(path))
    return [], (0, 0, 0)

def parse_json_file(path):
    with open(path, 'r') as fobj:
        fleet_data = json.loads(fobj.read())

    if fleet_data.get('center') is None:
        raise InvalidJSON('Need to provide a center for fleet')

    if fleet_data.get('ships') is None:
        raise InvalidJSON('Need to provide a list of ships for fleet')

    ship_dict = get_ships()

    fleet = []
    for ship in fleet_data['ships']:
        try:
            ship_type = ship['base']
        except KeyError:
            ship_type = 'Ship'

        count = 1
        if 'count' in ship:
            count = int(ship['count'])

        ship = {k: v for k, v in ship.items() if k not in ['count', 'base']}

        for i in range(count):
            new_ship = ship_dict[ship_type](**ship)
            fleet.append(new_ship)

    return fleet, tuple(fleet_data['center'])


def get_ships(module=None):
    if module is None:
        module = ships

    ship_dict = {}
    for name, instance in inspect.getmembers(module):
        if inspect.ismodule(instance):
            ship_dict = {**ship_dict, **get_ships(module=instance)}
        elif inspect.isclass(instance):
            if issubclass(instance, ships.Ship):
                ship_dict[name] = instance
    return ship_dict
