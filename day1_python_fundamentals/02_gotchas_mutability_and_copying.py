"""
Python Gotchas — Mutable Default Arguments & Shallow vs Deep Copy
====================================================================
Two of the most common interview trip-ups for Python beginners.
"""


def append_to_shared_list(item, values=None):
    """Correct pattern: use `None` as the default, not a mutable list.

    WARNING (the classic bug): if you write `def f(i, values=[])`, the
    default list is created ONCE when the function is defined and is
    REUSED across every call that doesn't pass its own list — so it
    silently accumulates values across calls. Using `None` + creating
    a fresh list inside the function avoids that trap entirely.
    """
    if values is None:
        values = []
    values.append(item)
    return values


def demonstrate_shallow_vs_deep_copy():
    """Show the difference between reference assignment, shallow copy,
    and deep copy for lists.
    """
    fruit_list1 = ["apple", "banana", "cherry", "papaya"]
    fruit_list2 = fruit_list1        # same object (reference/alias)
    fruit_list3 = fruit_list1[:]     # independent copy (shallow copy of a flat list)

    fruit_list2[0] = "kiwi"    # mutates fruit_list1 too, since they're the same object
    fruit_list3[1] = "mango"   # only affects fruit_list3

    return fruit_list1, fruit_list2, fruit_list3


if __name__ == "__main__":
    # Buggy pattern demo: calling repeatedly with the same mutable default
    # would leak state between calls. Here we call it correctly instead.
    print(append_to_shared_list(1))
    print(append_to_shared_list(2))
    print(append_to_shared_list(3))

    l1, l2, l3 = demonstrate_shallow_vs_deep_copy()
    print("list1 (aliased, mutated via list2):", l1)
    print("list2 (same object as list1):", l2)
    print("list3 (independent copy):", l3)
