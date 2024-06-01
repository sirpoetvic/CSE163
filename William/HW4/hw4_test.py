"""
Student Name
"""

# this file is excluded from flake8
# The tests you create will be graded

from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine


def test_term_frequency():
    assert_equals(
        0.25,
        Document("William\\HW4\\test_corpus\\document2.txt").term_frequency(
            "dog"
        ),
    )


def test_get_path():
    assert_equals(
        "William\\HW4\\test_corpus\\document1.txt",
        Document("William\\HW4\\test_corpus\\document1.txt").get_path(),
    )


def test_get_words():
    assert_equals(
        ['i', "love", "bruno"],
        Document("William\\HW4\\test_corpus\\document1.txt").get_words(),
    )


def test_search_engine():
    engine = SearchEngine("William\\HW4\\test_corpus\\")
    print(engine.search("love dogs"))


def main():
    # Call your test functions here!
    """
    Runs all testing functions
    """
    # test_term_frequency()
    # test_get_path()
    # test_get_words()
    test_search_engine()


if __name__ == "__main__":
    main()
