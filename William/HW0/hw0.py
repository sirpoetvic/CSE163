"""
HW0 - CSE 163
William Dinh
Includes functions funky_sum, total, and swip_swap
"""


def funky_sum(a, b, mix):
    """
    Function that combines two numbers, after a ratio is applied
    If mix is 0 or less, the result should be the same as a
    If mix is 1 or more, the result should be the same as b
    For any value of mix between 0 and 1, it should add 1-mix * a and mix * b

    Args:
        a (any numeric type)
        b (any numeric type)
        mix (any numeric type):
        A number to determine the ratio from a and b
        Described as a "slider" for how much to use a and b
    """
    if mix < 0:
        return a
    elif mix >= 1:
        return b
    elif 0 <= mix <= 1:
        # Getting a floating value error, so im going to round it using round()
        round_num = (1-mix) * a + mix * b
        return round(round_num, ndigits=2)


def total(n):
    """
    Returns the sum of the integers from 0 (inclusive) to n (inclusive)
    If n is negative, the function should return the value None instead

    Args:
        n (int): number to manipulate
    """
    total = 0
    if n < 0:
        return "None"
    else:
        for i in range(n+1):
            total = i + total
        return total


def swip_swap(source, c1, c2):
    """
    Takes a string source and characters c1 and c2
    Returns a copy of source with all occurrences of c1 and c2 swapped
    Assume c1 and c2 are single characters
    Use string concatenation with the + operator

    Args:
        source (str): number to return, based on c1 and c2
        c1 (char)
        c2 (char)
    """
    str_together = ''
    for i in source:
        if i == c1:
            str_together += c2
        elif i == c2:
            str_together += c1
        else:
            str_together += i
    return str_together
