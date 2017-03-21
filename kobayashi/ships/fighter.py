from .base_ship import Ship


class Fighter(Ship):
    def register_weapon(self, weapon):
        self.weapons.append(weapon)

    @property
    def capacity(self):
        return 2
