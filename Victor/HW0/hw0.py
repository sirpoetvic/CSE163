"""
Victor Wong
UW CSE163
Implements the functions for HW0
"""


def funky_sum(a, b, mix):
    """Returns linear interpolation of a and b,
    of c
    """
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    return (1 - mix) * a + mix * b


def total(n):
    """Returns the sum of all numbers from 0 (inclusive) to n (inclusive)"""
    if n < 0:
        return None
    else:
        result = 0
    for i in range(n + 1):
        result += i
    return result


"""Swaps characters c1 and c2 in source, returns source"""


def swip_swap(source, c1, c2):
    result = ""
    for c in source:
        if c == c1:
            result += c2
        elif c == c2:
            result += c1
        else:
            result += c
    return result
