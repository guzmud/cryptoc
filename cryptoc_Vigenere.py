#!/usr/bin/python

import string  # for testing purposes
import random  # for testing purposes


def xmpl_alphabet():
    """ Return a dictionnary with sample value for alphabet"""
    return {"alphabet": string.ascii_letters}


def get_key_element(key):
    ptr = 0

    while True:
        yield key[ptr]
        ptr = (ptr + 1) % len(key)


def session_init(key):
    return get_key_element(key)


def cypher_el(elvalue, keysession, alphabet):
    """Cypher an element according to key element value and alphabet"""
    indx = (alphabet.index(elvalue) + alphabet.index(keysession.next())) % len(alphabet)
    return alphabet[indx]


def cypher_lst(lstvalue, keysession, alphabet):
    """Cypher a list according to key element and alphabet"""
    return [cypher_el(e, keysession, alphabet) for e in lstvalue]


def uncypher_el(elvalue, keysession, alphabet):
    """Uncypher an element according to key element value and alphabet"""
    indx = (alphabet.index(elvalue) - alphabet.index(keysession.next())) % len(alphabet)
    return alphabet[indx]


def uncypher_lst(lstvalue, keysession, alphabet):
    """Uncypher a list according to key element and alphabet"""
    return [uncypher_el(e, keysession, alphabet) for e in lstvalue]


def test_lst(tlst, keysession1, keysession2, alphabet):
    """Test the equality between a list and its decyphered cypher"""
    clst = cypher_lst(tlst, keysession1, alphabet)
    llst = uncypher_lst(clst, keysession2, alphabet)
    return tlst == llst


def test_routine(rounds=500, verbose=False):
    """
    Test routine using the xmpl_alphabet on random elements for R rounds
    """
    alphabet = xmpl_alphabet()["alphabet"]
    
    key = random.sample(alphabet,
                        random.randint(20,46))
    
    keysession1 = session_init(key)
    keysession2 = session_init(key)
    
    if verbose:
        print "Testing {rounds} rounds: ".format(rounds=rounds),

    for x in range(rounds):
        tlst = random.sample(alphabet, random.randint(20, 46))

        if not test_lst(tlst, keysession1, keysession2, alphabet):
            if verbose:
                print "Failed list {tlst}: ".format(tlst=tlst)
                print "With key: {key}".format(key=key)
                print "alphabet: {alphabet}".format(alphabet=alphabet)
            return False

    return True
