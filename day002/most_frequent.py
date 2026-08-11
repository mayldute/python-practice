"""
Task:
Find the most frequent integer in a list.

Requirements:
- Return the integer that appears most often.
- If multiple integers have the same highest frequency, return the one that appears first in the original list.
- Do not use collections.Counter.
- Do not modify the original list.
- Aim for O(n) time complexity.
"""


def most_frequent(items: list[int]) -> int | None:
    counts = {}

    if not items:
        return None

    for i in items:
        counts[i] = counts.get(i, 0) + 1

    return max(counts, key=counts.get)
