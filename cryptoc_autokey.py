#!/usr/bin/python

import string
import random  # for testing purposes


_AUTOKEY_BUFFER = list()


def autokey_buffer_get():
    global _AUTOKEY_BUFFER
    return _AUTOKEY_BUFFER.pop(0)


def autokey_buffer_post(k):
    global _AUTOKEY_BUFFER
    _AUTOKEY_BUFFER.append(k)


def autokey_buffer_reset():
    global _AUTOKEY_BUFFER
    _AUTOKEY_BUFFER = list()


def init_autokey_buffer(key):
    """ Autokey buffer init according to key"""
    autokey_buffer_reset()
    for k in key:
        autokey_buffer_post(k)


def xmpl_alphabet():
    """ Return a dictionnary with sample value for alphabet"""
    return {"alphabet": string.ascii_letters}


def cypher_el(elvalue, alphabet):
    """Cypher an element according to alphabet (plus internal buffer)"""
    indx = (alphabet.index(elvalue) + alphabet.index(autokey_buffer_get())) % len(alphabet)
    autokey_buffer_post(elvalue)
    return alphabet[indx]


def cypher_lst(lstvalue, alphabet):
    """Cypher a list according to alphabet"""
    return [cypher_el(e, alphabet) for e in lstvalue]


def uncypher_el(elvalue, alphabet):
    """Uncypher an element according to alphabet (plus internal buffer)"""
    indx = (alphabet.index(elvalue) - alphabet.index(autokey_buffer_get())) % len(alphabet)
    autokey_buffer_post(alphabet[indx])
    return alphabet[indx]


def uncypher_lst(lstvalue, alphabet):
    """Uncypher a list according to shift and alphabet"""
    return [uncypher_el(e, alphabet) for e in lstvalue]


def test_lst(tlst, key, alphabet):
    """Test the equality between a list and its decyphered cypher"""
    init_autokey_buffer(key)
    clst = cypher_lst(tlst, alphabet)
    init_autokey_buffer(key)
    llst = uncypher_lst(clst, alphabet)
    autokey_buffer_reset()
    return tlst == llst


def test_routine(rounds=500, verbose=False):
    """
    Test routine using the xmpl_alphabet on random elements for R rounds
    """
    alphabet = xmpl_alphabet()["alphabet"]
    
    key = random.sample(alphabet,
                        random.randint(5,15))
    
    if verbose:
        print "Testing {rounds} rounds: ".format(rounds=rounds),

    for x in range(rounds):
        tlst = random.sample(alphabet, random.randint(20, 46))

        if not test_lst(tlst, key, alphabet):
            if verbose:
                print "Failed list {tlst}: ".format(tlst=tlst)
                print "With key: {key}".format(key=key)
                print "alphabet: {alphabet}".format(alphabet=alphabet)
            return False

    return True
