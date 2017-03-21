import math
import random


def distance(coord1, coord2):
    return math.sqrt(sum((coord1[i] - coord2[i])**2 for i in range(len(coord1))))


def dice(numdice, dicesides, droplowcount=0):
    rolls = sorted([random.randint(1, dicesides)
                       for _ in range(numdice)],
                      key=lambda d: -d)
    if droplowcount != 0:
        return sum(rolls[:-droplowcount])
    return sum(rolls)


def parameterize_towards_point(coords):
    pass



# Exceptions

class FullCrewException(Exception): pass

class NoTargetsAvailable(Exception): pass

class NotEnoughSpeed(Exception): pass