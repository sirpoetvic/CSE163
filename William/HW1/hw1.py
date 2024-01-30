"""
William Dinh
Period 5
HW1 Assignment from UW in the HS
"""
# do not import math


def total(n):
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def count_divisible_digits(n, m):
    """
    Takes two integer numbers, returns how many digits are divisible by m
    Returns 0 if m is 0, m is a single digit between 0 and 10 inclusive

    Args:
        n (int) = Integer that the digits are drawn from
        m (int) = Integer to divide by
    """
    counter, digits, n = 0, [], abs(n)

    if m == 0 or n == 0:
        return counter

    for digit in str(n):
        digits.append(digit)
        if int(digit) % m == 0:
            counter += 1
    return counter


def is_relatively_prime(n, m):
    """
    Takes two integer numbers n and m
    Returns True if n and m are relatively prime
    Numbers are relatively prime if they share no common factors besides 1
    Do not use data structures to store factors, use a single for loop

    Args:
        n (int) = Integer to test if it is "relatively prime" to n
        m (int) = Integer to test if it is "relatively prime" to m
    """
    for i in range(2, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            return False
    return True


def reformat_date(og_date, mdy, dmy):
    pass


def travel(directions, x, y):
    pass


def longest_word(file_name):
    """
    Returns the longest word in file_name
    Returns None if no words are in the file

    Args:
        file_name (.txt): File to be accessed
    """
    largest_word, largest_length, line_count, largest_linecount = "", 0, 0, 0
    with open(file_name) as file:
        words = file.readlines()

        if words == 0:
            return None

        for word in words:
            line_count += 1
            keys = word.split()
            if keys == 0:
                return None

            for key in keys:
                if len(key) > largest_length:
                    largest_linecount = line_count
                    largest_length = len(key)
                    largest_word = key

    return f"{largest_linecount}: {largest_word}"


def mode_digit(n):
    pass