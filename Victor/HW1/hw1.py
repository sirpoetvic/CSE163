"""
Victor Wong
Period 5
HW1 assignment
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


def count_divisible_digits(n: int, m: int) -> int:
    """
    returns the number of digits in n that are divisible
    by m

    Args:
        n (int): number to examine digits from
        m (int): divisor

    Returns:
        int: number of digits in n divisible by m
    """
    if m == 0:
        return 0
    n, num = abs(n), 0
    while n > 10:
        digit = n % 10
        if (digit % m) == 0:
            num += 1
        n //= 10
    if (n % m) == 0:
        num = num + 1
    return num


def is_relatively_prime(n: int, m: int) -> bool:
    """
    Determines if n and m have a common factor

    Args:
        n (int): number 1
        m (int): number 2

    Returns:
        bool: if n and m do not have a common factor
    """
    if (n == m) or (n == 1) or (m == 1):
        return True
    for i in range(2, int(max(n, m) / 2)):
        if n % i == 0 and m % i == 0:
            return False
    return True


def travel(directions, x, y):
    """
    adjusts (x, y) coordinates based on the string directions.
    "n", "s", "w", and "e" upper/lower are all move the coordinates
    in their respective direction

    Args:
        directions (string): string containing n, s, w, e, and
        other non-adjusting chars
        x (int): x-coordinate
        y (int): y-coordinate

    Returns:
        (x, y): adjusted coordinates
    """
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
    """Reformats the given date, from the current date format to a
    target date format

    Args:
        date (string): a combination of day, year, month, in any order, separated by "/"
        current_date_format (string): a combination of letters D, Y, M, in any order, separated by "/"
        target_date_format (string): a combination of letters D, Y, M, in any order, separated by "/"

    Returns:
        _type_: _description_
    """
    return_date = ""
    date_letters = current_date_format.split("/")
    target_date_letters = target_date_format.split("/")
    date_numbers = date.split("/")

    for i in range(len(target_date_letters)):
        return_date += date_numbers[
            date_letters.index(target_date_letters[i])
        ] + (("/" if i != len(target_date_letters) - 1 else ""))
    return return_date


def longest_word(file_name: str):
    """Finds the longest word in text, and the line that it came from
    Returns None if the file is empty.

    Args:
        file_name (txt file): text file with words on lines

    Returns:
        long_line, long_word: returns line number with longest token
    """
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
    """Returns the average of the numbers from range (low, high) in values
    Inclusive of low, exclusive of high

    Args:
        values (list): list containing ints
        low (int): start of range (inclusive)
        high (int): end of range (exclusive)

    Returns:
        average: average of range
    """
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
    """Returns the digit that appears most frequently in n.
    If there is a tie for the most frequent digit, the digit with the greatest value is returned.

    Args:
        n (int): number

    Returns:
        greatest_num: most common number in n
    """
    t = abs(n)
    greatest_num, occurences_dict, greatest_occurences = 0, {}, 0
    while t > 0:
        if (t % 10) not in occurences_dict.keys():
            occurences_dict[t % 10] = 1
        else:
            occurences_dict[t % 10] += 1
        if occurences_dict[t % 10] > greatest_occurences:
            greatest_num = t % 10
            greatest_occurences = occurences_dict[t % 10]
        elif (
            occurences_dict[t % 10] == greatest_occurences
            and (t % 10) >= greatest_num
        ):
            greatest_num = t % 10
        t //= 10
    return greatest_num
