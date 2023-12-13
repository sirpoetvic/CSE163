"""
Don't forget to put your name and information here!
Name: Victor Wong
"""

'''Returns linear interpolation of a and b,
of c
'''


def funky_sum(a, b, mix):
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    else:
        return (1 - mix) * b + mix * a


'''Returns the sum of all numbers from 0 (inclusive) to n (inclusive)'''


def total(n):
    if n < 0:
        return None
    else:
        result = 0
    for i in range(n + 1):
        result += i
    return result
