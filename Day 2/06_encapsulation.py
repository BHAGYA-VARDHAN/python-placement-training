"""
Encapsulation — Public, Protected & Private Members
=========================================================
Python access control is convention-based, not enforced like Java:
  - public     -> self.name        (accessible from anywhere)
  - protected  -> self._name       (single underscore — "internal use" convention)
  - private    -> self.__name      (double underscore — name-mangled to
                                     _ClassName__name, so it's NOT directly
                                     accessible from outside the class)
"""


class Base:
    def __init__(self):
        self.public_attr = "Bhagyavardhan"     # public
        self._protected_attr = "Rutuja"        # protected (convention only)
        self.__private_attr = "Secret"         # private (name-mangled)

    def reveal_private(self):
        """Private members ARE accessible from inside the class."""
        return self.__private_attr


class Derived(Base):
    def __init__(self):
        Base.__init__(self)


class RBI:
    def public_policy(self):
        print("Public: check the public policy of RBI")

    def __private_policy(self):
        print("Private: internal RBI policy, not exposed publicly")

    def expose_private_policy(self):
        """A public method can act as a controlled gateway to a private one."""
        self.__private_policy()


class SBI(RBI):
    def __init__(self):
        RBI.__init__(self)

    def calling_public_method(self):
        print("Inside child class:")
        self.public_policy()


if __name__ == "__main__":
    obj = Derived()
    print("Public   :", obj.public_attr)
    print("Protected:", obj._protected_attr)  # accessible, but "please don't touch" by convention
    print("Private (via method):", obj.reveal_private())
    # print(obj.__private_attr)              # AttributeError — not accessible directly
    print("Private (name-mangled access):", obj._Base__private_attr)

    print()
    sbi = SBI()
    sbi.calling_public_method()
    sbi.public_policy()
    sbi.expose_private_policy()
    # sbi.__private_policy()                 # AttributeError — private to RBI
