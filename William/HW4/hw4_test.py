"""
Student Name
"""

# this file is excluded from flake8
# The tests you create will be graded

from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine


def test_term_frequency():
    """
    testing term_frequency from Document
    """

    assert_equals(
        0.25,
        Document("William\\HW4\\test_corpus\\document2.txt").term_frequency(
            "dog"
        ),
    )


def test_get_path():
    """
    testing get_path from Document
    """
    assert_equals(
        "William\\HW4\\test_corpus\\document1.txt",
        Document("William\\HW4\\test_corpus\\document1.txt").get_path(),
    )


def test_get_words():
    """
    testing get_words from Document
    """
    assert_equals(
        ['i', "love", "bruno"],
        Document("William\\HW4\\test_corpus\\document1.txt").get_words(),
    )


def test_serach_test_corpus():
    """
    Testing test_corpus with serach engine
    """
    engine = SearchEngine("William//HW4//test_corpus")
    assert_equals(['William//HW4//test_corpus\\document3.txt',
                   'William//HW4//test_corpus\\document1.txt',
                   'William//HW4//test_corpus\\document2.txt'],
                  engine.search("i"))

    assert_equals(['William//HW4//test_corpus\\nsa.txt'],
                  engine.search("cia"))

    assert_equals(['William//HW4//test_corpus\\document1.txt'],
                  engine.search("bruno"))


def test_serach_small_text():
    """
    Testing search engine with small_text
    Must run in reasonable time.
    """
    engine = SearchEngine("William//HW4//small_text")
    assert_equals(['William//HW4//small_text\\Black or White - Wikipedia.txt',
                   'William//HW4//small_text\\Humberto Gatica - Wikipedia.txt'],
                  engine.search("Bottrell"))

    assert_equals(['William//HW4//small_text\\Rhinoplasty - Wikipedia.txt',
                   'William//HW4//small_text\\Michael Jackson - Wikipedia.txt'],
                  engine.search("Rhinoplasty"))

    assert_equals([['William//HW4//small_text\\Bob Corker - Wikipedia.txt',
                    'William//HW4//small_text\\Orrin Hatch - Wikipedia.txt',
                    'William//HW4//small_text\\Traditionalist conservatism - Wikipedia.txt']],
                  engine.search("corker"))


def main():
    # Call your test functions here!
    """
    Runs all testing functions
    """
    test_term_frequency()
    test_get_path()
    test_get_words()
    test_serach_test_corpus()
    test_serach_small_text()


if __name__ == "__main__":
    main()
