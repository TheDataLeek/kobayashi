from .base_ship import Ship


class NavalCourier(Ship):
    speed = 5
    armor = 5
    hp = 20
    crew_min = 1
    crew_max = 10
    armor_class = 5
    max_power = 10
    max_mass = 15
    max_hardpoints = 0
    ship_class = 1


class TroopTransport(Ship):
    speed = 0
    armor = 10
    hp = 50
    crew_min = 30
    crew_max = 3000
    armor_class = 7
    max_power = 30
    max_mass = 60
    max_hardpoints = 3
    ship_class = 2


class LogisticsShip(Ship):
    speed = 1
    armor = 15
    hp = 60
    crew_min = 30
    crew_max = 160
    armor_class = 5
    max_power = 40
    max_mass = 40
    max_hardpoints = 3
    ship_class = 2

