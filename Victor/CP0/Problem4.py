"""write a function named switch_pairs() that takes a string argument and
   swaps all adjacent letters (leaving any unpaired letter untouched)"""


def switch_pairs(str):
    returnstring = ""
    for i in range(0, len(str) - 1, 2):
        returnstring += str[i + 1] + str[i]
    if len(str) % 2 == 1:
        returnstring += str[len(str) - 1]
    return returnstring


def main():
    assert switch_pairs("example") == "xemalpe"
    assert switch_pairs("hello there") == "ehll ohtree"


if __name__ == "__main__":
    main()
