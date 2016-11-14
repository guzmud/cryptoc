#!/usr/bin/python

import random  # for testing purposes
import string  # for testing purposes


def key_str2intlst(keystring):
    return [ord(c) for c in keystring]


def key_scheduling_algorithm(S, key):

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return S


def get_pseudo_random_byte(key):
    
    S = [x for x in range(256)]

    iptr = 0
    jptr = 0
    rptr = 0

    while True:

        if rptr == 0:
            S = key_scheduling_algorithm(S, key)
        rptr = (rptr+1) % 256
        
        iptr = (iptr+1) % 256
        jptr = (jptr+S[iptr]) % 256
        S[iptr], S[jptr] = S[jptr], S[iptr]
        yield S[(S[iptr] + S[jptr]) % 256]


def session_init(key):    
    return get_pseudo_random_byte(key)


def cypher_int(intvalue, keysession):
    """Cypher an integer according to keysession"""
    return intvalue ^ keysession.next()


def cypher_char(charvalue, keysession):
    """Cypher a character according to keysession"""
    return chr(cypher_int(ord(charvalue), keysession))


def cypher_str(strvalue, keysession):
    """Cypher a string according to keysession"""
    return ''.join([cypher_char(c, keysession) for c in strvalue])


def test_str(tstr, keysession1,keysession2):
    """Test the equality between a string and its decyphered cypher"""
    cstr = cypher_str(tstr, keysession1)
    lstr = cypher_str(cstr, keysession2)
    return tstr == lstr


def test_routine(rounds=500, verbose=False):
    """
    Test routine using the xmpl_values on random ascii letters for R rounds
    """

    key = random.sample(string.ascii_letters, random.randint(20, 46))
    keysession1 = session_init(key_str2intlst(key))
    keysession2 = session_init(key_str2intlst(key))
    
    if verbose:
        print "Testing {rounds} rounds: ".format(rounds=rounds),

    for x in range(rounds):
        tstr = ''.join(random.sample(string.ascii_letters,
                                     random.randint(20, 46)))

        if not test_str(tstr, keysession1, keysession2):
            if verbose:
                print "Failed string {tstr}: ".format(tstr=tstr)
                print "Operation: cypher = (clear**pubkey % n), with "
                print "key: {key}".format(key=key)
            return False

    return True
