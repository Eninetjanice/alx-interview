#!/usr/bin/python3
'''Minimum Operations'''

'''def minOperations(n):
    if n <= 0:
        return 0

    operations = 0
    h_count = 1
    clipboard = 0

    while h_count < n:
        if n % h_count == 0 and n // h_count > 1:
            clipboard = h_count
        h_count += clipboard
        operations += 1

        if clipboard > 0:
            clipboard = 0

    if h_count == n:
        return operations
    else:
        return 0
'''


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n /= x
        x += 1
    return result
