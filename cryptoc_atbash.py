#!/usr/bin/python

import random  # for testing purposes


def xmpl_alphabet():
    """ Return a dictionnary with sample value for alphabet"""
    import string
    return {"alphabet": string.ascii_letters}


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


def test_lst(tlst, alphabet):
    """Test the equality between a list and its decyphered cypher"""
    llst = uncypher_lst(cypher_lst(tlst, alphabet),
                        alphabet)
    return tlst == llst


def test_routine(rounds=500, verbose=False):
    """
    Test routine using the xmpl_alphabet on random ascii letters for R rounds
    """
    alphabet = xmpl_alphabet()["alphabet"]
    
    if verbose:
        print "Testing {rounds} rounds: ".format(rounds=rounds),

    for x in range(rounds):
        tlst = random.sample(alphabet, random.randint(20, 46))

        if not test_lst(tlst, alphabet):
            if verbose:
                print "Failed list {tlst}: ".format(tlst=tlst)
                print "Alphabet: {alphabet}".format(alphabet=alphabet)
            return False

    return True
