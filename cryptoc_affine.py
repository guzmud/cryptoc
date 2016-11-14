#!/usr/bin/python

import fractions
import random  # for testing purposes
import string  # for testing purposes


def xmpl_values():
    """ Return a dictionnary with sample values for modulo, key and salt"""
    return {"modulo": 256,
            "key": 11,
            "salt": 7}


def test_coprimes(value, modulo):
    """ Return if value and modulo are coprimes or not as a boolean"""
    if (fractions.gcd(modulo, value) != 1):
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
    if test_coprimes(value, modulo):
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


def test_str(tstr, key, salt, modulo):
    """Test the equality between a string and its decyphered cypher"""
    lstr = uncypher_str(cypher_str(tstr, key, salt, modulo),
                        get_inverse(key, modulo),
                        salt, modulo)
    return tstr == lstr


def test_routine(rounds=500, verbose=False):
    """
    Test routine using the xmpl_values on random ascii letters for R rounds
    """
    key = xmpl_values()["key"]
    salt = xmpl_values()["salt"]
    modulo = xmpl_values()["modulo"]
    if verbose:
        print "Testing {rounds} rounds: ".format(rounds=rounds),

    for x in range(rounds):
        tstr = ''.join(random.sample(string.ascii_letters,
                                     random.randint(20, 46)))

        if not test_str(tstr, key, salt, modulo):
            if verbose:
                print "Failed string {tstr}: ".format(tstr=tstr)
                print "Operation: cypher = (K*clear + S) % M, with"
                print "K: {key}; S: {salt}; M: {modulo}".format(key=key,
                                                                salt=salt,
                                                                modulo=modulo)
            return False

    return True
