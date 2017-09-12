import math

import pytest
from pytest import approx

from .. import util

def test_distance():
    test_points = [
        ((0, 0), (0, 1), 1),
        ((0, 0), (1, 1), math.sqrt(2)),
        ((0, 0, 0), (0, 0, 1), 1),
        ((0, 0, 0), (1, 1, 0), math.sqrt(2))
    ]

    for p1, p2, dist in test_points:
        assert util.distance(p1, p2) == approx(dist)

