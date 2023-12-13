
def count_votes(voting_results):
    canidates = [0, 0, 0]
    for i in voting_results:
        canidates[i] += 1
    return canidates


def main():
    votes = [1, 0, 1, 1, 2, 0]
    result = count_votes(votes)
    print(result)  # prints [2, 3, 1]


if __name__ == "__main__":
    main()
