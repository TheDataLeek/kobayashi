import abc

class ShipAI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def new_pos(self, ship, arena): pass
