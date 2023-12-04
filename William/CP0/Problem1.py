#!/usr/bin/env python3

""" 
Problem 1, CPO, UW CSE 163
Timer that decrements from 60 to 10 seconds, using a for loop.
"""

def main():
    print("One minute countdown")

    for i in range(60, -1, -10):
        print(i)

    print("Done!")

if __name__ == "__main__":
    main()
