from my_set import MySet


def main():
    s = MySet()
    nums = [14, 2, 17, 12]
    query = [14, 2, 17, 12, 4]
    for n in nums:
        s.add(n)
    print('Length of set:', len(s))
    for n in query:
        print('Set contains', n, '=>:', n in s)


if __name__ == '__main__':
    main()
