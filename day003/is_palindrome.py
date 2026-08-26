"""
Task:
Determine whether a string is a palindrome.

Requirements:
- Return True if the text reads the same forwards and backwards.
- Ignore letter case.
- Ignore spaces.
- Ignore punctuation.
- Do not use reversed().
- Do not use slicing with [::-1].
- Do not create a reversed copy of the string.
- Aim for O(n) time complexity.
"""


def is_palindrome(text: str) -> bool:
    text = text.lower()
    i = 0
    j = len(text) - 1

    while i < j:
        if not text[i].isalnum():
            i += 1
            continue

        if not text[j].isalnum():
            j -= 1
            continue

        if text[i] != text[j]:
            return False

        i += 1
        j -= 1

    return True
