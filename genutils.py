#!/usr/bin/python

from string import ascii_letters, printable
from random import randint, sample


def seed_gen(rounds=500):
    return randint(0, 1024*rounds)


def alphabet_gen():
    return ascii_letters


def element_gen(offset=0, modulo=256):
    return randint(offset, offset+modulo-1)


def data_gen(offset=0, modulo=256, minsize=20, maxsize=50):
    return ''.join([chr(element_gen(offset, modulo))
                    for y in range(randint(minsize, maxsize))])


def smallcap_gen(minsize=20, maxsize=50):
    return data_gen(offset=97, modulo=26, minsize=minsize, maxsize=maxsize)


def printable_gen(minsize=20, maxsize=50):
    return ''.join(sample(printable, randint(minsize, maxsize)))
