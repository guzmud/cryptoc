#!/usr/bin/python

import string
import random  # for testing purposes

from genutils import alphabet_gen


def cipher_alphabet(key, alphabet):
    """Generate the cipher alphabet from the key and the original alphabet"""
    keylphabet = list()

    for k in key:
        if k not in keylphabet:
            keylphabet.append(k)

    for a in alphabet:
        if a not in keylphabet:
            keylphabet.append(a)

    return keylphabet


def cypher_el(elvalue, keylphabet, alphabet):
    """Cypher an element according to keylphabet and alphabet"""
    return keylphabet[alphabet.index(elvalue)]


def cypher_lst(lstvalue, keylphabet, alphabet):
    """Cypher a list according to keylphabet and alphabet"""
    return [cypher_el(e, keylphabet, alphabet) for e in lstvalue]


def uncypher_el(elvalue, keylphabet, alphabet):
    """Uncypher an element according to keylphabet and alphabet"""
    return alphabet[keylphabet.index(elvalue)]


def uncypher_lst(lstvalue, keylphabet, alphabet):
    """Uncypher a list according to keylphabet and alphabet"""
    return [uncypher_el(e, keylphabet, alphabet) for e in lstvalue]


def test_routine(rounds=500):
    """
    Test routine using the xmpl_alphabet on random elements for R rounds
    """
    alphabet = alphabet_gen()
    key = random.sample(alphabet,
                        random.randint(5,15))
    keylphabet = cipher_alphabet(key, alphabet)
    for x in range(rounds):
        tlst = random.sample(alphabet, random.randint(20, 46))
        llst = uncypher_lst(cypher_lst(tlst, keylphabet, alphabet),
                            keylphabet, alphabet)
        assert tlst == llst
