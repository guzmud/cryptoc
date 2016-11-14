#!/usr/bin/python

import random  # for testing purposes
import string  # for testing purposes


def cypher_str(strvalue, fencenum):
    lstvalue = list(strvalue)
    fence = [[] for f in range(fencenum)]
    flow = range(fencenum) + [x for x in reversed(range(1, fencenum-1))]
    flowptr = 0

    while len(lstvalue) > 0:
        fence[flow[flowptr]].append(lstvalue.pop(0))
        flowptr = (flowptr + 1) % len(flow)

    return ''.join([''.join(k) for k in fence])


def uncypher_str(strvalue, fencenum):
    fence = [[] for f in range(fencenum)]
    flow = range(fencenum) + [x for x in reversed(range(1, fencenum-1))]
    flowptr = 0

    for k in range(len(strvalue)):
        fence[flow[flowptr]].append(k)
        flowptr = (flowptr + 1) % len(flow)

    translation = []
    [translation.extend(f) for f in fence]

    return ''.join([strvalue[translation.index(k)]
                    for k in range(len(strvalue))])


def test_str(tstr, fencenum):
    """Test the equality between a string and its decyphered cypher"""
    lstr = uncypher_str(cypher_str(tstr, fencenum), fencenum)
    return tstr == lstr


def test_routine(rounds=500, verbose=False):
    """
    Test routine using random ascii printables for R rounds
    """

    fencenumber = random.randint(1,10)

    if verbose:
        print "Testing {rounds} rounds: ".format(rounds=rounds),

    for x in range(rounds):
        tstr = ''.join(random.sample(string.printable,
                                     random.randint(20, 50)))

        if not test_str(tstr, fencenumber):
            if verbose:
                print "Failed string {tstr}: ".format(tstr=tstr)
                print "fencenumber: {fencenum}".format(fencenum=fencenumber)
            return False

    return True
