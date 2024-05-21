"""
Victor Wong
Period 5
HW1 assignment tester file
"""

import Victor.HW1.hw1 as hw1

from cse163_utils import assert_equals


def test_total():
    """
    Tests the total method
    """
    # The regular case
    assert_equals(15, hw1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw1.total(1))
    assert_equals(0, hw1.total(0))

    # Test the None case
    assert_equals(None, hw1.total(-1))


def test_count_divisible_digits():
    """
    Tests the count_divisible_digits method
    """
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(0, hw1.count_divisible_digits(1, 0))
    assert_equals(4, hw1.count_divisible_digits(100002, 5))
    assert_equals(5, hw1.count_divisible_digits(200000543534543543534, 7))


def test_is_relatively_prime():
    """
    Tests the is_relatively_prime method
    """
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(12, 14))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))
    assert_equals(False, hw1.is_relatively_prime(2, 6))
    assert_equals(True, hw1.is_relatively_prime(1, 5))


def test_travel():
    """
    Tests the travel method
    """
    assert_equals((-1, 4), hw1.travel("NW!ewnW", 1, 2))
    assert_equals((0, 0), hw1.travel("eeeewwwwnnnnssss", 0, 0))
    assert_equals((1, -4), hw1.travel("jfkld;ajkfl;", 1, -4))


def test_reformat_date():
    """
    Tests the reformat_date method
    """
    assert_equals(
        "31/12/1998", hw1.reformat_date("12/31/1998", "M/D/Y", "D/M/Y")
    )
    assert_equals("4/2000", hw1.reformat_date("0/2000/4", "D/Y/M", "M/Y"))
    assert_equals("2", hw1.reformat_date("3/2", "M/D", "D"))


def test_longest_word():
    """
    Tests the longest_word method
    """
    assert_equals(
        "3: Merrily,",
        hw1.longest_word("song.txt"),
    )


def test_get_average_in_range():
    """
    Tests the get_average_in_range method
    """
    assert_equals(5.5, hw1.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    assert_equals(2.0, hw1.get_average_in_range([1, 2, 3], -1, 10))
    assert_equals(0, hw1.get_average_in_range([0, 0, 0, 0, 0, 0, 0], -1, 10))
    assert_equals(0, hw1.get_average_in_range([1, 1, 1], 2, 10))


def test_mode_digit():
    """
    Tests the mode_digit method
    """
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))


def main():
    """
    Runs all test methods (main)
    """
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_reformat_date()
    test_longest_word()
    test_get_average_in_range()
    test_mode_digit()


if __name__ == "__main__":
    main()
