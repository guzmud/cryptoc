#!/usr/bin/python

import random


def xmpl_book():
    """ Return a dictionnary with sample value for book"""
    from this import d, s
    book = "".join([d.get(c, c) for c in s]).lower().split('\n')
    book = [k for k in book if k]
    return {"book": book}


def get_occurences(value, source):
    """
    Find all occurences of char in sequence source; return list of couples
    """
    occurences = []
    for b in range(len(source)):
        block = source[b]
        pos = block.find(value)
        while pos != -1:
            occurences += [(b, pos),]
            pos = block.find(value, pos+1)
    return occurences


def cypher_char(charvalue, book):
    """Cypher a char according to book"""
    return random.choice(get_occurences(charvalue, book))


def cypher_str(strvalue, book):
    """Cypher a string according to book"""
    return [cypher_char(c, book) for c in strvalue]


def uncypher_el(elvalue, book):
    """Uncypher an element according to book"""
    return book[elvalue[0]][elvalue[1]]


def uncypher_lst(lstvalue, book):
    """Uncypher a list according to book"""
    return ''.join([uncypher_el(e, book) for e in lstvalue])


def test_routine(rounds=500):
    """
    Test routine using the xmpl_book on random elements for R rounds
    """
    book = xmpl_book()["book"]
    for x in range(rounds):
        tstr = ''.join(random.sample(''.join(book), random.randint(20, 46)))
        lstr = uncypher_lst(cypher_str(tstr, book),
                            book)
        assert tstr == lstr
