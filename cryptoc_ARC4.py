#!/usr/bin/python

from genutils import smallcap_gen


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
    return intvalue ^ next(keysession)


def cypher_char(charvalue, keysession):
    """Cypher a character according to keysession"""
    return chr(cypher_int(ord(charvalue), keysession))


def cypher_str(strvalue, keysession):
    """Cypher a string according to keysession"""
    return ''.join([cypher_char(c, keysession) for c in strvalue])


def test_routine(rounds=500):
    """
    Test routine using the xmpl_values on random ascii letters for R rounds
    """

    key = smallcap_gen()
    keysession1 = session_init(key_str2intlst(key))
    keysession2 = session_init(key_str2intlst(key))
    for x in range(rounds):
        tstr = smallcap_gen()
        cstr = cypher_str(tstr, keysession1)
        lstr = cypher_str(cstr, keysession2)
        assert tstr == lstr
