#!/usr/bin/python3
""" pyhton coding challenge using a bunch of different concepts like prime factorization, greedy algorithms and so on 
"""


def minOperations(n):
    """ calculates the fewest number of operations needed to result in exactly n H characters in the file. """

    if n <= 1:
        return (0)
    operation = 0
    divider = 2

    while n > 1:
        while n % divider == 0:
            operation += divider
            n //= divider
        divider += 1
    return operation
