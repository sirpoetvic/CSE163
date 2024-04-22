def count_words(file_name):
    """
    Returns a dict that stores the words as keys and values
    Counts the number of times that word appeared in the file

    Args:
        file_name (.txt file): file to access,
    """
    word_appear = {}
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for i in words:
                if i in word_appear:
                    word_appear[i] += 1
                else:
                    word_appear[i] = 1
    return word_appear


def main():
    print(count_words("William\\CP1\\text_files\\popular_techno_song.txt"))


if __name__ == "__main__":
    main()
