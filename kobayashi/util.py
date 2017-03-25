import math
import random
import itertools

def distance(coord1, coord2):
    return math.sqrt(sum((coord1[i] - coord2[i])**2 for i in range(len(coord1))))


def dice(numdice, dicesides, droplowcount=0):
    rolls = sorted([random.randint(1, dicesides)
                       for _ in range(numdice)],
                      key=lambda d: -d)
    if droplowcount != 0:
        return sum(rolls[:-droplowcount])
    return sum(rolls)

def all_neighbor_points(point):
    coord_mods = list(set(itertools.permutations([0,0,0,1,1,1,-1,-1,-1], 3)))
    new_coords = [tuple(point[i] + coord_mods[j][i]
                        for i in range(len(point)))
                  for j in range(len(coord_mods))]
    return new_coords
