"""
Task:
Implement a function that merges two lists while removing duplicates.

Requirements:
- Create a `merge_unique` function.
- Accept two lists of integers.
- Combine both lists.
- Remove duplicate values.
- Preserve the order of first appearance.
- Return a new list.
- Do not modify the input lists.

Examples:
    [1, 2, 3], [3, 4, 5] → [1, 2, 3, 4, 5]
    [3, 1, 2], [2, 1, 4] → [3, 1, 2, 4]
    [1, 1, 2], [2, 2, 3] → [1, 2, 3]
    [], [1, 2] → [1, 2]
"""


def merge_unique(first: list[int], second: list[int]) -> list[int]:
    result = []
    seen = set()

    for number in first:
        if number not in seen:
            result.append(number)
            seen.add(number)

    for number in second:
        if number not in seen:
            result.append(number)
            seen.add(number)

    return result
