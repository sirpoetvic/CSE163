"""
Victor Wong
UW CSE163
Implements the functions for HW0
"""


def funky_sum(a: float, b: float, mix: float) -> float:
    """
    returns the linear interpolation of a, b, and c
    a - min
    b - max
    c - ratio of each

    Args:
        a (float): _description_
        b (float): _description_
        mix (float): _description_

    Returns:
        float: linear interpolation result
    """
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    return (1 - mix) * a + mix * b


def total(n: int):
    """
    Returns the sum of all numbers from 0 (inclusive) to n (inclusive)

    Args:
        n (int): max number for sum
    """
    if n < 0:
        return None
    else:
        result = 0
    for i in range(n + 1):
        result += i
    return result


def swip_swap(source, c1, c2):
    """
    Swaps characters c1 and c2 in source, returns source

    Args:
        source (str): target string
        c1 (char): character to be swapped with c2
        c2 (char): character to be swapped with c1
    Returns:
        str: string after swaps
    """
    result = ""
    for c in source:
        if c == c1:
            result += c2
        elif c == c2:
            result += c1
        else:
            result += c
    return result
