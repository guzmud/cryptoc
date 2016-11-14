#!/usr/bin/python

import random  # for testing purposes

MODULO = 256


def cypher_int(intvalue, rotvalue):
    return (intvalue + rotvalue) % MODULO


def cypher_char(charvalue, rotvalue):
    return chr(cypher_int(ord(charvalue), rotvalue))


def cypher_str(strvalue, rotvalue):
    return ''.join([cypher_char(c, rotvalue) for c in strvalue])


def uncypher_int(intvalue, rotvalue):
    return (intvalue - rotvalue) % MODULO


def uncypher_char(charvalue, rotvalue):
    return chr(uncypher_int(ord(charvalue), rotvalue))


def uncypher_str(strvalue, rotvalue):
    return ''.join([uncypher_char(c, rotvalue) for c in strvalue])


def test_str(tstr, rotvalue):
    """Test the equality between a string and its decyphered cypher"""
    lstr = uncypher_str(cypher_str(tstr, rotvalue),
                        rotvalue)
    return tstr == lstr


def test_routine(rounds=500, verbose=False):
    """
    Test routine using random ascii letters for R rounds
    """

    if verbose:
        print "Testing {rounds} rounds: ".format(rounds=rounds),

    for x in range(rounds):
        tstr = ''.join([chr(random.randint(0, MODULO-1))
                        for y
                        in range(random.randint(50, 250))])

        rotvalue = random.randint(-2*MODULO, 2*MODULO)

        if not test_str(tstr, rotvalue):
            if verbose:
                print "Failed string {tstr}: ".format(tstr=tstr)
                print "Operation: cypher = (clear + rotvalue) % M, with"
                print "rotvalue: {rotvalue}; "
                print "M: {modulo}".format(rotvalue=rotvalue,
                                           modulo=modulo)
            return False

    return True
