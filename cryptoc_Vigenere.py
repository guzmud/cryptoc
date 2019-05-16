#!/usr/bin/python

import string  # for testing purposes
import random  # for testing purposes

from genutils import alphabet_gen


def get_key_element(key):
    ptr = 0

    while True:
        yield key[ptr]
        ptr = (ptr + 1) % len(key)


def session_init(key):
    return get_key_element(key)


def cypher_el(elvalue, keysession, alphabet):
    """Cypher an element according to key element value and alphabet"""
    indx = (alphabet.index(elvalue) + alphabet.index(next(keysession))) % len(alphabet)
    return alphabet[indx]


def cypher_lst(lstvalue, keysession, alphabet):
    """Cypher a list according to key element and alphabet"""
    return [cypher_el(e, keysession, alphabet) for e in lstvalue]


def uncypher_el(elvalue, keysession, alphabet):
    """Uncypher an element according to key element value and alphabet"""
    indx = (alphabet.index(elvalue) - alphabet.index(next(keysession))) % len(alphabet)
    return alphabet[indx]


def uncypher_lst(lstvalue, keysession, alphabet):
    """Uncypher a list according to key element and alphabet"""
    return [uncypher_el(e, keysession, alphabet) for e in lstvalue]


def test_routine(rounds=500):
    """
    Test routine using the xmpl_alphabet on random elements for R rounds
    """
    alphabet = alphabet_gen()
    key = random.sample(alphabet,
                        random.randint(20,46))
    keysession1 = session_init(key)
    keysession2 = session_init(key)
    for x in range(rounds):
        tlst = random.sample(alphabet, random.randint(20, 46))
        clst = cypher_lst(tlst, keysession1, alphabet)
        llst = uncypher_lst(clst, keysession2, alphabet)
        assert tlst == llst
