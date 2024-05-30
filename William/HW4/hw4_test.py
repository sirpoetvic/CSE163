'''
Student Name
'''
# this file is excluded from flake8
# The tests you create will be graded

from cse163_utils import assert_equals

from document import Document
# from search_engine import SearchEngine


def test_document(paths):
    assert_equals("William\\HW4\\test_corpus\\document1.txt", paths.get_path())
    assert_equals(['i', 'love', 'bruno'], paths.get_words())
    assert_equals(1/3, paths.term_frequency("love"))


def main():
    # Call your test functions here!
    """
    Runs all testing functions
    """
    path = Document("William\\HW4\\test_corpus\\document1.txt")
    path2 = Document("William\\HW4\\test_corpus\\document2.txt")
    path3 = Document("William\\HW4\\test_corpus\\document3.txt")
    nsa = Document("William\\HW4\\test_corpus\\nsa.txt")
    test_document(path)


if __name__ == "__main__":
    main()
