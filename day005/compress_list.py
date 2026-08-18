"""
Task:
Compress consecutive duplicate values in a list.

Requirements:
- Replace each consecutive group of identical values with one value.
- Preserve the original order.
- Only consecutive duplicates should be removed.
- Do not use set().
- Do not use itertools.groupby().
- Do not modify the original list.
- Return a new list.
- Aim for O(n) time complexity.
"""


def compress_list(items: list[int]) -> list[int]:
    if not items:
        return []
    
    result = [items[0]]

    for index in range(1, len(items)):
        if items[index] != items[index - 1]:
            result.append(items[index])

    return result
