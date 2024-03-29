def most_frequent(counts):
    """
    Returns the word with the highest count. The input is a dict
    with keys that are words and values that are counts.

    If the given dict is empty, returns None.
    """
    max_word = None
    for key, value in counts.items():
        if max_word is None or value > counts[max_word]:
            max_word = key
    return max_word


def main():
    word_counts = {'green': 2, 'eggs': 6, 'and': 3, 'yam': 2}
    print(most_frequent(word_counts))


if __name__ == '__main__':
    main()
