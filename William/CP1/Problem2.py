def filter_long_lines(song_file, word_min):
    """
    Prints out all of the lines in the file with at least that many words

    Args:
        song_file (.txt): file name
        word_min (int): minimum number of words
    """
    with open(song_file) as file:
        lines = file.readlines()
        for line in lines:
            words = line.strip().split()
            if len(words) >= word_min:
                print(line)


def main():
    filter_long_lines('William\\CP1\\song.txt', 7)


if __name__ == "__main__":
    main()
