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
    # my test
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
    # my test
    assert_equals(False, hw1.is_relatively_prime(8, 24))
    assert_equals(True, hw1.is_relatively_prime(87, 88))


def test_travel():
    """
    Tests travel
    """
    assert_equals((-1, 4), hw1.travel("NW!ewnW", 1, 2))
    # my test
    assert_equals((2, 5), hw1.travel("nsxxwe!enW", 2, 4))
    assert_equals((0, 0), hw1.travel("SsEeNnWw", 0, 0))


def test_reformat_date():
    """
    Tests refortmat_date
    """
    assert_equals('31/12/1998',
                  hw1.reformat_date("12/31/1998", "M/D/Y", "D/M/Y"))
    assert_equals('3/1/2', hw1.reformat_date("1/2/3", "M/D/Y", "Y/M/D"))
    assert_equals('4/0', hw1.reformat_date("0/2000/4", "Y/D/M", "M/Y"))
    assert_equals('2', hw1.reformat_date("3/2", "M/D", "D"))
    # add another test case
    # add anohter test case


def test_longest_word():
    """
    Tests longest_word
    """
    assert_equals('3: Merrily,', hw1.longest_word('William\\HW1\\song.txt'))
    # add another test case, prob with 'None'
    # add another test case


def test_get_average_in_range():
    """
    Tests get_average_in_range()
    """
    assert_equals(5.5, hw1.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    assert_equals(2.0, hw1.get_average_in_range([1, 2, 3], -1, 10))
    assert_equals(2.0, hw1.get_average_in_range([1, 2, 3], -1, 10))
    # my test
    assert_equals(0, hw1.get_average_in_range([], 1, 5))
    assert_equals(0, hw1.get_average_in_range([1, 2, 3], 5, 8))


def test_mode_digit():
    """
    Tests mode_digit
    """
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))
    # my test
    assert_equals(5, hw1.mode_digit(5555545111))
    assert_equals(3, hw1.mode_digit(333334377733))


def main():
    """
    Running all the testing functions
    """
    test_total()
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_reformat_date()
    test_longest_word()
    test_get_average_in_range()
    test_mode_digit()


if __name__ == '__main__':
    main()
