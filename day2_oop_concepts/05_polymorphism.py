"""
Polymorphism — Method/Constructor Overloading & Overriding
===============================================================
Python does NOT support true method overloading (redefining a method
with the same name multiple times just overwrites the previous
definition). The idiomatic workaround is default arguments.
"""


class Arithmetic:
    """Simulates 'overloaded' add() using default arguments, since
    Python keeps only the LAST definition if you write add() 3 times
    with different signatures.
    """

    def add(self, a, b=None, c=None):
        if b is None and c is None:
            print(a)
        elif c is None:
            print(a + b)
        else:
            print(a + b + c)


class ArithmeticConstructor:
    """Same idea applied to __init__: default arguments simulate
    'constructor overloading'."""

    def __init__(self, a=None, b=None):
        if a is None:
            print("No arguments passed")
        elif b is None:
            print("One argument passed:", a)
        else:
            print("Two arguments passed:", a, b)


# ---- Method overriding ----
class RBI:
    def home_loan(self):
        print("RBI base home loan rate: 8%")

    def car_loan(self):
        print("RBI base car loan rate: 7%")


class SBI(RBI):
    def home_loan(self):
        print("SBI home loan rate: 10.5%")
        super().home_loan()  # explicitly call the parent's version too


# ---- Constructor overriding ----
class Father:
    def __init__(self):
        print("Father: I am on time for breakfast.")


class Child(Father):
    def __init__(self):
        print("Child: I will be late for breakfast.")
        super().__init__()


if __name__ == "__main__":
    calc = Arithmetic()
    calc.add(10)
    calc.add(10, 20)
    calc.add(1, 2, 3)

    print()
    ArithmeticConstructor()
    ArithmeticConstructor(10)
    ArithmeticConstructor(2, 2)

    print()
    sbi = SBI()
    sbi.home_loan()
    sbi.car_loan()

    print()
    Child()
