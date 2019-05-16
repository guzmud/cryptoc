#!/usr/bin/python

import random  # for testing purposes

from genutils import data_gen


def cypher_int(intvalue, keyvalue):
    return intvalue ^ keyvalue


def cypher_char(charvalue, keyvalue):
    return chr(cypher_int(ord(charvalue), ord(keyvalue)))


def cypher_str(strvalue, keyvalue):
    return ''.join([cypher_char(c, keyvalue[i % len(keyvalue)])
                    for i, c
                    in enumerate(strvalue)])


def test_routine(rounds=500):
    """
    Test routine using random ascii letters for R rounds
    """
    for x in range(rounds):
        tstr = data_gen()
        keyvalue = data_gen()
        lstr = cypher_str(cypher_str(tstr, keyvalue), keyvalue)
        assert tstr == lstr
