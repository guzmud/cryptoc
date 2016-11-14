#!/usr/bin/python

import random


def xmpl_book():
    """ Return a dictionnary with sample value for book"""
    from this import d, s
    book = filter(None,
                  "".join([d.get(c, c) for c in s]).lower().split('\n'))
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


def test_str(tstr, book):
    """Test the equality between a string and its decyphered cypher"""
    lstr = uncypher_lst(cypher_str(tstr, book),
                        book)
    return tstr == lstr


def test_routine(rounds=500, verbose=False):
    """
    Test routine using the xmpl_book on random elements for R rounds
    """
    book = xmpl_book()["book"]
    
    if verbose:
        print "Testing {rounds} rounds: ".format(rounds=rounds),

    for x in range(rounds):
        tstr = ''.join(random.sample(''.join(book), random.randint(20, 46)))

        if not test_str(tstr, book):
            if verbose:
                print "Failed string {tstr}: ".format(tstr=tstr)
                print "With book: {book}".format(book=book)
            return False

    return True
