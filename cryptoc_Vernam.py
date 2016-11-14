#!/usr/bin/python

import random
import string  # for testing purposes


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


def test_str(tstr, seed):
    """Test the equality between a string and its crafted craft"""
    set_seed(seed)
    cstr = craft_strvalue(tstr)
    set_seed(seed)
    rstr = craft_strvalue(cstr)

    return tstr == rstr


def test_routine(rounds=500, verbose=False):
    """
    Test routine using a random seed on random printable ascii for R rounds
    """
    if verbose:
        print "Testing {rounds} rounds: ".format(rounds=rounds),

    for x in range(rounds):
        seed = random.randint(0, 1024*rounds)
        tstr = ''.join(random.sample(string.printable,
                                     random.randint(40, 90)))

        if not test_str(tstr, seed):
            if verbose:
                print "Failed string {tstr}: ".format(tstr=tstr)
                print "Operation: cypher= clear^maskbit, with"
                print "S: {seed}, as the seed for the mask".format(seed=seed)

            return False

    return True
