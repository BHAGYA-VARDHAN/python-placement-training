"""
Tuples & the zip() Function
==============================
Tuple immutability/equality basics, and using zip() to iterate
over multiple iterables in parallel.
"""


def tuple_basics_demo():
    """Show tuple creation (with/without parentheses), equality, and
    concatenation."""
    empty_tuple = ()
    a = 'a', 'b'          # parentheses are optional
    b = ('a', 'b')
    concatenated = ('1', '2') + ('3', '4')
    return {
        "empty_len": len(empty_tuple),
        "implicit_equals_explicit": a == b,
        "concatenated": concatenated,
    }


def zip_with_skip(range_a, range_b, skip_when_equal=None):
    """Pair up two ranges with zip(), optionally skipping a pair where
    both values match `skip_when_equal`.

    zip() combines iterables element-wise into tuples and stops as
    soon as the shortest iterable is exhausted.
    """
    pairs = []
    for i, j in zip(range_a, range_b):
        if skip_when_equal is not None and i == j == skip_when_equal:
            continue
        pairs.append((i, j))
    return pairs


if __name__ == "__main__":
    print(tuple_basics_demo())

    result = zip_with_skip(range(1, 6), range(5, 0, -1), skip_when_equal=3)
    for i, j in result:
        print(i, j)
