"""
William Dinh
Intermediate Data Programming
CSE 163
"""

from cse163_utils import normalize_token


class Document:
    def __init__(self, path):
        with open(path) as file:
            self.path = file.readlines()

    def td(self, t, d):
        # count of term t in d
        # divided by count of words in d
        
        pass


token = "CoRgi!!"
token = normalize_token(token)
print(token)  # corgi

token1 = "<div>Hi!</div>"
token1 = normalize_token(token1)
print(token1)  # divhidiv
