#!/usr/bin/python

import random

from genutils import data_gen, seed_gen


def set_seed(seed):
    """Set the seed that will be used to generate the binary mask"""
    random.seed(seed)


def get_maskbit():
    """Return one bit of the binary mask"""
    return bin(random.getrandbits(1))[2:]


def craft_bit(bitvalue):
    """Return an xOR between the bitvalue and maskbit (a crafted bit)"""
    return int(bitvalue) ^ int(get_maskbit())


def craft_charbyte(charbyte):
    """Return a crafted character"""
    return chr(int(''.join([str(craft_bit(o))
                            for o
                            in bin(ord(charbyte))[2:].zfill(8)]),
                   2))


def craft_strvalue(strvalue):
    """Return a crafted string"""
    return ''.join([craft_charbyte(c) for c in strvalue])


def test_routine(rounds=500):
    """
    Test routine using a random seed on random printable ascii for R rounds
    """
    for x in range(rounds):
        seed = seed_gen()
        tstr = data_gen()
        set_seed(seed)
        cstr = craft_strvalue(tstr)
        set_seed(seed)
        rstr = craft_strvalue(cstr)
        assert tstr == rstr
