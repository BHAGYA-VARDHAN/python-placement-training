"""
Interview-Style List Problems
================================
Finding repeated numbers, common elements across lists, and the
maximum count of consecutive 1s in a binary list.
"""


def find_repeated_numbers(numbers):
    """Return the list of values that appear more than once."""
    repeated = []
    for value in numbers:
        if numbers.count(value) > 1 and value not in repeated:
            repeated.append(value)
    return repeated


def common_elements(*lists):
    """Return elements present in ALL given lists, preserving order of
    the first list.
    """
    first, rest = lists[0], lists[1:]
    return [item for item in first if all(item in lst for lst in rest)]


def max_consecutive_ones(binary_list):
    """Return the length of the longest run of consecutive 1s."""
    max_count = 0
    current = 0
    for value in binary_list:
        if value == 1:
            current += 1
            max_count = max(max_count, current)
        else:
            current = 0
    return max_count


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 2, 3, 4]
    repeats = find_repeated_numbers(nums)
    print("Repeated numbers:", repeats if repeats else -1)

    n, m, o = [1, 2, 3], [2, 3, 4], [3, 4, 5]
    print("Common to all three lists:", common_elements(n, m, o))

    b = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0]
    print("Max consecutive ones:", max_consecutive_ones(b))
