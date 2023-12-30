"""
<name>
<period>
<file description>
"""
# do not import math


from itertools import count


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
    if m == 0 or n == 0:
        return 0
    n = abs(n)
    if (n % 10) % m == 0:
        return count_divisible_digits(n // 10, m) + 1
    else:
        return count_divisible_digits(n // 10, m)


def is_relatively_prime(n, m):
    """Determines if n and m have a common factor

    Args:
        n (int): number 1
        m (int): number 2

    Returns:
        boolean: if n and m do not have a common factor
    """
    for i in range(2, int(max(n, m) / 2)):
        if n % i == 0 and m % i == 0:
            return False
    return True


def travel(directions, x, y):
    for i in directions.lower():
        if i == "n":
            y += 1
        elif i == "s":
            y -= 1
        elif i == "e":
            x += 1
        elif i == "w":
            x -= 1
    return (x, y)


def reformat_date(date, current_date_format, target_date_format):
    return_date = ""
    date_letters = current_date_format.split("/")
    target_date_letters = target_date_format.split("/")
    date_numbers = date.split("/")

    for i in range(len(target_date_letters)):
        return_date += date_numbers[date_letters.index(target_date_letters[i])] + (
            ("/" if i != len(target_date_letters) - 1 else "")
        )
    return return_date


def longest_word(file_name):
    long_line, long_word, long_word_length = 0, "", 0
    with open(file_name) as f:
        lines = f.readlines()
        if len(lines) == 0:
            return None
        for line in enumerate(lines):
            tokens = line[1].split(" ")
            for token in tokens:
                if len(token) > long_word_length:
                    long_line = line[0] + 1
                    long_word_length = len(token)
                    long_word = token
    return f"{long_line}: {long_word}"


def get_average_in_range(values, low, high):
    if len(values) == 0:
        return 0
    total_values, num_nums = 0, 0
    for i in values:
        if i >= low and i < high:
            total_values += i
            num_nums += 1
    if num_nums == 0:
        return 0
    return total_values / num_nums


def mode_digit(n):
    greatest_num, occurences_dict, greatest_occurences = n % 10, {}, 0
    n %= 10
    while n > 0:
        if n % 10 not in occurences_dict.keys():
            occurences_dict[n % 10] = 1
            n %= 10
        else:
            occurences_dict[n % 10] += 1
            if occurences_dict[n % 10] > greatest_occurences and n % 10 > greatest_num:
                greatest_num = n % 10
                n %= 10
    return greatest_num
