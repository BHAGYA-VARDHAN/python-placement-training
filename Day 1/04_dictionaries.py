"""
Dictionaries — Keys, Counting, Sorting & Identity
====================================================
Covers: tuple keys, key-type coercion (int vs float vs str keys),
counting occurrences, sorting by key, and object identity with id().
"""


def dict_with_tuple_keys():
    """Dictionaries can use tuples as keys since tuples are hashable."""
    d = {(1, 2): 1, (2, 3): 2, (4, 5): 3}
    return d[(4, 5)]  # -> 3


def count_occurrences(items):
    """Build a frequency dictionary. Note: dict keys are case-sensitive,
    so 'Apple' and 'apple' are counted as two different keys.
    """
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def int_vs_float_keys_demo():
    """In Python, `1` and `1.0` hash to the same value and are treated
    as the SAME dictionary key (since 1 == 1.0), while the string '1'
    is a distinct key.
    """
    d = {}
    d[1] = 1
    d['1'] = 2
    d[1.0] = 4     # overwrites the value stored at key 1
    return d, sum(d.values())


def sort_dict_by_key(d):
    """Iterating over `sorted(d)` sorts by key, not by value."""
    return [d[k] for k in sorted(d)]


def identity_demo():
    """id() returns a unique identifier (memory address in CPython) for
    an object. Two dicts with equal content are still different objects
    unless one is literally a reference to the other.
    """
    original = {"Name": "Python", "Age": "20"}
    reference = original          # same object
    shallow_copy = original.copy()  # new object, equal content

    return {
        "same_object": id(original) == id(reference),
        "copy_is_different_object": id(original) == id(shallow_copy),
    }


if __name__ == "__main__":
    print("Value at key (4, 5):", dict_with_tuple_keys())

    fruit_counts = count_occurrences(["Apple", "Banana", "apple"])
    print("Fruit counts:", fruit_counts, "| unique keys:", len(fruit_counts))

    d, total = int_vs_float_keys_demo()
    print("Dict with int/float/str keys:", d, "| sum of values:", total)

    print("Sorted by key:", sort_dict_by_key({'c': 97, 'a': 96, 'b': 98}))

    print("Identity checks:", identity_demo())
