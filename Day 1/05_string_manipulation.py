"""
String Manipulation — Classic Interview Problems
====================================================
Reversing a string manually, checking palindromes, and removing
duplicate characters while preserving order.
"""


def reverse_string(text):
    """Reverse a string by walking it backwards (without slicing)."""
    reversed_text = ""
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]
    return reversed_text


def is_palindrome(sequence):
    """Check whether a list or string reads the same forwards and backwards."""
    return sequence == sequence[::-1]


def remove_duplicate_chars(text):
    """Remove duplicate characters from a string, preserving first-seen order."""
    seen = ""
    for char in text:
        if char not in seen:
            seen += char
    return seen


if __name__ == "__main__":
    print("Reversed 'hello':", reverse_string("hello"))

    print("Is [1,2,3,2,1] a palindrome?", is_palindrome([1, 2, 3, 2, 1]))

    print("Deduplicated 'bhagyavardhan':", remove_duplicate_chars("bhagyavardhan"))
