"""
Implements the functions for HW0 to test
Remember to import all modules/functions when testing!
"""

import hw0

"""
Note to William: Reformat to assert_equals() formatting
"""


def test_funky_sum():
    # Makes at least 4 calls to assert_equals
    # At least two calls should be examples shown in the specification
    # At least two should be new examples you make up
    assert hw0.funky_sum(1, 3, 0.5) == 2.0
    assert hw0.funky_sum(1, 3, 0) == 1
    assert hw0.funky_sum(1, 3, 0.25) == 1.5
    assert hw0.funky_sum(1, 3, 0.6) == 2.2
    assert hw0.funky_sum(1, 3, 1) == 3


def test_total():
    # Testing total
    #
    assert hw0.total(5) == 15
    assert hw0.total(10) == 55
    assert hw0.total(-1) is None


def test_swip_swap():
    # Testing swip_swap using 4 calls to assert_equals
    # At least two calls should be examples shown in the specification
    # At least two should be new examples you make up
    assert hw0.swip_swap('foobar', 'f', 'o') == 'offbar'
    assert hw0.swip_swap('foobar', 'b', 'c') == 'foocar'
    assert hw0.swip_swap('foobar', 'z', 'c') == 'foobar'


def main():
    test_funky_sum()
    test_total()
    test_swip_swap()


if __name__ == "__main__":
    main()
