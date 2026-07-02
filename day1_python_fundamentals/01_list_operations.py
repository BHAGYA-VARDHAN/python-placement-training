"""
List Operations — Slicing, Indexing & Modification
=====================================================
Core list manipulation patterns: step slicing, reverse slicing,
in-place replacement via slice assignment, and 2D list (matrix)
element removal.
"""


def slice_every_second_element(numbers):
    """Return every 2nd element of a list, starting from index 0."""
    return numbers[::2]


def replace_every_second_element(numbers, replacements):
    """Replace every 2nd element (in place) with values from `replacements`."""
    numbers[::2] = replacements
    return numbers


def reverse_slice(numbers, start, stop):
    """Return a reversed slice of the list between two indices.

    Example: reverse_slice([1,2,3,4,5], 3, 0) -> [4, 3, 2]
    """
    return numbers[start:stop:-1]


def pop_last_column(matrix):
    """Pop and return the last element of every row in a 2D list (matrix)."""
    return [row.pop() for row in matrix]


def shift_left_in_place(numbers):
    """Shift every element one position to the left (last element stays).

    Example: [1,2,3,4,5,6] -> [2,3,4,5,6,6]
    """
    for i in range(1, len(numbers)):
        numbers[i - 1] = numbers[i]
    return numbers


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Every 2nd element:", slice_every_second_element(nums))

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("After replacing every 2nd element:",
          replace_every_second_element(nums, [10, 20, 30, 40, 50]))

    print("Reversed slice [1..5] from idx 3 to 0:", reverse_slice([1, 2, 3, 4, 5], 3, 0))

    matrix = [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    print("Popped last column:", pop_last_column(matrix))

    print("Shifted left:", shift_left_in_place([1, 2, 3, 4, 5, 6]))
