"""
The purpose of this file is to show how loosely typed, 
interpreted language can behave strangely.

We define two classes A, B which override some special methods.
  * The < operator (less than)
  * The + operator (add)
  * the toString method

The addition operator doesn't actually do addition.

To reduce the redundant code, B inherits from A.
But, B has its own definition for less than (<).

Lastly, there is a method named strange. Note that the code
compiles and runs just fine because we don't ever call
the method strange(). Can you explain why?

Play around with the code for a bit. What odd behaviors
can you get the program to do?

Activity Objectives:
* What was expected?
* How does it behave differently from Java?
* What was surprising?
* What did you learn?
* What is confusing?
* What questions do you have?

"""


class A:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return True

    def __add__(self, other):
        return A(self.value + other.value)

    def __str__(self):
        return str(self.value)


class B(A):
    def __lt__(self, other):
        return False


def loose(o1, o2):
    """
    This one method will work with all objects that implement both
       __lt__
       __add__
    """
    if o1 < o2:
        print(f"{o1} < {o2}")
    else:
        print(f"{o1} >= {o2}")
    print(f"{o1} + {o2} = {o1 + o2}")


def strange(b):
    if b.no_existence():
        b.complain()


def identifier_t():
    t = 7
    t = str(t) + " is prime"
    t = A(7)


def main():
    a = A(1)
    b = B(2)
    loose(a, b)


if __name__ == "__main__":
    main()
