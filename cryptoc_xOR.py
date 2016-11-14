#!/usr/bin/python

import random  # for testing purposes


def cypher_int(intvalue, keyvalue):
    return intvalue ^ keyvalue


def cypher_char(charvalue, keyvalue):
    return chr(cypher_int(ord(charvalue), ord(keyvalue)))


def cypher_str(strvalue, keyvalue):
    return ''.join([cypher_char(c, keyvalue[i % len(keyvalue)])
                    for i, c
                    in enumerate(strvalue)])


def test_str(tstr, keyvalue):
    """Test the equality between a string and its decyphered cypher"""
    lstr = cypher_str(cypher_str(tstr, keyvalue), keyvalue)
    return tstr == lstr


def test_routine(rounds=500, verbose=False):
    """
    Test routine using random ascii letters for R rounds
    """

    if verbose:
        print "Testing {rounds} rounds: ".format(rounds=rounds),

    for x in range(rounds):
        tstr = ''.join([chr(random.randint(0, 255))
                        for y
                        in range(random.randint(50, 250))])

        keyvalue = ''.join([chr(random.randint(0, 255))
                            for y
                            in range(random.randint(50, 250))])

        if not test_str(tstr, keyvalue):
            if verbose:
                print "Failed string {tstr}: ".format(tstr=tstr)
                print "Operation: cypher = clear ^ keyvalue, with "
                print "keyvalue: {keyvalue}".format(keyvalue=keyvalue)
            return False

    return True
