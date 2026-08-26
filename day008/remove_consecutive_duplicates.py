"""
Task:
Implement a function that removes consecutive duplicates from a list.

Requirements:
- Create a `remove_consecutive_duplicates` function.
- The function accepts a list of integers.
- Remove only duplicates that appear consecutively.
- Keep exactly one copy of each consecutive group.
- If the same value appears again later but is not consecutive, keep it.
- Preserve the original order of the remaining elements.
- Return an empty list for an empty input.

Examples:
    [1, 1, 2, 2, 2, 3] → [1, 2, 3]
    [1, 2, 1, 1] → [1, 2, 1]
    [5, 5, 5, 5] → [5]
    [1, 2, 3, 4] → [1, 2, 3, 4]
    [] → []
"""


def remove_consecutive_duplicates(items: list[int]) -> list[int]:
    if not items:
        return []

    result = [items[0]]

    for i in range(1, len(items)):
        if items[i] != items[i - 1]:
            result.append(items[i])

    return result
