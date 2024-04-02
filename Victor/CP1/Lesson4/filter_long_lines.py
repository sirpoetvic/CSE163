# filter_long_lines

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-4-lists-and-files/practice-filter-long-lines.html


def filter_long_lines(filename, minnum):
    """Prints all lines that have at least minnum number of
    words in each line of file

    Args:
        filename (txt file): file
        minnum (int): minimum number of words
    """
    with open(filename, encoding="r") as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.split()
            if len(tokens) >= minnum:
                print(line)
