import abc
from ..util import dice


class Weapon(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def wdamage(self):
        pass

    @abc.abstractproperty
    def wrange(self):
        pass
