#!/usr/bin/env python3
"""
Write a function named switch_pairs that accepts a string as a parameter and returns that string with each pair of 
neighboring letters reversed. 

If the string has an odd number of letters, the last letter should not be modified. 

For example, the call switch_pairs("example") should return "xemalpe" and the call switch_pairs("hello there") 
should return "ehll ohtree".

This function returns a string and does not print anything.
"""

def switch_pairs(pair):
    str_holder = list(pair)
    for i in range(0, len(pair)-1, 2):
        str_holder[i], str_holder[i+1] = str_holder[i+1], str_holder[i]
    return ''.join(str_holder)

# using to test if the output is actually correct 
def main():
    print(switch_pairs("example")) # returns - "xemalpe"
    print(switch_pairs("hello there")) # returns - "ehll ohtree"
    
if __name__ == "__main__":
    main()