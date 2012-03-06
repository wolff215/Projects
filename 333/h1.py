# CSC 333 - Spring 2012 - Homework 1
# Time-stamp: <2012-01-26 10:04:47 shade>

# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return a value, which means that they
# implicitly return None. They all include doctests, which you can
# test by running this file as a script: python h1.py

# Feel free to add your own doctests.

# This makes / always do float division, and turns print into a
# function, both of which are the standard behavior in Python 3.

from __future__ import division, print_function


def tnp1(n):
    """
    The "three N plus 1" sequence starting from a positive integer n
    is defined as follows: if n is 1, stop; if n is odd, the next
    number is 3n+1; if n is even, the next number is n//2. For
    example, here's the sequence starting from 7:

        7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1

    The function tnp1 must return the total length of the sequence
    starting from n, so

    >>> tnp1(7)
    17

    Remember that // performs integer division in Python.
    """
    pass


def poly(cs, x):
    """
    cs is a nonempty list of coefficients. Return the polynomial with
    those coefficients evaluated at x. For example, [2,-5,3.5] defines
    the quadratic 2*x**2 - 5*x + 3.5, so

    >>> poly([2,-5,3.5], 4)
    15.5

    The list can be arbitrarily long, so you can not hardcode a
    formula for every possible degree of polynomial.  Hint: use
    Horner's rule.

    NOTE: you may get slight round-off errors. That's OK.
    """
    pass


def ascend(xs):
    """
    Returns a new sorted list from xs by working left-to-right and
    dropping any element that is less than any of its predecessors in
    the list. Can easily be done in linear time. For example,

    >>> ascend([])
    []
    >>> ascend(list('godfather'))
    ['g', 'o', 't']
    >>> ascend([1,3,2,6,5,6,9,0])
    [1, 3, 6, 6, 9]
    """
    pass


def closest_point(xys):
    """
    Given a list of ordered pairs representing points in the plane,
    return the point that is closest to the origin. If two or more
    points are equally close, return the one that appears earliest in
    the list. If the list is empty, return None. For example,

    >>> closest_point([(1,2),(4,-2),(-0.5,0),(3.14,2)])
    (-0.5, 0)
    """
    pass


def conway(n):
    """
    The mathematician John Conway defined the following sequence:

       [1]                     # one 1
       [1,1]                   # two 1's
       [2,1]                   # one 2, one 1
       [1,2,1,1]               # one 1, one 2, two 1's
       [1,1,1,2,2,1]           # three 1's, two 2's, one 1
       [3,1,2,2,1,1]           # one 3, one 1, two 2's, two 1's
       [1,3,1,1,2,2,2,1]       # ...

    Note that each list after the first describes the previous list.
    Given n, return the nth element of the Conway sequence, where [1]
    is element number 0.

    >>> conway(3)
    [1, 2, 1, 1]

    You'll probably want to write helper functions for this one.
    """
    pass


def count_if(p, xs):
    """
    Returns the number of elements of list xs that satisfy predicate p.

    >>> count_if(lambda x: x > 5, [8,6,7,5,3,0,9])
    4
    >>> count_if(lambda c: c.isupper(), list('Heavy Rain'))
    2
    """
    pass


def find_last(p, xs):
    """
    Returns the last element in list xs that satisfies predicate p. If
    there is no element in xs that satisfies p, it returns None.

    >>> find_last(lambda x: x > 10, [7,3,5,9,9,1,5,3])
    >>> find_last(lambda x: x % 2 == 0, [7,2,5,4,4,1,6,3])
    6
    """
    pass


def conjoin(ps, x):
    """
    Returns True if x satisfies all the predicates in list ps, and
    False otherwise. The list can be any length, including zero.

    >>> conjoin([lambda x: x % 2 == 0, lambda x: x > 6], 10)
    True
    >>> conjoin([lambda x: x % 2 == 0, lambda x: x > 6], 11)
    False
    """
    pass


def fixed_point(f, x0, n=1000):
    """
    A fixed point of function f is a value x such that f(x) is x. Try
    to find a fixed point of f starting with x0: compute f(x0),
    f(f(x0)), f(f(f(x0))), ..., until two successive values are the
    same. If you find a fixed point in at most n steps, return it,
    otherwise return None.

    >>> fixed_point(lambda x: x + 1, 100)
    >>> fixed_point(lambda x: x//2 + 1, 37)
    2
    >>> fixed_point(lambda s: s[2]+s[1]+s[3:]+s[1], 'football')
    'oooooooo'

    Not all functions have fixed points, and not all fixed points can be
    found using this simple technique.
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
