# most_frequent

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-6-csv-data/practice-most-frequent-word.html


def most_frequent(counts):
    """
    Returns the word with the highest count. The input is a dict
    with keys that are words and values that are counts.

    If the given dict is empty, returns None.
    """
    max_word, max_num = "", 0
    if not counts:
        return None
    for word in counts.items():
        if word[1] > max_num:
            max_word = word[0]
            max_num = word[1]
    return max_word
