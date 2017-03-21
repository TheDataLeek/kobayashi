from .base_ship import Ship


class Fighter(Ship):

    speed = 5
    armor = 5
    hp = 8
    crew_min = 1
    crew_max = 1
    armor_class = 4
    max_power = 5
    max_mass = 2
    max_hardpoints = 1
    ship_class = 0

    def register_weapon(self, weapon):
        self.weapons.append(weapon)


    @property
    def capacity(self):
        return 2


class Shuttle(Ship):
    speed = 3
    armor = 0
    hp = 15
    crew_min = 1
    crew_max = 10
    armor_class = 9
    max_power = 3
    max_mass = 2
    max_hardpoints = 1
    ship_class = 0

    def register_weapon(self, weapon):
        self.weapons.append(weapon)

    @property
    def capacity(self):
        return 2


class FreeMerchant(Ship):
    speed = 3
    armor = 2
    hp = 20
    crew_min = 1
    crew_max = 6
    armor_class = 6
    max_power = 10
    max_mass = 15
    max_hardpoints = 2
    ship_class = 1

    def register_weapon(self, weapon):
        self.weapons.append(weapon)

    @property
    def capacity(self):
        return 2


class PatrolBoat(Ship):
    speed = 4
    armor = 5
    hp = 25
    crew_min = 5
    crew_max = 20
    armor_class = 6
    max_power = 10
    max_mass = 10
    max_hardpoints = 4
    ship_class = 1

    def register_weapon(self, weapon):
        self.weapons.append(weapon)

    @property
    def capacity(self):
        return 2


class Frigate(Ship):
    speed = 2
    armor = 10
    hp = 40
    crew_min = 10
    crew_max = 40
    armor_class = 7
    max_power = 15
    max_mass = 15
    max_hardpoints = 6
    ship_class = 1

    def register_weapon(self, weapon):
        self.weapons.append(weapon)

    @property
    def capacity(self):
        return 2


class BulkFreighter(Ship):
    speed = 0
    armor = 0
    hp = 40
    crew_min = 10
    crew_max = 40
    armor_class = 9
    max_power = 15
    max_mass = 25
    max_hardpoints = 2
    ship_class = 2

    def register_weapon(self, weapon):
        self.weapons.append(weapon)

    @property
    def capacity(self):
        return 2


class Cruiser(Ship):
    speed = 1
    armor = 15
    hp = 60
    crew_min = 50
    crew_max = 200
    armor_class = 6
    max_power = 50
    max_mass = 30
    max_hardpoints = 10
    ship_class = 2

    def register_weapon(self, weapon):
        self.weapons.append(weapon)

    @property
    def capacity(self):
        return 2


class Battleship(Ship):
    speed = 0
    armor = 20
    hp = 100
    crew_min = 200
    crew_max = 1000
    armor_class = 4
    max_power = 75
    max_mass = 50
    max_hardpoints = 15
    ship_class = 3

    def register_weapon(self, weapon):
        self.weapons.append(weapon)

    @property
    def capacity(self):
        return 2


class Carrier(Ship):
    speed = 0
    armor = 10
    hp = 75
    crew_min = 300
    crew_max = 1500
    armor_class = 6
    max_power = 50
    max_mass = 100
    max_hardpoints = 4
    ship_class = 3

    def register_weapon(self, weapon):
        self.weapons.append(weapon)

    @property
    def capacity(self):
        return 2