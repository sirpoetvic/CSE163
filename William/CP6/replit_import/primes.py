from cse163_utils import assert_equals
from math import sqrt, ceil
from time_graph import TimeGraph

# Implement get_primes
def get_primes(max):
    '''
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
    '''
    # Your implementation goes here
    everything = set()

    # step 1
    for e in range(2, max):
        everything.add(e)

    # copy to remove stuff later on
    primes = everything.copy()
    # make sqrt is a whole number
    # if no factors are before sqrt(max) then the number will has to be prime
    new_max = ceil(sqrt(max))
    # remove multiples
    for i in range(2, new_max + 1):
        # if i is in the set primes, it is prime
        if i in primes:
            # start at i*i since dupes are already removed and we can
            # loop through faster because of it
            for j in range(i * i, max, i):
                primes.discard(j)
    return primes


# Test get_primes as necessary
def test_set_of_primes():
    fiddy = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
    assert_equals(fiddy, get_primes(50))
    print('set_of_primes Success')


def hailstone_seq(n):
    '''
    n = the max n value to include in the result.
    return a dictionary with the key = number, value = length of sequence.
    next = n / 2     if n is even
    next = n * 3 + 1 if n is odd
    End the sequence when n == 1
    '''
    # Your implementation goes here
    return {1: 1, 2: 2, 3: 8, 4: 3}

    
def graph_prime_performance(timer):
    timer.time_and_graph(get_primes, 'get_primes')


def main():
    # once your implementation of getting primes is complete,
    # graph its performance
    test_set_of_primes()
    timer = TimeGraph()
    graph_prime_performance(timer)
    
if __name__ == '__main__':
    main()
