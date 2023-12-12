'''write a method named fibonacci() that takes an argument n that will
   return the first fibonacci number that is greater than n.'''


def fibonacci(int):
    num1, num2 = 0, 1
    while num2 <= int:
        num1, num2 = num2, num1 + num2
    return num2


def main():
    assert fibonacci(3) == 5
    assert fibonacci(6) == 8
    assert fibonacci(-2) == 1


if __name__ == '__main__':
    main()