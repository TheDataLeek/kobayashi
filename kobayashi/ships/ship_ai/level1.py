from .base_ai import ShipAI


class Level1(ShipAI):
    def new_pos(self, ship, arena):
        enemies = [e for e in arena.ships if ship.team != e.team]
        return (0, 0, 0)
