"""switch_pairs"""

# https://cse163.github.io/book/module-1-introduction-to-python/lesson-3-strings-and-lists/practice-switch_pairs.html


def switch_pairs(string: str):
    """takes a string argument and swaps all adjacent letters (leaving any
    unpaired letter untouched)

     Args:
         string (str): string to have leters swapped

     Returns:
         _type_: _description_
    """

    returnstring = ""
    for i in range(0, len(string) - 1, 2):
        returnstring += string[i + 1] + string[i]
    if len(string) % 2 == 1:
        returnstring += string[len(string) - 1]
    return returnstring


def main():
    """Main method using assert for test cases"""

    assert switch_pairs("example") == "xemalpe"
    assert switch_pairs("hello there") == "ehll ohtree"


if __name__ == "__main__":
    main()
