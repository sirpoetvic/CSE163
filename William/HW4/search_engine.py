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
        associating each term in the corpus to the list of documents
        that contain the term.Do not recreate any behavior that is
        already done in the Document class—call the Document.get_words method!
        Create at most one Document object for each file.

        Args:
            path (str): file path(s) to be accessed
        """
        self._docs = []
        self._inverted_indexes = {}

        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            document = Document(file_path)
            self._docs.append(document)

            for word in document.get_words():
                normalized = normalize_token(word)
                if normalized not in self._inverted_indexes:
                    self._inverted_indexes[normalized] = [document]
                else:
                    self._inverted_indexes[normalized].append(document)

    def _calculate_idf(self, term):
        """
        Calculates the Inverse Document Frequency (IDF) for a given term.

        Args:
            term (str): The term for which IDF is to be calculated.

        Returns:
            float: The IDF value of the term. If the term is not in any
            document, returns 0.
        """
        normalized_term = normalize_token(term)
        word_list = self._inverted_indexes.get(normalized_term, [])
        num_docs = len(word_list)
        if num_docs == 0:
            return 0
        return math.log(len(self._docs) / num_docs)

    def _calculate_tf_idf(self, term, document):
        """
        Calculates the Term Frequency-Inverse Document Frequency (TF-IDF)
        for a term in a given document.

        Args:
            term (str): The term for which TF-IDF is to be calculated.
            document (Document): The document in which the term's TF-IDF
            is to be calculated.

        Returns:
            float: The TF-IDF value of the term in the document.
        """
        normalized_term = normalize_token(term)
        idf = self._calculate_idf(normalized_term)
        tf = document.term_frequency(normalized_term)
        return idf * tf

    def search(self, query):
        """
        Searches for the given query in the corpus and returns a list of
        document paths sorted by relevance based on rf-idf scores.

        Args:
            query (str): The search query containing one or more terms.

        Returns:
            list: A list of document paths sorted by relevance.
        """

        terms = [normalize_token(term) for term in query.split()]
        if not terms:
            return []

        # initialize scores for all documents to 0
        document_scores = {document: 0 for document in self._docs}

        for term in terms:
            if term in self._inverted_indexes:
                for document in self._inverted_indexes[term]:
                    # calculate tfidf for the term in the document
                    tf_idf = self._calculate_tf_idf(term, document)
                    document_scores[document] += tf_idf

        # sort documents by their scores in descending order
        sorted_documents = sorted(document_scores.items(),
                                  key=lambda x: x[1],
                                  reverse=True)

        # extract paths of sorted documents
        sorted_paths = [doc.get_path() for doc,
                        score in sorted_documents if score > 0]

        return sorted_paths
