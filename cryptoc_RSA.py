#!/usr/bin/python

from genutils import data_gen
from rsamaths import xmpl_values


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


def test_routine(rounds=500):
    """
    Test routine using the xmpl_values on random ascii letters for R rounds
    """
    rsa_values = xmpl_values()
    n = rsa_values["n"]
    pubkey = rsa_values["pubkey"]
    privkey = rsa_values["privkey"]
    for x in range(rounds):
        tstr = data_gen()
        lstr = uncypher_lst(cypher_str(tstr, pubkey, n),
                            privkey, n)
        assert tstr == lstr
