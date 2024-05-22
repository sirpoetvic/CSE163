"""
Victor Wong
CSE163
Document class
"""
import normalize_token from cse163_utils

class Document:
    # might need a dict containing unique normalized words in doc
    doc_dict = dict()
    # path file name
    file_name = ""
    

def __init__(path):
    """takes a path to a document and initializes the document data.
    precompute the term frequency

    Args:
        path (string): string of the path of the document
    """
    # normalize all of the tokens in the file, create dictionary
    
def term_frequency(self, term) -> int:
    """
    return the number of occurences of a term in the doc

    Args:
        term (string): term

    Returns:
        int: number of occurences of term
    """
    if(term not in self.doc_dict):
        return 0
    return term[term]

def get_words(self) -> list:
    """
    returns a list of the unique, normalized words in the document

    Returns:
        list: list of unique, normalized words in the document
    """
    return list(self.doc_dict)



    
