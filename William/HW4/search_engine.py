"""
William Dinh
Intermediate Data Programming
"""

import os
import math

from document import Document
from cse163_utils import normalize_token


class SearchEngine():

    def __init__(self, path):
        """Takes a string as a path, constructs an inverted index
        associating each term in the corpus to the list of documents that contain the term
        Do not recreate any behavior that is already done in the Document class—call the Document.get_words method!
        Create at most one Document object for each file.

        Args:
            path (str): file path(s) to be accessed
        """
        self._document_scores = {}
        self._document = Document
        self._inverted_indexes = dict()
        self._docs = [
            Document(os.path.join(path, filename))
            for filename in os.listdir(path)]

        # appends to the inverted index
        for document in self._docs:
            for words in document.get_words():
                if words not in self._inverted_indexes:
                    self._inverted_indexes[words] = [document]
                else:
                    self._inverted_indexes[words].append(document)

    def _calculate_idf(self, term):
        word_list = self._inverted_indexes.get(normalize_token(term))
        if word_list is not None:
            num_docs = len(word_list)
        else:
            num_docs = 0

        return math.log(len(self._docs) / num_docs)

    def _calculate_tf_idf(self, term, document):
        idf = self._calculate_idf(term)

        if not idf:
            return 0

        return idf * document.term_frequency(term)

    def search(self, query):
        terms = []
        for term in query.split():
            normalized_term = normalize_token(term)
            terms.append(normalized_term)

        if not terms:
            return []

        # Initialize scores for all documents to 0
        document_scores = {}
        for document in self._docs:
            document_scores[document] = 0

        for term in terms:
            if term in self._inverted_indexes:
                for document in self._inverted_indexes[term]:
                    # Calculate TF-IDF for the term in the document
                    tf_idf = self._calculate_tf_idf(term, query)
                    document_scores[document] += tf_idf

        # Sort documents by their scores in descending order
        sorted_documents = sorted(document_scores.items(),
                                  key=lambda x: x[1],
                                  reverse=True)

        # Extract paths of sorted documents
        sorted_paths = []
        for (doc, _) in sorted_documents:
            sorted_paths.append(doc.get_path())

        return sorted_paths
