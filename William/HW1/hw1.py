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
    counter, n_abs = 0, abs(n)

    if (m == 0) or (n == 0):
        return counter

    while n_abs > 0:
        digit = n_abs % 10
        if digit % m == 0 or digit == 0:
            counter += 1
        n_abs //= 10
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


def travel(directions, x, y):
    """
    Returns a tuple of the position in format (x_new, y_new)
    Args:
        directions (String): Directions given in N E S W
        x (int): starting position x
        y (int): starting position y
    """
    x_new, y_new = x, y
    for i in range(len(directions)):
        if directions[i].lower() == "n":
            y_new += 1
        elif directions[i].lower() == "e":
            x_new += 1
        elif directions[i].lower() == "s":
            y_new -= 1
        elif directions[i].lower() == "w":
            x_new -= 1
    return (x_new, y_new)


def reformat_date(given_date, current_date, target_date):
    """
    Returns a date, reformatted to a target format

    Args:
        given_date (String): date that is given
        current_date (String): format of the date given
        target_date (String): what to change the format of the date to
    """
    date_split = given_date.split("/")
    current_date_split = current_date.split("/")
    target_date_split = target_date.split("/")
    result_date, result_date_parts = "", []

    for target_part in target_date_split:
        index_in_current = current_date_split.index(target_part)
        result_date_parts.append(date_split[index_in_current])

    result_date = result_date_parts[0]
    for part in result_date_parts[1:]:
        result_date += "/" + part

    return result_date


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

        if len(words) == 0:
            return None

        for word in words:
            line_count += 1
            keys = word.split()
            if len(keys) == 0:
                return None

            for key in keys:
                if len(key) > largest_length:
                    largest_linecount = line_count
                    largest_length = len(key)
                    largest_word = key

    return f"{largest_linecount}: {largest_word}"


def get_average_in_range(int_list, low, high):
    """
    Takes a list of integers, returns the average of all values in the list
    Range from low (inclusive) to high (exclusive)
    Args:
        int_list (list of Integers):
        low (int):
        high (int):
    """
    range_list = []
    for i in int_list:
        if i >= low and i < high:
            range_list.append(i)
    if len(range_list) == 0:
        return 0
    return sum(range_list)/len(range_list)


def mode_digit(n):
    """
    Takes int n, returns the digit that appears most frequently in the number
    Digit returned MUST be positive.
    Do not create strings in any way to solve any part of the problem.
    Do not use any nested loops or recursion.
    Do not use an if, elif, or else branch for each digit.

    Args:
        n (int): positive or negative number
    """
    digit_list, digit_counts, most_word, most_word_val = [], {}, 0, 0
    n = abs(n)

    while n != 0:
        digit_list.append(n % 10)
        n //= 10

    for digit in digit_list:
        if digit in digit_counts:
            digit_counts[digit] += 1
        else:
            digit_counts[digit] = 1

        if digit_counts[digit] > most_word_val:
            most_word = digit
            most_word_val = digit_counts[digit]

    return most_word
