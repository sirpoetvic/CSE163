def count_unique_words(file_name):
    """
    Returns the amount of unique words, including punctuation.

    Args:
        file_name (.txt): file name to count unique words
    """
    file_words = []
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            words = line.strip().split()
            for i in words:
                if i not in file_words:
                    file_words.append(i)
    return len(file_words)


def main():
    print(count_unique_words("William\\CP1\\test_files\\song.txt"))


if __name__ == "__main__":
    main()
