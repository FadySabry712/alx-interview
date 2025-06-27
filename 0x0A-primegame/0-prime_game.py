#!/usr/bin/python3
"""
A solution to the Prime Game problem
"""


def primes(n):
    """Return list of prime numbers between 1 and n
       Args:
        n (int): upper boundary of range.
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determine winner of Prime Game
    Args:
        x (int): no. of rounds
        nums (int): upper limit of range
    Return:
        Name of winner (Maria or Ben) or None
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
