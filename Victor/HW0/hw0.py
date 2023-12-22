"""
Victor Wong
UW CSE163
Implements the functions for HW0
"""
'''Returns linear interpolation of a and b,
of c
'''


def funky_sum(a, b, mix):
    return (1 - mix) * a + mix * b


'''Returns the sum of all numbers from 0 (inclusive) to n (inclusive)'''


def total(n):
    if n < 0:
        return None
    else:
        result = 0
    for i in range(n + 1):
        result += i
    return result


'''Swaps characters c1 and c2 in source, returns source'''


def swip_swap(source, c1, c2):
    result = ''
    for c in source:
        if c == c1:
            result += c2
        elif c == c2:
            result += c1
        else:
            result += c
    return result
