"""
Task:
Find the first non-repeating character in a string.

Requirements:
- Return the first character that appears exactly once.
- The search must be case-sensitive.
- Spaces and punctuation count as characters.
- Return None if every character repeats or the string is empty.
- Do not use collections.Counter.
- Aim for O(n) time complexity.
"""


def first_unique(text: str) -> str | None:
    counts = {}

    for i in text:
        counts[i] = counts.get(i, 0) + 1

    for key, v in counts.items():
        if v == 1:
            return key
        
    return None