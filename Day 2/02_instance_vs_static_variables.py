"""
Instance Variables vs Static (Class) Variables
==================================================
Instance variables belong to a single object. Static/class variables
are shared across every instance of the class — updating them via the
class updates the value seen by ALL existing objects.
"""


class New:
    """`a` is a class (static) variable; `name` is set as an instance
    variable per-object."""
    a = 10

    def __init__(self):
        self.name = "Bhagya"


class College:
    """Static member `collegename` is shared; `studentname` is per-object."""
    collegename = "Modern College"

    def __init__(self):
        self.studentname = "Bhagya"


class Student:
    """Demonstrates adding and deleting instance attributes dynamically,
    plus static methods (which don't need `self` or an instance at all).
    """

    def __init__(self, name):
        self.s_name = name
        self.s_rollno = 101

    def add_mobile(self, mobile_number):
        self.s_mb = mobile_number

    @staticmethod
    def get_personal_details(firstname, lastname):
        print("Personal detail:", firstname, lastname)

    @staticmethod
    def contact_detail(mobile_no, roll_no):
        print("Contact detail:", mobile_no, roll_no)


if __name__ == "__main__":
    obj1, obj2, obj3 = New(), New(), New()
    New.a = 50  # changing the class variable affects every instance
    print("Static variable seen by all instances:", obj1.a, obj2.a, obj3.a)

    print()
    principal, teacher, accountant = College(), College(), College()
    College.collegename = "SITRC"
    principal.studentname = "Bhagyavardhan Nagane"
    print("principal:", principal.collegename, "|", principal.studentname)
    print("teacher  :", teacher.collegename, "|", teacher.studentname)
    print("accountant:", accountant.collegename, "|", accountant.studentname)

    print()
    student = Student("Bhagya")
    student.add_mobile(9999999999)
    student.s_branch = "E&TC"       # adding an instance attribute dynamically
    del student.s_rollno            # deleting an instance attribute
    print("Dynamic attributes:", student.__dict__)

    Student.get_personal_details("Bhagyavardhan", "Nagane")
    Student.contact_detail(9999999999, 24)
