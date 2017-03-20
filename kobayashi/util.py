import math
import random


def distance(coord1, coord2):
    return math.sqrt(sum((coord1[i] - coord2[i])**2 for i in range(len(coord1))))


def dice(numdice, dicesides, droplowcount=0):
    return sorted([random.randint(1, dicesides)
                   for _ in range(numdice)],
                  key=lambda d: -d)[:-droplowcount]