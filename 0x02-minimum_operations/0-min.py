#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n == 1:
        return 0
    operations = {(1, 1): 0}
    queue = [(1, 1)]
    while queue:
        x, y = queue.pop(0)
        if x == n and y == n:
            return operations[(x, y)]
        if (x, 2*x) not in operations:
            operations[(x, 2*x)] = operations[(x, y)] + 1
            queue.append((x, 2*x))
        if (x+y, y) not in operations:
            operations[(x+y, y)] = operations[(x, y)] + 1
            queue.append((x+y, y))
    return 0
