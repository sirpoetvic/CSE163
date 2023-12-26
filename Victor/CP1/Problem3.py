# count_unique_words

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-4-lists-and-files/practice-count-unique-words.html

    """Returns all unique words in a given txt file
    """
def count_unique_words(file_name):
    unique_words = []
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.split()
            for i in tokens:
                if i in unique_words:
                    continue
                else:
                    unique_words.append(i)
    return unique_words
