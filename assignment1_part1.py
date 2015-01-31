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
    if listDivide([1, 2, 3, 4, 5]) == 2:
        pass
    else:
        raise ListDivideException
    if listDivide([2, 4, 6, 8, 10]) == 5:
        pass
    else:
        raise ListDivideException
    if listDivide([30, 54, 63, 98, 10], divide=10) == 2:
        pass
    else:
        raise ListDivideException
    if listDivide([]) == 0:
        pass
    else:
        raise ListDivideException
    if listDivide([1, 2, 3, 4, 5], divide=1) == 5:
        pass
    else:
        raise ListDivideException

if __name__ == "__main__":
    testListDivide()