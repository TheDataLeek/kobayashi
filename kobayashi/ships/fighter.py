from .base_ship import Ship


class Fighter(Ship):
    @property
    def capacity(self):
        return 2
