"""
Student Name
"""

# this file is excluded from flake8
# The tests you create will be graded

from cse163_utils import assert_equals

from document import Document

# from search_engine import SearchEngine


# This file is left blank for you to fill in with your tests!
test = Document("Victor\\HW4\\test_corpus\\document1.txt")
print(test.term_frequency("love"))
