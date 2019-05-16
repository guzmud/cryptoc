#!/usr/bin/python

import random  # for testing purposes

from genutils import alphabet_gen


def cypher_el(elvalue, alphabet):
    """Cypher an element according to alphabet"""
    return list(reversed(alphabet))[alphabet.index(elvalue)]


def cypher_lst(lstvalue, alphabet):
    """Cypher a list according to alphabet"""
    return [cypher_el(e, alphabet) for e in lstvalue]


def uncypher_el(elvalue, alphabet):
    """Uncypher an element according to alphabet"""
    return alphabet[list(reversed(alphabet)).index(elvalue)]


def uncypher_lst(lstvalue, alphabet):
    """Uncypher a list according to alphabet"""
    return [uncypher_el(e, alphabet) for e in lstvalue]


def test_routine(rounds=500):
    """
    Test routine using the xmpl_alphabet on random ascii letters for R rounds
    """
    alphabet = alphabet_gen()
    for x in range(rounds):
        tlst = random.sample(alphabet, random.randint(20, 46))
        llst = uncypher_lst(cypher_lst(tlst, alphabet),
                            alphabet)
        assert tlst == llst
