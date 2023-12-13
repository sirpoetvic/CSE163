def switch_pairs(pair):
    str_together = ''
    for i in range(0, len(pair)-1, 2):
        str_together += pair[i+1] + pair[i]
    if len(pair) % 2 != 0:
        str_together += pair[-1]  # pair[-1] indicates the end of the list
    return str_together


def main():
    print(switch_pairs("example"))  # "xemalpe"
    print(switch_pairs("hello there"))  # "ehll ohtree"


if __name__ == "__main__":
    main()
