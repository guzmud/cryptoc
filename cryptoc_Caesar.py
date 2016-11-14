#!/usr/bin/python

import random  # for testing purposes


def xmpl_alphabet():
    """ Return a dictionnary with sample value for alphabet"""
    import string
    return {"alphabet": string.ascii_letters}


def rectify_shift(shift, alphabet):
    return shift % len(alphabet)


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


def test_lst(tlst, shift, alphabet):
    """Test the equality between a list and its decyphered cypher"""
    llst = uncypher_lst(cypher_lst(tlst, shift, alphabet),
                        shift, alphabet)
    return tlst == llst


def test_routine(rounds=500, verbose=False):
    """
    Test routine using the xmpl_alphabet on random elements for R rounds
    """
    alphabet = xmpl_alphabet()["alphabet"]
    
    if verbose:
        print "Testing {rounds} rounds: ".format(rounds=rounds),

    for x in range(rounds):
        shift = random.randint(0, len(alphabet)*3)
        shift = rectify_shift(shift, alphabet)
        tlst = random.sample(alphabet, random.randint(20, 46))

        if not test_lst(tlst, shift, alphabet):
            if verbose:
                print "Failed list {tlst}: ".format(tlst=tlst)
                print "With shift: {shift}".format(shift=shift)
                print "alphabet: {alphabet}".format(alphabet=alphabet)
            return False

    return True
