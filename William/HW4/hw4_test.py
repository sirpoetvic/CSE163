'''
Student Name
'''
# this file is excluded from flake8
# The tests you create will be graded

from William.HW4.cse163_utils import assert_equals

from document import Document
# from search_engine import SearchEngine


def test_document(path):
    assert_equals("document1.txt", path.get_path("William\\HW4\\test_corpus\\document1.txt"))


def main():
    # Call your test functions here!
    """
    Runs all testing functions
    """
    path = Document("William\\HW4\\test_corpus\\document1.txt")
    test_document(path)


if __name__ == "__main__":
    main()
