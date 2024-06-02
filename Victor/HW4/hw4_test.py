"""
Victor Wong
CSE163 Data Science
Testing file
"""

# this file is excluded from flake8
# The tests you create will be graded

from cse163_utils import assert_equals

from document import Document

from search_engine import SearchEngine


def test_term_frequency():
    """
    test the document class ability to get the term frequency (tf)
    """
    assert_equals(
        0.25,
        Document("test_corpus\\document2.txt").term_frequency("dog"),
    )


def test_get_path():
    """
    tests the document class ability to get the document path
    """
    assert_equals(
        "test_corpus\\document1.txt",
        Document("test_corpus\\document1.txt").get_path(),
    )


def test_get_words():
    """
    tests the ability for the document class to collect words
    """
    assert_equals(
        ["i", "love", "bruno"],
        Document("test_corpus\\document1.txt").get_words(),
    )


def test_search_engine():
    engine = SearchEngine("test_cases")

    # searching for a term in ALL documents
    result = engine.search("the")
    expected = [
        "test_cases\\test1.txt",
        "test_cases\\test2.txt",
        "test_cases\\test3.txt",
    ]
    assert_equals(expected, result)

    # searching for a term in SOME documents
    result = engine.search("quick")
    expected = [
        "test_cases\\test1.txt",
        "test_cases\\test3.txt",
    ]
    assert_equals(expected, result)

    # searching for a term in ONE document
    result = engine.search("slow")
    expected = ["test_cases\\test2.txt"]
    assert_equals(expected, result)

    # searching for a term in NO documents
    result = engine.search("superduperwowow")
    expected = []
    assert_equals(expected, result)


def main():
    # Call your test functions here!
    """
    Runs all testing functions
    """
    test_term_frequency()
    test_get_path()
    test_get_words()
    test_search_engine()
    print("all good!")


main()
