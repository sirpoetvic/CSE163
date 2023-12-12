def switch_pairs(pair):
    str_holder = list(pair)
    for i in range(0, len(pair)-1, 2):
        str_holder[i], str_holder[i+1] = str_holder[i+1], str_holder[i]
    return ''.join(str_holder)


def main():
    print(switch_pairs("example"))  # returns - "xemalpe"
    switch_pairs("hello there")  # returns - "ehll ohtree"


if __name__ == "__main__":
    main()
