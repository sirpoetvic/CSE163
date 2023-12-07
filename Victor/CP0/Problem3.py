'''write a method named fibonacci() that takes an argument n that will
   return the first fibonacci number that is greater than n.'''

def fibonacci( int ):
    num1, num2 = 0, 1
    while(num1 < int):
        num1, num2 = num2, num1 + num2
    print(num2)

def main():
    fibonacci(2)
    
if(__name__ == '__main__'): 
    main()