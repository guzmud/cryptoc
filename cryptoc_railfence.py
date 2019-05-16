#!/usr/bin/python

import random  # for testing purposes
import string  # for testing purposes

from genutils import data_gen

def cypher_str(strvalue, fencenum):
    lstvalue = list(strvalue)
    fence = [[] for f in range(fencenum)]
    flow = list(range(fencenum)) + [x for x in reversed(range(1, fencenum-1))]
    flowptr = 0

    while len(lstvalue) > 0:
        fence[flow[flowptr]].append(lstvalue.pop(0))
        flowptr = (flowptr + 1) % len(flow)

    return ''.join([''.join(k) for k in fence])


def uncypher_str(strvalue, fencenum):
    fence = [[] for f in range(fencenum)]
    flow = list(range(fencenum)) + [x for x in reversed(range(1, fencenum-1))]
    flowptr = 0

    for k in range(len(strvalue)):
        fence[flow[flowptr]].append(k)
        flowptr = (flowptr + 1) % len(flow)

    translation = []
    [translation.extend(f) for f in fence]

    return ''.join([strvalue[translation.index(k)]
                    for k in range(len(strvalue))])


def test_routine(rounds=500):
    """
    Test routine using random ascii printables for R rounds
    """
    fencenum = random.randint(1,10)
    for x in range(rounds):
        tstr = data_gen()
        lstr = uncypher_str(cypher_str(tstr, fencenum), fencenum)
        assert tstr == lstr
