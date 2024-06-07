import numpy as np

class CountMinSketch:
    '''
    Implements a dictionary according to the description found
    at: https://cse163.github.io/book/module-9-miscellaneous-topics/lesson-26-reading-hashing/optional-count-min-sketch.html

    We will have 4 "dictionaries", with 4 unique hashing methods.
    '''
    def __init__(self, size):
        '''
        size = the size of each dictionary
        Use numpy to create four arrays of the requested size
        '''
        self.primes = [ 1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 ]
        self.hashes = [ self.hash_1, self.hash_2, self.hash_3, self.hash_4 ]
        self.large_prime = 12345678923
        self.size = size

    def hash_1(self, s):
        '''
        hash = Sigma: ch(i) * i
        '''
        pass
        
    def hash_2(self, s):
        '''
        hash = Sigma: ch(i)*prime[i]
        '''
        pass

    def hash_3(self, s):
        '''
        hash = Sigma: ch(i)*p**n-i-1
        p = 31
        '''
        pass

    def hash_4(self, s):
        '''
        hash = concatenate ord(ch(i)) mod m
        '''
        pass

    def add(self, word):
        '''
        Increments the count for this string to all 4 hash tables
        '''
        pass

    def get(self, word):
        '''
        Find the value for this string in all 4 hash tables.
        return the min value
        '''
        pass
        
def test_hashes():
    size = 200
    cms = CountMinSketch(size)
    
    words = ['test', 'stride', 'monkey', 'the', 'is', 'elephant']
    
    for word in words:
        hashes = {}
        for hash in cms.hashes:
            val = hash(word) % size
            hashes.add(val)
        # assert(len(hashes) == 4)

def test_add_get():
    cms = CountMinSketch(5)
    words = ['test', 'stride', 'monkey', 'the', 'is', 'elephant']
    for word in words:
        cms.add(word)
        cms.add(word)
    for word in words:
        print(cms.get(word))
    expected = [ 2, 4, 4, 2, 2, 2]
    
def main():
    test_hashes()
    
if __name__ == '__main__':
    main()