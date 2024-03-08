"""
Your information here
"""

import pandas as pd

from cse163_utils import assert_equals, parse

import hw2_manual
import hw2_pandas


# Your tests here!
def test_species_count():
    assert_equals(3,
                  hw2_manual.species_count('William\\HW2\\pokemon_test.csv'))
    assert_equals(3,
                  hw2_pandas.species_count('William\\HW2\\pokemon_test.csv'))


def main():
    # Call your test functions here!
    test_species_count()


if __name__ == "__main__":
    main()
