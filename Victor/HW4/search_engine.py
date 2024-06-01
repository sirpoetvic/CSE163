"""
Victor Wong
CSE163 Data Science
SearchEngine Class
"""

import math
import os
from document import Document
from cse163_utils import normalize_token


class SearchEngine:

    def __init__(self, path: str):
        # Documents are in a list so that it may be iterated upon
        self._documents = list()
        # list of words, mapped to documents words are in
        self._inverted_index = dict()

        for filename in os.listdir(path):
            self._documents.append(Document(os.path.join(path, filename)))

        for doc in self._documents:
            for word in doc.get_words():
                normalized = normalize_token(word)
                if word in self._inverted_index:
                    self._inverted_index[normalized].append(doc)
                else:
                    self._inverted_index[normalized] = [doc]

    def _calculate_idf(self, item: str):
        """
        Calculates the inverse document frequency of the item.
        If the item is not in the corpus, then return 0.

        Args:
            item (str): term

        Returns:
            int: inverse document frequency
        """
        if item not in self._inverted_index:
            return 0
        # logarithm total documents divided by documents with term
        return math.log(len(self._documents) / len(self._inverted_index[item]))

    def search(self, query: str):
        """
        Returns a list of document paths sorted in descending order
        by tf-idf statistic.

        Args:
            query (str): _description_
        """
        valid_docs = dict()
        # normalize each token
        words = query.split()
        words = (normalize_token(token) for token in words)

        # check each word
        for word in words:
            if word not in self._inverted_index:
                break
            # Calculate the tfidf per word, in a given doc
            idf = self._calculate_idf(word)
            for doc in self._inverted_index[word]:
                tf = doc.term_frequency(word)
                tfidf = tf * idf
                if doc not in valid_docs:
                    # Create new entry in valid_docs
                    valid_docs[doc] = tfidf
                else:
                    # Add to the current tfidf for the current doc
                    valid_docs[doc] += tfidf
        # sort the documents by their tfidf scores
        sorted_docs_with_scores = sorted(
            valid_docs.items(), key=lambda item: item[1], reverse=True
        )
        # return ONLY the document paths, excluding the tfidf part of the tuple
        return [doc.get_path() for doc, _ in sorted_docs_with_scores]
