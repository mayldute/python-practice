"""
Task:
Count the number of vowels in a given text.

Requirements:
- Count only English vowels: a, e, i, o, u.
- Handle both lowercase and uppercase letters.
- Ignore spaces, numbers, and punctuation.
- Return the total number of vowels as an integer.
- Aim for O(n) time complexity.
"""

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a given text.
    """
    vowels = {"a", "e", "i", "o", "u"}
    return sum(1 for char in text if char.lower() in vowels)
