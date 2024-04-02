"""count_words"""

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-5-data-structures-tuple-set-dict/practice-count-words.html


def count_words(file_name) -> dict:
    """Returns a dictionary denoting how many times
    each word occurs in a file

    Args:
        file_name (txt file): file

    Returns:
        dict: dictionary with words and number
        of respective occurences
    """

    dictionary = {}
    with open(file_name, encoding="r") as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.split()
            for token in tokens:
                if token not in dictionary.keys():
                    dictionary[token] = 1
                else:
                    dictionary[token] += 1
    return dictionary
