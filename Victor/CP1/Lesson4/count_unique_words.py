# count_unique_words

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-4-lists-and-files/practice-count-unique-words.html


def count_unique_words(file_name) -> list:
    """Returns all unique words from a file

    Args:
        file_name (txt file): file

    Returns:
        list: list of unique words from file
    """
    unique_words = []
    with open(file_name, encoding="r") as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.split()
            for i in tokens:
                if i not in unique_words:
                    unique_words.append(i)
    return unique_words
