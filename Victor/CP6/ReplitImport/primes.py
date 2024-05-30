from cse163_utils import assert_equals
from math import sqrt
from time_graph import TimeGraph


# Implement get_primes
def get_primes(max: int):
    """
    Gets all of the primes that are between 2 and max

    Args:
        max (int): number

    Returns:
        _type_: _description_
    """

    # Original implentation
    # primes = set()
    # for i in range(2, max):
    #     is_prime = True
    #     for j in range(2, int(i**0.5) + 1):
    #         if i % j == 0:
    #             is_prime = False
    #             break
    #     if is_prime:
    #         return_set.add(i)
    # return primes

    # Sieve of Eratosthenes implementation
    primes = set(range(2, max))
    for i in range(2, int(max**0.5)):
        if i in primes:
            for j in range(i * i, max, i):
                primes.discard(j)

    return primes


# Test get_primes as necessary
def test_set_of_primes():
    fiddy = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
    assert_equals(fiddy, get_primes(50))
    print("set_of_primes Success")


# O(n)


def hailstone_seq(n):
    """
    n = the max n value to include in the result.
    return a dictionary with the key = number, value = length of sequence.
    next = n / 2     if n is even
    next = n * 3 + 1 if n is odd
    End the sequence when n == 1
    """
    # Your implementation goes here
    return {1: 1, 2: 2, 3: 8, 4: 3}


def graph_prime_performance():
    timer = TimeGraph()
    timer.time_and_graph(get_primes, "get_primes")


def main():
    # once your implementation of getting primes is complete,
    # graph its performance
    test_set_of_primes()
    graph_prime_performance()


if __name__ == "__main__":
    main()
