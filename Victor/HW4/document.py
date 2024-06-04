"""
Victor Wong
CSE163 Data Science
Document class
"""

from cse163_utils import normalize_token


class Document:
    """
    Document class holds a dict variable that holds the frequency of unique,
    normalized words strings.
    """

    def __init__(self, path):
        """
        Takes a path to a document and initializes the document data.
        precompute term frequency

        Args:
            path (string): string of the path of the document
        """

        # might need a dict containing unique normalized words in doc
        self._doc_dict = dict()
        # path file name
        self._file_name = path
        # total number of words in doc
        self._total_words = 0

        with open(path, encoding="utf8") as f:
            lines = f.readlines()
            for line in lines:
                tokens = line.split()
                for token in tokens:
                    normal = normalize_token(token)
                    if normal in self._doc_dict:
                        self._doc_dict[normal] += 1
                    else:
                        self._doc_dict[normal] = 1
                    self._total_words = self._total_words + 1

    def term_frequency(self, term) -> int:
        """
        return the number of occurences of a term in the doc divided by
        the total number of terms in the doc

        Args:
            term (string): term

        Returns:
            int: number of occurences of term
        """
        normalized = normalize_token(term)
        if normalized in self._doc_dict:
            return self._doc_dict[normalized] / self._total_words
        return 0

    def get_words(self) -> list:
        """
        Returns a list of the unique, normalized words in the document

        Returns:
            list: list of unique, normalized words in the document
        """
        return list(self._doc_dict)

    def get_path(self) -> str:
        """
        Returns the path of the current document

        Returns:
            str: _description_
        """
        return self._file_name
