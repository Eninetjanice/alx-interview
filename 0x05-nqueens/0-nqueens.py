#!/usr/bin/python3
""" Python program that solves the N queens problem."""

import sys


def is_valid_solution(resolve):
    """ Solution validator """
    for i in range(len(resolve)):
        for j in range(i + 1, len(resolve)):
            if resolve[i] == resolve[j]:
                return False
            if abs(resolve[i] - resolve[j]) == abs(i - j):
                return False
    return True


def solve_n_queens(n, solutions, resolve=[]):
    """ Solve nqueen's problem recursively"""
    if len(resolve) == n:
        if is_valid_solution(resolve):
            solutions.append([[i, resolve[i]] for i in range(n)])
        return
    for i in range(n):
        if i not in resolve:
            new_solution = resolve + [i]
            if is_valid_solution(new_solution):
                solve_n_queens(n, solutions, new_solution)


if __name__ == '__main__':
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
    solve_n_queens(n, solutions)
    for solution in solutions:
        print(solution)
