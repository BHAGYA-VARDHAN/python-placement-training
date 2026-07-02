"""
Classes, Objects & Constructors
===================================
The building blocks of OOP: defining a class, creating objects,
and using __init__ as a constructor that runs once per object.
"""


class Student:
    """A minimal class with a class-level data member and a method."""
    roll_no = 101  # class (data) member — shared unless overridden per-instance

    def msg(self):
        print("hello world")


class Demo:
    """Shows that __init__ runs exactly once, automatically, per object."""

    def __init__(self):
        print("Constructor called — runs automatically when the object is created")

    def info(self):
        print("This method was called explicitly on an existing object")


class Hod:
    """A constructor that accepts parameters to initialize instance data."""

    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def show(self):
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Rollno :", self.rollno)


if __name__ == "__main__":
    s = Student()
    print("Roll no:", s.roll_no)
    s.msg()

    print()
    d1 = Demo()   # constructor runs here
    d1.info()
    d2 = Demo()   # constructor runs again for the new object

    print()
    hod = Hod("Bhagyavardhan", 21, 24)
    hod.show()
