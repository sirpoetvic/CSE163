"""
William Dinh
Intermediate Data Programming
"""

from cse163_utils import normalize_token


class Document:
    """
    Represents the data in a single web page and
    includes methods to compute term frequency
    """
    def __init__(self, path):
        """initializes the docuemnt data

        Args:
            path (str): file path
        """
        self._path_loc = path
        self._docdict = dict()
        self._term_counting = 0

        with open(path, encoding='utf-8') as file:
            contents = file.readlines()
            for content in contents:
                tokens = content.split()
                for token in tokens:
                    n = normalize_token(token)
                    if n in self._docdict:
                        self._docdict[n] += 1
                    else:
                        self._docdict[n] = 1
                    self._term_counting += 1

    def term_frequency(self, term):
        """
        Args:
            terms (str): term to be looked up

        Returns:
            Term frequency of a given term by looking it up
            in the precomputed dictionary.
        """
        normalize = normalize_token(term)

        if normalize in self._docdict:
            return self._docdict[normalize] / self._term_counting
        return 0

    def get_path(self):
        """
        Returns:
            The path of the file that this document represents
        """
        return self._path_loc

    def get_words(self):
        """
        Returns:
        list of the unique, normalized words in this document
        """
        return list(self._docdict)
