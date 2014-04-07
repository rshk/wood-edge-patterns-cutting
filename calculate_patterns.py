"""
Calculate usable patterns for wood cutting.

Cuts enter wood from a side with a certain depth.
We use shapely to calculate area of intersection between
two "modules".

We also want to figure out which patterns are usable
and which ones would end up with too small area.

Steps:

1. Create polygons for each allowable cut
2. Generate patterns for all the possible cuts
   -> remove duplicates!
3. Build a table matching patterns to possible
   successors.
4. Write some algorithm to convert some sequence
   into a sequence of patterns.
"""

from __future__ import division
from itertools import product
from shapely.geometry import Polygon
from shapely.affinity import rotate

DEPTHS = [  # Fractions
    (0, 1),
    (1, 3),
    (1, 2),
]

SIDE_LENGTH = 1000


def generate_cuts(depths, side=SIDE_LENGTH):
    """
    For each depth, generate a polygon describing
    the cut on the "north" side.
    """
    for num, den in depths:
        ad = num * side / den
        poly = Polygon([(0, 0), (side, 0), (side, ad), (0, ad)])
        yield poly


def generate_patterns(depths):
    cuts_n = list(generate_cuts(depths))
    cuts_e = [rotate(x, 90) for x in cuts_n]
    cuts_s = [rotate(x, 180) for x in cuts_n]
    cuts_w = [rotate(x, 270) for x in cuts_n]
    for cut_n, cut_e, cut_s, cut_w in product(cuts_n, cuts_e, cuts_s, cuts_w):
        poly = cut_n.union(cut_e).union(cut_s).union(cut_w)
        yield poly


for i, obj in enumerate(generate_patterns(DEPTHS)):
    print("Pattern {0}: area {1:.0f}%".format(
        i, obj.area * 100 / (SIDE_LENGTH ** 2)))
