def find_range(rng_list):
    return max(rng_list) - min(rng_list) + 1


def main():
    find_range([12, 17, 6])
    find_range([2, 3, 4])


if __name__ == "__main__":
    main()
