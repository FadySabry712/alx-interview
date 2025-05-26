#!/usr/bin/python3
"""N Queens problem solution for ALX"""
import sys


def is_safe(row, col, queens):
    """Check if a queen can be placed safe pstion"""
    for r, c in queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row=0, queens=[], solutions=[]):
    """Backtracking"""
    if row == n:
        solutions.append(queens.copy())
        return
    for col in range(n):
        if is_safe(row, col, queens):
            queens.append([row, col])
            solve_nqueens(n, row + 1, queens, solutions)
            queens.pop()


def main():
    """parse arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(n, solutions=solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

