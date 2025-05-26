#!/usr/bin/python3
"""N Queens problem Solution"""
import sys


def is_safe(row, col, queens):
    """Check if a queen can be placed at a safe postion"""
    for r, c in queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve(row, n, queens, solutions):
    """Recursive backtracking for queens placement"""
    if row == n:
        solutions.append(queens[:])
        return
    for col in range(n):
        if is_safe(row, col, queens):
            queens.append([row, col])
            solve(row + 1, n, queens, solutions)
            queens.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve(0, n, [], solutions)
    for sol in solutions:
        print(sol)

