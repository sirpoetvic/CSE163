"""
Victor Wong
CSE163
SearchEngine Class
"""

import math
import os
from cse163_utils import normalize_token
from document import term_frequency
from symbol import tfpdef


class SearchEngine:

    def __init__(self, path: str):
        # Documents are in a list so that it may be iterated upon
        self._documents = list()
        # list of words, mapped to documents words are in
        self._wordlist = dict()

        directory = "/course/small_wiki/"
        for filename in os.listdir(directory):
            self._documents.append(os.path.join(directory, filename))

        for doc in self._documents:
            for word in doc.get_words():
                normalized = normalize_token(word)
                if word in self._wordlist:
                    self._wordlist[normalized].append(doc)
                else:
                    self._wordlist[normalized] = [doc]

    def _calculate_idf(self, item: str):
        """
        Calculates the inverse document frequency of the item.
        If the item is not in the corpus, then return 0.

        Args:
            item (str): term

        Returns:
            int: inverse document frequency
        """
        if item not in self._wordlist:
            return 0
        # logarithm total documents divided by documents with term
        return math.log(len(self._documents) / len(self._wordlist[item]))

    def search(self, query: str):
        """
        Returns a list of document paths sorted in descending order
        by tf-idf statistic.

        Args:
            query (str): _description_
        """
        return_list = dict()
        # word_tfidf = dict()
        # for each normalized token, get the tfidf statistic
        words = query.split()
        words = (normalize_token(token) for token in words)
        for word in words:
            num = self._calculate_idf(word)
            if word in return_list:
                return_list[word] = set(
                    self._wordlist[word] + return_list[word]
                )
            else:
                return_list[word] = [self._wordlist[word]]
            # if word in word_tfidf:
            #     word_tfidf[word] += num
            # else:
            #     word_tfidf[word] = num
        # sort docs by tfidf statistics

        # add all the tfidf statistics together
        pass
