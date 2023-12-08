#!/usr/bin/env python3
"""
Write a function called countdown that takes a starting number of seconds and starts the countdown from there instead (from increments of 10)
The format of the output will be slightly different to accommodate this starting point.

If the sequence does not evenly end with a 0 (e.g. if the countdown starts from 15 ), then 0 will not be printed. 
"""
def countdown(number):
    if number < 0:
        print ("Start must be non-negative!")
    else:  
        print (f"{number} second countdown!")       
        for i in range (number, -1, -10):
            print (i)
                
        print("Done!")
    
def sample_run():
    countdown(60)
    print()
    countdown(15)
    print()
    countdown(-4)
    print()
    countdown(0)
    
def main():
    sample_run()

if __name__ == "__main__":
    main()