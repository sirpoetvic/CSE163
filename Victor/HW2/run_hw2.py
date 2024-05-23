"""
Victor Wong
CSE 163
Testing cases only
"""

from cse163_utils import assert_equals
from cse163_utils import parse

import Victor.HW2.hw2_manual as hw2_manual
import Victor.HW2.hw2_pandas as hw2_pandas
import pandas as pd


file = parse("pokemon_test.csv")
data = pd.read_csv("Victor\\HW3\\pokemon_test.csv")
victor_data = pd.read_csv("Victor\\HW3\\victor_test.csv")
victor_file = parse("victor_test.csv")


# Your tests here!
def test_species_count():
    """
    Tests both manual and pandas version of species_count
    """
    assert_equals(3, hw2_manual.species_count(file))
    assert_equals(3, hw2_pandas.species_count(data))
    # my test with my own CSV
    assert_equals(8, hw2_manual.species_count(victor_file))
    assert_equals(8, hw2_pandas.species_count(victor_data))


def test_max_level():
    """
    Tests both manual and pandas version of max_level
    """
    assert_equals(("Lapras", 72), hw2_manual.max_level(file))
    assert_equals(("Lapras", 72), hw2_pandas.max_level(data))

    # my test case
    assert_equals(("Blastoise", 89), hw2_pandas.max_level(victor_data))
    assert_equals(("Blastoise", 89), hw2_manual.max_level(victor_file))


def test_filter_range():
    """
    Tests both manual and pandas version of filter_range
    """
    assert_equals(
        ["Arcanine", "Arcanine", "Starmie"],
        hw2_pandas.filter_range(data, 35, 72),
    )
    assert_equals(
        ["Arcanine", "Arcanine", "Starmie"],
        hw2_manual.filter_range(file, 35, 72),
    )
    # my test case
    assert_equals(
        [
            "Arcanine",
            "Arcanine",
            "Starmie",
            "Pikachu",
            "Snorlax",
            "Charizard",
            "Poliwrath",
        ],
        hw2_pandas.filter_range(victor_data, 35, 72),
    )
    assert_equals(
        [
            "Arcanine",
            "Arcanine",
            "Starmie",
            "Pikachu",
            "Snorlax",
            "Charizard",
            "Poliwrath",
        ],
        hw2_manual.filter_range(victor_file, 35, 72),
    )


def test_mean_attack_for_type():
    """
    Tests manual and pandas version of mean_attack_for_type
    """
    assert_equals(47.5, hw2_pandas.mean_attack_for_type(data, "fire"))
    assert_equals(47.5, hw2_manual.mean_attack_for_type(file, "fire"))
    # my test case
    assert_equals(
        112.25,
        hw2_pandas.mean_attack_for_type(victor_data, "water"),
    )
    assert_equals(
        112.25,
        hw2_manual.mean_attack_for_type(victor_file, "water"),
    )
    assert_equals(
        None,
        hw2_manual.mean_attack_for_type(file, "sdjflaksjdflka"),
    )
    assert_equals(None, hw2_pandas.mean_attack_for_type(data, "edge"))


def test_count_types():
    expected1 = {"fire": 2, "water": 2}
    expected2 = {"fire": 3, "water": 4, "electric": 1, "normal": 1}
    assert_equals(expected1, hw2_manual.count_types(file))
    assert_equals(expected1, hw2_pandas.count_types(data))
    assert_equals(expected2, hw2_pandas.count_types(victor_data))
    assert_equals(expected2, hw2_manual.count_types(victor_file))


def test_mean_attack_per_type():
    """
    Testing mean_attack_per_type manual and python
    """
    assert_equals(
        {"fire": 47.5, "water": 140.5},
        hw2_manual.mean_attack_per_type(file),
    )
    assert_equals(
        {"fire": 47.5, "water": 140.5},
        hw2_pandas.mean_attack_per_type(data),
    )
    assert_equals(
        {"fire": 60, "water": 112.25, "electric": 55.0, "normal": 110.0},
        hw2_manual.mean_attack_per_type(victor_file),
    )
    assert_equals(
        {"fire": 60, "water": 112.25, "electric": 55.0, "normal": 110.0},
        hw2_pandas.mean_attack_per_type(victor_data),
    )


def main():
    # Call your test functions here!
    """
    Runs all testing functions
    """
    test_species_count()
    test_max_level()
    test_filter_range()
    test_mean_attack_for_type()
    test_count_types()
    test_mean_attack_per_type()


if __name__ == "__main__":
    main()
