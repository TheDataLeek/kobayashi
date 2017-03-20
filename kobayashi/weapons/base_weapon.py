import abc


class Weapon(metaclass=abc.ABCMeta):
    def __init__(self, weapon_range, weapon_damage):
        self.weapon_damage = weapon_damage
        self.weapon_range = weapon_range

    @property
    def damage(self):
        if callable(self.weapon_damage):
            return self.weapon_damage()
        return self.weapon_damage

    @property
    def wrange(self):
        if callable(self.weapon_range):
            return self.weapon_range()
        return self.weapon_range
