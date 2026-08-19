"""
Task:
Find the first element that appears more than once.

Requirements:
- Return the first value whose second occurrence appears earliest.
- Preserve the order in which elements are encountered.
- Return None if there are no duplicates.
- Do not modify the original list.
- Aim for O(n) time complexity.
"""


def first_repeated(items: list[int]) -> int | None:
    seen = set()

    for item in items:
        if item in seen:
            return item

        seen.add(item)

    return None
