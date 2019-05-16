#!/usr/bin/python

try:
    from math import gcd
except:
    from fractions import gcd

import random  # for testing purposes
import string  # for testing purposes

from affinemaths import xmpl_values
from genutils import data_gen


def coprimes_check(value, modulo):
    """ Return if value and modulo are coprimes or not as a boolean"""
    if gcd(modulo, value) != 1:
        return False
    else:
        return True


def egcd(a, b):
    """Return the egcd for the two provided values"""
    x, y, u, v = 0, 1, 1, 0

    while a != 0:
        q = b // a
        r = b % a
        m = x-u*q
        n = y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n

    return b, x, y


def get_inverse(value, modulo):
    """Return the inverse value according to the modulo in an affine system"""
    if coprimes_check(value, modulo):
        g, x, y = egcd(value, modulo)
        invalue = x % modulo
        return invalue
    else:
        return 0


def cypher_int(intvalue, key, salt, modulo):
    """Cypher an integer value according to key, salt and modulo"""
    return (key*intvalue+salt) % modulo


def cypher_char(charvalue, key, salt, modulo):
    """Cypher a character according to key, salt and modulo"""
    return chr(cypher_int(ord(charvalue), key, salt, modulo))


def cypher_str(strvalue, key, salt, modulo):
    """Cypher a string according to key, salt and modulo"""
    return ''.join([cypher_char(c, key, salt, modulo) for c in strvalue])


def uncypher_int(intvalue, invkey, salt, modulo):
    """Uncypher an integer according to the inverse key, salt and modulo"""
    return invkey*(intvalue - salt) % modulo


def uncypher_char(charvalue, invkey, salt, modulo):
    """Uncypher a character according to the inverse key, salt and modulo"""
    return chr(uncypher_int(ord(charvalue), invkey, salt, modulo))


def uncypher_str(strvalue, invkey, salt, modulo):
    """Uncypher a string according to the inverse key, salt and modulo"""
    return ''.join([uncypher_char(c, invkey, salt, modulo) for c in strvalue])


def test_routine(rounds=500):
    """
    Test routine using the xmpl_values on random ascii letters for R rounds
    """
    affine_values = xmpl_values()
    key = affine_values["key"]
    salt = affine_values["salt"]
    modulo = affine_values["modulo"]
    for x in range(rounds):
        tstr = data_gen()
        lstr = uncypher_str(cypher_str(tstr, key, salt, modulo),
                            get_inverse(key, modulo),
                            salt, modulo)
        assert tstr == lstr
