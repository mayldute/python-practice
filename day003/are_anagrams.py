"""
Task:
Determine whether two strings are anagrams of each other.

Requirements:
- Return True if both strings contain exactly the same letters
  with the same frequencies.
- Ignore letter case.
- Ignore spaces.
- Do not use collections.Counter.
- Do not use sorted().
- Do not modify the original strings.
- Aim for O(n + m) time complexity.
"""

def count_letters(normalized_text: str) -> dict[str, int]:
    counts = {}

    for char in normalized_text:
        counts[char] = counts.get(char, 0) + 1

    return counts


def are_anagrams(first: str, second: str) -> bool:
    normalized_first = first.lower().replace(" ", "")
    normalized_second = second.lower().replace(" ", "")

    if len(normalized_first) != len(normalized_second):
        return False

    first_letters = count_letters(normalized_first)
    second_letters = count_letters(normalized_second)
    
    return first_letters == second_letters
