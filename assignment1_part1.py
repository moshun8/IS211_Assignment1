#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Part 1"""


def listDivide(numbers, divide=2):
    '''
    Returns number of items in a list
    divisible by the divide parameter
    '''
    counter = 0
    for num in numbers:
        if num % divide == 0:
            counter += 1
    return counter


class ListDivideException(Exception):
    pass


def testListDivide():
    '''
    Tests function listDivide
    '''
    try:
        assert listDivide([1, 2, 3, 4, 5]) == 2, '1st'
        assert listDivide([2, 4, 6, 8, 10]) == 5, '2nd'
        assert listDivide([30, 54, 63, 98, 10], divide=10) == 2, '3rd'
        assert listDivide([]) == 0, '4th'
        assert listDivide([1, 2, 3, 4, 5], divide=1) == 5, '5th'
        # assert listDivide([1, 2, 3, 4, 5],0) == 2, 'test'
    except:
        raise ListDivideException

if __name__ == "__main__":
    testListDivide()