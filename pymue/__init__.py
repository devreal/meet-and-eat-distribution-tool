from _pymue import Team, DistanceMatrix, GuestPair, Calculation, RoundData, IterationData, GuestCandidate, Round

def pair_pprint(pair):
    return "(%s, %s)" % (pair.first, pair.second)

GuestPair.__repr__ = pair_pprint
