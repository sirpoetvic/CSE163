"""
Victor Wong
CSE163
SearchEngine Class
"""

from cse163_utils import normalize_token
import math


class SearchEngine:

    def __init__(self, path: str):
        # Documents are in a list so that it may be iterated upon
        self._documents = list()

        for document in self._documents:
            # check all documents to see if the word is present, and add the doc if the word is in there.
            break  # temp block

        # number of docs is stored to help calculate IDF
        self._num_docs = 0

    def _calculate_idf(self, item: str):
        """
        Calculates the inverse document frequency of the item.
        If the item is not in the corpus, then return 0.

        Args:
            item (str): term

        Returns:
            int: inverse document frequency
        """
        num_docs_with_term = 0
        for doc in self._documents:
            if item in doc:
                num_docs_with_term += 1
        if num_docs_with_term == 0:
            return 0
        return math.log(self._num_docs / num_docs_with_term)

    def search(self, query: str):
        """
        Returns a list of document paths sorted in descending order
        by tf-idf statistic.

        Args:
            query (str): _description_
        """
        tokens = query.split()
        for token in tokens:
            
