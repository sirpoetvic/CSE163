"""
Student Name
"""

# this file is excluded from flake8
# The tests you create will be graded

from cse163_utils import assert_equals

from document import Document

# from search_engine import SearchEngine


def test_term_frequency():
    assert_equals(
        0.25,
        Document("Victor\\HW4\\test_corpus\\document2.txt").term_frequency(
            "dog"
        ),
    )


def test_get_path():
    assert_equals(
        "Victor\\HW4\\test_corpus\\document1.txt",
        Document("Victor\\HW4\\test_corpus\\document1.txt").get_path(),
    )


def main():
    # Call your test functions here!
    """
    Runs all testing functions
    """
    test_term_frequency()
    test_get_path()


main()
