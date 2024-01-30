"""
William Dinh
Period 5
Tests functions found in hw1.py
"""
import hw1

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
    Tests count_divisible_digits
    """
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(0, hw1.count_divisible_digits(1, 0))
    assert_equals(5, hw1.count_divisible_digits(96922, 1))
    assert_equals(4, hw1.count_divisible_digits(969220, 2))


def test_is_relatively_prime():
    """
    Tests is_relatively_prime
    """
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(12, 14))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(7, 1))
    assert_equals(False, hw1.is_relatively_prime(8, 24))
    assert_equals(True, hw1.is_relatively_prime(87, 88))


def test_longest_word():
    """
    Test longest_word
    """
    assert_equals('3: Merrily', hw1.longest_word('William\\HW1\\song.txt'))
    # add another test case, prob with 'None'
    # add another test case


def main():
    test_total()
    test_count_divisible_digits()
    test_is_relatively_prime()


if __name__ == '__main__':
    main()
