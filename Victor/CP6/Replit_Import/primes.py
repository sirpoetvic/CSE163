from cse163_utils import assert_equals
from math import sqrt
from time_graph import TimeGraph


# Implement get_primes
def get_primes(max):
    """
    Return a set of all the prime numbers lower than max. (max is exclusive)

    Create by using the following process/algorithm:
      Fill a set with all numbers starting at 2 and go up to max.
      For every number n still in the set of primes
        remove all multiples of n, but not n itself

    The steps go like this: (This is the Sieve of Eratosthenes)
    Step 1 { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 }  # fill with all numbers
    Step 2 { 2, 3,    5,    7,    9,     11,     13,     15 }  # remove multiples of 2
    Step 3 { 2, 3,    5,    7,           11,     13         }  # remove multiples of 3
    Etc.
    """
    return_set = set()
    for i in range(2, max):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            return_set.add(i)
    return return_set


# Test get_primes as necessary
def test_set_of_primes():
    fiddy = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
    assert_equals(fiddy, get_primes(50))
    print("set_of_primes Success")


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
