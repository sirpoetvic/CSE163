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
        )
    )

    assert_equals(3/226,
                  Document(
                      "William\\HW4\\test_corpus_two\\upside_down.txt"
                      ).term_frequency("upside"))


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


def test_search_engine():
    """
    Testing search engine with test_corpus_two
    """
    engine = SearchEngine("William\\HW4//test_corpus_two")

    # search for a term that is in some documents
    result1 = engine.search("Bruno")
    expected1 = [
        'William\\HW4//test_corpus_two\\doc1.txt',
        'William\\HW4//test_corpus_two\\doc2.txt']

    assert_equals(expected1, result1)

    # search for a term that is in all documents
    result2 = engine.search("the")
    expected2 = ['William\\HW4//test_corpus_two\\doc3.txt',
                 'William\\HW4//test_corpus_two\\doc2.txt',
                 'William\\HW4//test_corpus_two\\upside_down.txt']
    assert_equals(expected2, result2)

    # no term in doc
    result3 = engine.search("asdfhjlasdjflaksjd")
    expected3 = []
    assert_equals(expected3, result3)

    # search for a term that appears in only one document
    result4 = engine.search("musician")
    expected4 = ['William\\HW4//test_corpus_two\\doc1.txt']
    assert_equals(expected4, result4)


def main():
    # Call your test functions here!
    """
    Runs all testing functions
    """
    test_term_frequency()
    test_get_path()
    test_get_words()
    test_search_engine()
    print("it works!")


main()
