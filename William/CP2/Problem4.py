"""
Same as problem 1
"""


def fun_numbers(start, stop):
    return [i for i in range(start, stop) if (i % 2 == 0 or i % 5 == 0)]
