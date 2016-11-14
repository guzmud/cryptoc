#!/usr/bin/python

import random  # for testing purposes
import string  # for testing purposes


def modular_multiplicative_inverse(a, b):
    """
    Return the modular multiplicative inverse using the extended Euclide.
    Warning: this function assumes there is one to be found.
    """

    if a != 0:
        R, x0, x1, y0, y1 = 0, 1, 0, 0, 1
        U, V = a, b
        while R != 1:
            Q = U//V
            R = U-(Q*V)
            x0, x1 = x1, x0-(Q*x1)
            y0, y1 = y1, y0-(Q*y1)
            U, V = V, R
        return x1 % b

    else:
        return 0


def xmpl_values():
    """Return a dictionnary with sample values for n, pubkey and privkey"""

    p = 263
    q = 271
    n = p*q
    totient = (p-1)*(q-1)
    e = 281
    d = modular_multiplicative_inverse(e, totient)

    return {"n": n,
            "pubkey": e,
            "privkey": d}


def cypher_int(intvalue, pubkey, n):
    """Cypher an integer according to pubkey and n"""
    return pow(intvalue, pubkey, n)


def cypher_char(charvalue, pubkey, n):
    """Cypher a character according to pubkey and n. Return an integer."""
    return cypher_int(ord(charvalue), pubkey, n)


def cypher_str(strvalue, pubkey, n):
    """Cypher a string according to pubkey and n. Return a list of integers."""
    return [cypher_char(c, pubkey, n) for c in strvalue]


def uncypher_int(intvalue, privkey, n):
    """Uncypher an integer according to privkey and n"""
    return pow(intvalue, privkey, n)


def uncypher_el(elvalue, privkey, n):
    """Uncypher an element according to privkey and n. Return a char."""
    return chr(uncypher_int(elvalue, privkey, n))


def uncypher_lst(lstvalue, privkey, n):
    """Uncypher a list according to privkey and n. Return a string."""
    return ''.join([uncypher_el(e, privkey, n) for e in lstvalue])


def test_str(tstr, pubkey, privkey, n):
    """Test the equality between a string and its decyphered cypher"""
    lstr = uncypher_lst(cypher_str(tstr, pubkey, n),
                        privkey, n)
    return tstr == lstr


def test_routine(rounds=500, verbose=False):
    """
    Test routine using the xmpl_values on random ascii letters for R rounds
    """
    n = xmpl_values()["n"]
    pubkey = xmpl_values()["pubkey"]
    privkey = xmpl_values()["privkey"]
    if verbose:
        print "Testing {rounds} rounds: ".format(rounds=rounds),

    for x in range(rounds):
        tstr = ''.join(random.sample(string.ascii_letters,
                                     random.randint(20, 46)))

        if not test_str(tstr, pubkey, privkey, n):
            if verbose:
                print "Failed string {tstr}: ".format(tstr=tstr)
                print "Operation: cypher = (clear**pubkey % n), with"
                print "n: {n}; pubkey: {pubkey};".format(n=n, pubkey=pubkey)
                print "privkey: {privkey}".format(privkey=privkey)
            return False

    return True
