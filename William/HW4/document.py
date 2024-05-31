"""
William Dinh
Intermediate Data Programming
"""

from cse163_utils import normalize_token



class Document:
    """_summary_
    """
    def __init__(self, path):
        """_summary_

        Args:
            path (_type_): _description_
        """
        self._path_loc = path
        self._docdict = dict()
        self._term_counting = 0

        with open(path, 'r') as file:
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
        """_summary_

        Args:
            terms (_type_): _description_

        Returns:
            _type_: _description_
        """
        if term in self._docdict:
            return self._docdict[term] / self._term_counting
        return 0

    def get_path(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._path_loc

    def get_words(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return list(self._docdict)
