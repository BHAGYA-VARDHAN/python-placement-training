"""
Inheritance — Single, Multilevel, Multiple & Method Resolution Order
========================================================================
"""


# ---- Single-level inheritance ----
class College:
    def college_name(self):
        print("SITRC")


class StudentSingle(College):
    def student_info(self):
        print("Name: Bhagyavardhan Nagane | Branch: E&TC")


# ---- Multilevel inheritance ----
class Exam(StudentSingle):
    def subject(self):
        print("Subject1: PDC | Subject2: ML | Subject3: MIC")


# ---- Multiple inheritance ----
class SubjectMarks:
    def __init__(self, math, ml, dl):
        self.math = math
        self.ml = ml
        self.dl = dl


class PracticalMarks:
    def __init__(self, cpract):
        self.cpract = cpract


class Result(SubjectMarks, PracticalMarks):
    def __init__(self, math, ml, dl, cpract):
        SubjectMarks.__init__(self, math, ml, dl)
        PracticalMarks.__init__(self, cpract)

    def total(self):
        passed = self.math >= 40 and self.ml >= 40 and self.dl >= 40 and self.cpract >= 20
        print("Result:", "Pass" if passed else "Fail")


# ---- Diamond problem / Method Resolution Order (MRO) ----
class A:
    def add(self):
        print("A.add() called")


class B:
    def add(self):
        print("B.add() called")


class C(A, B):
    """When both parents define the same method, Python resolves the
    call using MRO (left-to-right as listed in the class definition)."""
    pass


if __name__ == "__main__":
    student = Exam()
    student.college_name()   # inherited from College (single-level)
    student.student_info()   # inherited from StudentSingle
    student.subject()        # defined in Exam (multilevel)

    print()
    result = Result(math=80, ml=75, dl=90, cpract=25)
    result.total()

    print()
    c = C()
    c.add()  # resolves to A.add() due to MRO — this is the "ambiguity problem"
    print("MRO order:", [cls.__name__ for cls in C.__mro__])
