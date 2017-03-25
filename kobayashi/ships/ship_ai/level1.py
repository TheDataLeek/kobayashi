from .base_ai import ShipAI


class Level1(ShipAI):
    def move(self, arena):
        targets = self.ship.list_ships(arena)
        if len(targets) != 0:
            target, distance, threat = targets[0]
            if not self.ship.within_range(target):
                self.ship.move_towards(arena, target.coords)
