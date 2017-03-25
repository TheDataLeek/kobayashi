import abc

class ShipAI(metaclass=abc.ABCMeta):
    def __init__(self, ship):
        self.ship = ship

    @abc.abstractmethod
    def move(self, ship, arena): pass
