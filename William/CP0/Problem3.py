#!/usr/bin/env python3
"""
Write a function named fibonacci to compute the first Fibonacci number larger than a given value n .

The Fibonacci Sequence is the following sequence of numbers: 1, 1, 2, 3, 5, 8, 13, … 
The sequence starts with 1 and 1. The next number in the sequence is the sum of the previous two.
"""
def fibonacci(n):
    if n <= 0:
        return 1
# curr stores the current value; prev stores the prev value
    curr, prev = 1, 1
    sum = 0
    while (sum <= n):
        # add code that gives the value of the first number larger than N
        sum = curr + prev
        prev = curr
        curr = sum 
    return sum

def main():
    print(fibonacci(3)) # output is 5
    print(fibonacci(6)) # output is 8
    print(fibonacci(-2)) # output is 1    
    
if __name__ == "__main__":
    main()