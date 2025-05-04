#!/usr/bin/python3
""" coding challenge using different concepts like prime factorization """


def minOperations(n):
    """ calculates the fewest num to result in exactly n H of characters """

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
