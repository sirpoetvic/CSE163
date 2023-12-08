# fun_numbers

'''Write a function called fun_numbers that takes a start number
and stop number and returns a list of all “fun” numbers between
start (inclusive) and stop (exclusive). A number is “fun” if it
is divisible by 2 or divisible by 5. The result should have the
numbers arranged from smallest to largest.'''

def fun_numbers( start, stop ):
    list = []
    for i in range(start, stop):
        if(i % 2 == 0 or i % 5 == 0):
            list.append(i)
    return list

print(fun_numbers(2, 16))