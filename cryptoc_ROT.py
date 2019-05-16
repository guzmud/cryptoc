#!/usr/bin/python

import random  # for testing purposes

from genutils import data_gen, element_gen

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


def test_routine(rounds=500):
    """
    Test routine using random ascii letters for R rounds
    """
    for x in range(rounds):
        tstr = data_gen()
        rotvalue = element_gen()
        lstr = uncypher_str(cypher_str(tstr, rotvalue),
                            rotvalue)
        assert tstr == lstr
