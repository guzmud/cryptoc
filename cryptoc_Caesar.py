#!/usr/bin/python

from random import randint, sample

from genutils import alphabet_gen, element_gen, data_gen


def cypher_el(elvalue, shift, alphabet):
    """Cypher an element according to shift and alphabet"""
    return alphabet[(alphabet.index(elvalue) + shift) % len(alphabet)]


def cypher_lst(lstvalue, shift, alphabet):
    """Cypher a list according to shift and alphabet"""
    return [cypher_el(e, shift, alphabet) for e in lstvalue]


def uncypher_el(elvalue, shift, alphabet):
    """Uncypher an element according to shift and alphabet"""
    return alphabet[(alphabet.index(elvalue) - shift) % len(alphabet)]


def uncypher_lst(lstvalue, shift, alphabet):
    """Uncypher a list according to shift and alphabet"""
    return [uncypher_el(e, shift, alphabet) for e in lstvalue]


def test_routine(rounds=500):
    """
    Test routine using the xmpl_alphabet on random elements for R rounds
    """
    alphabet = alphabet_gen()
    for x in range(rounds):
        shift = element_gen()
        tlst = sample(alphabet, randint(5,15))
        llst = uncypher_lst(cypher_lst(tlst, shift, alphabet),
                            shift, alphabet)
        assert tlst == llst
